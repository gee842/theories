import Becoming.Tail
import Becoming.Runs

/-!
# Sensitivity on webs and flows: what depends on the whole, read off the courses

`Becoming.Sensitivity` and `Becoming.Tail` state, of a law of exchange and the level histories it
reads, that what depends on the whole depends on some part, and that a law of the whole and no
part does not read through what it is sensitive to. A law of exchange enters the unfolding
through the flows that follow it along webs (`Flow.Follows`, `Becoming.Counterfactual`), through
the couplings of a web it reads through (`ExchangeLaw.Through`), and through its course, a
world (`ExchangeLaw.courseWorld`, `Becoming.Runs`). This module states those laws there.

* **Flows following a law exchange alike where it depends on no single condition.** At a step at
  which the law is, for a formation outside the part, insensitive to every condition, two flows
  following it along two webs exchange alike for that formation wherever the law reads within a
  list of conditions under the second web's levels (`exchange_alike_of_insensitiveAt`); where the
  law reads finitely many conditions and the formation's exchange is sensitive to none, they
  exchange alike at every step, whatever the webs (`exchange_alike_of_insensitive`).
* **The law of a whole does not read through what it is sensitive to, on a web.** On a web in
  which the formation depends on nothing, the law exchanging a number no condition changes, where
  that number differs between two levels, does not read through the coupling of what it is sensitive
  to (`wholeLaw_not_through`); the tail law's form is `tailLaw_not_through` of
  `Becoming.Sensitivity`.
* **The tail law's course is a world.** The course the tail law generates is a balanced world
  exactly where it is feasible (`tailLaw_courseWorld_balanced_iff`), since the tail law reads what
  has stood.

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace SensitivityWebs

/-! ## Flows following a law -/

section Flows

variable {F C : Type} [DecidableEq C] {law : ExchangeLaw F C} {part : F → Bool}
  {L L' : Flow F C} {W W' : Web F C}

/-- **Where the law is insensitive at a step to every condition, two flows following it exchange
alike there**, for a formation outside the part, wherever the law reads within a list under the
second web's levels. Any number of conditions; nothing is decided of sensitivity. -/
theorem exchange_alike_of_insensitiveAt (follows : L.Follows law part W.level)
    (follows' : L'.Follows law part W'.level) {h : F} (out : part h = false) {t : Nat}
    (insensitive : ∀ c, law.InsensitiveAt t h c) {cs : List C}
    (within : law.ReadsWithin t h W'.level cs) (c : C) :
    L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c :=
  have same := alike_of_insensitiveAt_within insensitive within c
  ⟨(follows h out t c).1.trans (same.1.trans (follows' h out t c).1.symm),
   (follows h out t c).2.trans (same.2.trans (follows' h out t c).2.symm)⟩

/-- **Where the law reads finitely many conditions and a formation's exchange is sensitive to
none, every two flows following it exchange alike for that formation at every step**, whatever
the webs they follow it along. -/
theorem exchange_alike_of_insensitive (fin : law.ReadsFinitely)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level) {h : F}
    (out : part h = false) (nothing : ∀ c, ¬ law.Sensitive h c) (t : Nat) (c : C) :
    L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c :=
  have same := fin.alike_of_insensitive nothing t W.level W'.level c
  ⟨(follows h out t c).1.trans (same.1.trans (follows' h out t c).1.symm),
   (follows h out t c).2.trans (same.2.trans (follows' h out t c).2.symm)⟩

end Flows

/-! ## The law of a whole on a web -/

/-- **On a web in which the formation depends on nothing, the law of a number no condition
changes, where the number differs, does not read through what it is sensitive to.** -/
theorem wholeLaw_not_through {f : (Nat → Nat) → Nat} (fixed : ChangedByNoCondition f)
    {α β : Nat → Nat} (differs : f α ≠ f β) {W : Web Unit Nat}
    (free : ∀ t c, ¬ W.requires t () c) :
    ¬ (wholeLaw f).Through W (wholeLaw f).Sensitive (fun _ => false) :=
  fun through => wholeLaw_not_through_sensitive fixed differs fun t l l' agree =>
    through () rfl t l l' fun s le =>
      ⟨⟨fun _ c requires => absurd requires (free s c),
        fun _ c requires => absurd requires (free s c)⟩,
       fun c sensitive => agree c sensitive s le⟩

/-! ## The tail law's course -/

/-- **The course the tail law generates is a balanced world exactly where it is feasible.** -/
theorem tailLaw_courseWorld_balanced_iff (decides : ∀ α : Nat → Nat, Decidable (VanishFrom α))
    {present : Nat → List Unit} {start : Nat → Nat} {W : Web Unit Nat} :
    ((tailLaw decides).courseWorld present start W).Balanced ↔
      (tailLaw decides).Feasible present start :=
  ExchangeLaw.courseWorld_balanced_iff (tailLaw_nonanticipating decides)

end SensitivityWebs

end Becoming
