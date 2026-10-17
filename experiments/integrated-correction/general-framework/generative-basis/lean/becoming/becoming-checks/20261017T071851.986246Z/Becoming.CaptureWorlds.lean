import Becoming.Capture

/-!
# Capture in worlds: a target's share among descendants

`Becoming.Capture` states the share of a target among offspring for any family of parents and
any listing of their offspring (`share_not_lower`, `share_rises`), and `Becoming.Evolution` states
selection through support in a world: where only active formations give and activity needs
support, a formation unsupported at a step leaves no descendant across it
(`unsupported_childless`). This module joins the two. Read the offspring of each parent as
relata descending from it across a step of a world's flow (`Flow.DescendsAt`).

* **Unsupported others, rising share.** Where the formations not carrying a target are
  unsupported at the step, and each carrier leaves at least one descendant across it, the
  carriers' descendants stand to the others' strictly more than the carriers stand to the others
  (`share_rises_of_unsupported`), and the others leave none (`unsupported_leave_none`); with no
  count of the carriers' descendants, the share does not fall (`share_not_lower_of_unsupported`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace CaptureWorlds

variable {X : Type} {L : Flow X X} {W : Web X X}

/-- A list with no member has length zero. -/
theorem length_le_zero {l : List X} (none : ∀ k, k ∈ l → False) : l.length ≤ 0 :=
  match l, none with
  | [], _ => Nat.le_refl 0
  | k :: _, none => (none k (.head _)).elim

/-- **Formations unsupported at a step leave no descendant listed across it.** Where only
active formations give and activity needs support, an unsupported formation's listed
descendants across the step number none. -/
theorem unsupported_leave_none (acting : L.Acting W) (dependent : W.Dependent) {t : Nat}
    {es : List X} {kids : X → List X} (descend : ∀ p k, p ∈ es → k ∈ kids p → L.DescendsAt W t k p)
    (unsupported : ∀ p, p ∈ es → ¬ W.Supported t p) : ∀ p, p ∈ es → (kids p).length ≤ 0 :=
  fun p mem => length_le_zero fun k kid =>
    Flow.unsupported_childless acting dependent (unsupported p mem) k (descend p k mem kid)

/-- **Selection through support raises a target's share.** Where only active formations give
and activity needs support, the formations not carrying a target are unsupported at the step and
their listed offspring descend from them across it, and each carrier leaves at least one listed
descendant, the carriers' descendants stand to the others' strictly more than the carriers stand
to the others, both kinds present. -/
theorem share_rises_of_unsupported (acting : L.Acting W) (dependent : W.Dependent) {t : Nat}
    {ms es : List X} {kids : X → List X} {a : Nat}
    (descend : ∀ p k, p ∈ es → k ∈ kids p → L.DescendsAt W t k p)
    (unsupported : ∀ p, p ∈ es → ¬ W.Supported t p)
    (carriers : ∀ p, p ∈ ms → a ≤ (kids p).length) (pos : 0 < a)
    (some : 0 < ms.length) (some' : 0 < es.length) :
    ms.length * offspringCount es kids < offspringCount ms kids * es.length :=
  share_rises carriers (unsupported_leave_none acting dependent descend unsupported) pos some some'

/-- **Selection through support keeps a target's share from falling.** Where only active
formations give and activity needs support, and the formations not carrying a target are
unsupported at the step with their listed offspring descending from them across it, the carriers'
descendants stand to the others' at least as the carriers stand to the others. -/
theorem share_not_lower_of_unsupported (acting : L.Acting W) (dependent : W.Dependent) {t : Nat}
    {ms es : List X} {kids : X → List X}
    (descend : ∀ p k, p ∈ es → k ∈ kids p → L.DescendsAt W t k p)
    (unsupported : ∀ p, p ∈ es → ¬ W.Supported t p) :
    ms.length * offspringCount es kids ≤ offspringCount ms kids * es.length :=
  share_not_lower (a := 0) (fun _ _ => Nat.zero_le _)
    (unsupported_leave_none acting dependent descend unsupported) (Nat.le_refl 0)

end CaptureWorlds

end Becoming
