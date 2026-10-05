import PaidArchiveReader
import ReasonReplay

namespace RecipientReasons

set_option maxRecDepth 4096
set_option maxHeartbeats 2000000

open RecipientCorrection (receiptOf)

structure Triple where
  first : Option Bool
  second : Option Bool
  third : Option Bool
  deriving DecidableEq, Repr

def empty : Triple := ⟨none,none,none⟩
def normalize (desired : Bool) : Option Bool → Option Bool
  | none => none
  | some b => some (if b then desired else !desired)

def entrySound (z : Bool) (x : Option Bool) : Prop := ∀ v, x=some v → v=z
def Sound (z : Bool) (t : Triple) : Prop :=
  entrySound z t.first ∧ entrySound z t.second ∧ entrySound z t.third

def known (z : Bool) (t : Triple) : Bool :=
  t.first == some z || t.second == some z || t.third == some z

def conflict (t : Triple) : Bool := known false t && known true t

def orientation (t : Triple) : Option Bool :=
  if known false t then if known true t then none else some false
  else if known true t then some true else none

def derived (t : Triple) : List (Option Bool) :=
  match orientation t with
  | none => [none,none,none]
  | some z => [some (!z),some z,none]

def star : ReasonReplay.Graph := ⟨(.root,.p),(.root,.q),(.root,.p)⟩

def Compatible (z action : Bool) : Prop := ∀ available, receiptOf action z available=available

def Meaning (G : Prop) (z : Bool) : ReasonReplay.Node → Prop
  | .root => G
  | .p => G ∧ Compatible z false
  | .q => G ∧ Compatible z true

theorem compatible_iff (z action : Bool) : Compatible z action ↔ action=z := by
  cases z <;> cases action <;> simp [Compatible,receiptOf]

theorem normalization_sound {desired z : Bool} {x : Option Bool}
    (h : ∀ b, x=some b → b=(z==desired)) : entrySound z (normalize desired x) := by
  cases x with
  | none => simp [entrySound,normalize]
  | some b =>
      have hb := h b rfl
      clear h
      cases z <;> cases desired <;> cases b <;> simp_all [entrySound,normalize]

def normalizeFacts (xs : List (Bool × Option Bool)) : List (Option Bool) :=
  xs.map (fun x => normalize x.1 x.2)

def ListSound (z : Bool) (xs : List (Option Bool)) : Prop :=
  ∀ x, x ∈ xs → entrySound z x

def firstKnown : List (Option Bool) → Option Bool
  | [] => none
  | none::xs => firstKnown xs
  | some z::_ => some z

theorem finite_normalization_sound {z : Bool} {xs : List (Bool × Option Bool)}
    (h : ∀ d x, (d,x) ∈ xs → ∀ b, x=some b → b=(z==d)) :
    ListSound z (normalizeFacts xs) := by
  intro x hx
  rcases List.mem_map.mp hx with ⟨⟨d,observed⟩,hm,rfl⟩
  exact normalization_sound (h d observed hm)

theorem finite_known_agree {z a b : Bool} {xs : List (Option Bool)}
    (h : ListSound z xs) (ha : some a ∈ xs) (hb : some b ∈ xs) : a=b := by
  exact (h _ ha a rfl).trans (h _ hb b rfl).symm

theorem finite_no_conflict {z : Bool} {xs : List (Option Bool)} (h : ListSound z xs) :
    ¬ (some false ∈ xs ∧ some true ∈ xs) := by
  intro bad
  have impossible := finite_known_agree h bad.1 bad.2
  cases impossible

theorem first_known_sound {z v : Bool} {xs : List (Option Bool)}
    (h : ListSound z xs) (hv : firstKnown xs=some v) : v=z := by
  induction xs with
  | nil => cases hv
  | cons x xs ih =>
      cases x with
      | none => exact ih (fun x hx => h x (by simp [hx])) hv
      | some a =>
          have ha : a=v := Option.some.inj hv
          subst v
          exact h _ (by simp) a rfl

theorem finite_informative_identifies {z : Bool} {xs : List (Option Bool)}
    (h : ListSound z xs) (hi : ∃ a, some a ∈ xs) : firstKnown xs=some z := by
  induction xs with
  | nil => simp at hi
  | cons x xs ih =>
      cases x with
      | none =>
          apply ih (fun x hx => h x (by simp [hx]))
          simpa using hi
      | some a =>
          have ha := h _ (by simp) a rfl
          simp [firstKnown,ha]

theorem finite_identifies_compatible {z a : Bool} {xs : List (Option Bool)}
    (h : ListSound z xs) (ha : firstKnown xs=some a) : Compatible z a :=
  (compatible_iff z a).mpr (first_known_sound h ha)

theorem normalization_preserves_unknown (d : Bool) : normalize d none=none := rfl

theorem negative_fact_is_informative (d : Bool) : normalize d (some false)=some (!d) := rfl

theorem option_bool_cases (x : Option Bool) : x=none ∨ x=some false ∨ x=some true := by
  cases x with
  | none => exact Or.inl rfl
  | some b => cases b <;> simp

theorem sound_no_conflict {z : Bool} {t : Triple} (h : Sound z t) : conflict t=false := by
  rcases option_bool_cases t.first with ha|ha|ha <;>
    rcases option_bool_cases t.second with hb|hb|hb <;>
    rcases option_bool_cases t.third with hc|hc|hc <;>
    cases z <;> simp_all [Sound,entrySound,conflict,known]

theorem sound_orientation {z v : Bool} {t : Triple}
    (h : Sound z t) (ho : orientation t=some v) : v=z := by
  rcases option_bool_cases t.first with ha|ha|ha <;>
    rcases option_bool_cases t.second with hb|hb|hb <;>
    rcases option_bool_cases t.third with hc|hc|hc <;>
    cases z <;> simp_all [Sound,entrySound,orientation,known]

theorem sound_informative {z : Bool} {t : Triple} (h : Sound z t)
    (hi : t.first≠none ∨ t.second≠none ∨ t.third≠none) : orientation t=some z := by
  rcases option_bool_cases t.first with ha|ha|ha <;>
    rcases option_bool_cases t.second with hb|hb|hb <;>
    rcases option_bool_cases t.third with hc|hc|hc <;>
    cases z <;> simp_all [Sound,entrySound,orientation,known]

theorem unknown_is_not_conflict : orientation empty=none ∧ conflict empty=false := by decide

theorem conflict_is_distinct :
    orientation ⟨some false,some true,none⟩=none ∧
    conflict ⟨some false,some true,none⟩=true := by decide

theorem closure_of_orientation (t : Triple) :
    ReasonReplay.closureMask star (derived t) =
      match orientation t with
      | none => ReasonReplay.emptyMask
      | some z => ⟨!z,z⟩ := by
  cases ho : orientation t with
  | none => simp [derived,ho,ReasonReplay.closureMask,ReasonReplay.paths,ReasonReplay.applyPath,
      ReasonReplay.endpoint,ReasonReplay.pathValid,ReasonReplay.edge,star,ReasonReplay.positive,
      ReasonReplay.emptyMask]
  | some z => cases z <;>
      simp [derived,ho,ReasonReplay.closureMask,ReasonReplay.paths,ReasonReplay.applyPath,
        ReasonReplay.endpoint,ReasonReplay.pathValid,ReasonReplay.edge,star,ReasonReplay.positive,
        ReasonReplay.emptyMask]

theorem informative_exact_route {z : Bool} {t : Triple} (h : Sound z t)
    (hi : t.first≠none ∨ t.second≠none ∨ t.third≠none) :
    ReasonReplay.closureMask star (derived t) = ⟨!z,z⟩ := by
  rw [closure_of_orientation,sound_informative h hi]

theorem actual_relevance {G : Prop} {z : Bool} {t : Triple} (hs : Sound z t)
    {u v : ReasonReplay.Node} (he : ReasonReplay.edge star (derived t) u v=true)
    (hu : Meaning G z u) : Meaning G z v := by
  cases ho : orientation t with
  | none => simp [derived,ho,ReasonReplay.edge,star,ReasonReplay.positive] at he
  | some o =>
      have hz := sound_orientation hs ho
      subst o
      cases u <;> cases v <;> cases z <;>
        simp_all [derived,ReasonReplay.edge,star,ReasonReplay.positive,Meaning,compatible_iff]

theorem closure_instrumental_sound {G : Prop} {z : Bool} {t : Triple}
    (root : G) (hs : Sound z t) {v : ReasonReplay.Node}
    (hm : (ReasonReplay.closureMask star (derived t)).has v) : Meaning G z v := by
  apply ReasonReplay.closure_semantic_sound star (derived t) (Meaning G z) root _ hm
  intro u v he hu
  exact actual_relevance hs he hu

def cacheTriple (s : PaidArchiveReader.State W) : Triple :=
  ⟨normalize false (s.cache 0),normalize true (s.cache 1),normalize false (s.cache 2)⟩

theorem current_cache_normalizes_sound {s : PaidArchiveReader.State W} {z : Bool}
    (hc : PaidArchiveReader.Complete s) (ha : PaidArchiveReader.CacheAgrees s)
    (hf : PaidArchiveReader.Facts z s) : Sound z (cacheTriple s) := by
  constructor
  · apply normalization_sound; intro b hb
    simpa [RecipientArchive.designated] using
      PaidArchiveReader.completed_paid_cache_sound hc ha hf (show 0<3 by decide) hb
  constructor
  · apply normalization_sound; intro b hb
    simpa [RecipientArchive.designated] using
      PaidArchiveReader.completed_paid_cache_sound hc ha hf (show 1<3 by decide) hb
  · apply normalization_sound; intro b hb
    simpa [RecipientArchive.designated] using
      PaidArchiveReader.completed_paid_cache_sound hc ha hf (show 2<3 by decide) hb

end RecipientReasons
