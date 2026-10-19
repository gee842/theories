import Becoming.Frame
import Becoming.Integers
import Becoming.Decidedness

/-!
# Coverage: a placement course, the global cover it builds, and an invariant that rules it out

A board is a finite list of cells; a tile covers two cells a supplied relation allows together.
**Placing** a tile is a step of a process (`placement`): it removes the two cells from the board, in
any order of the rest. A course of placements ends at a rest of the board exactly where the tiles
are each allowed and the board is their cells together with the rest, up to order (`Global`,
`realizes_iff_global`); it covers the board exactly where it does so with nothing left
(`complete_trace_iff`). The global cover holds no event order: one cover is reached by more than one
order of placement (`two_tile_orders`).

**An invariant of the cover.** Where each allowed tile joins two cells of opposite colours, the
balance of colours (`balance`, counting `+1` and `-1`) is kept under reordering (`balance_perm`) and
by each tile (`opposite_pair_balance`), so a cover keeps it (`global_balance`): a board whose balance
is not `0` has no cover and no course of placements covering it (`unbalanced_no_cover`,
`unbalanced_no_placement_history`). On the eight-by-eight board with two opposite corners removed,
adjacent cells have opposite colours (`adjacent_opposite`) and the balance is `-2`
(`mutilated_balance`), so it has no cover by adjacent pairs and no placement course covering it
(`mutilated_no_cover`, `mutilated_no_history`). The invariant is necessary, not sufficient: two
cells three apart in a row balance and cannot be covered (`separated_balanced`,
`separated_not_coverable`), so the balance does not determine coverability
(`balance_does_not_determine_coverability`).

A matched rival to a history-first reading: the same question answered by a global condition and by
a course of steps. The colouring is a supplied reading of the board, not a law of placement. This
module states in the core what `ExplanatoryStructure` and one theorem of `ExplanatoryUniqueness`
(6 October 2026) proved with Lean's list and integer lemmas, which carry `propext`; the permutation
facts and integer laws here are constructive (board item F3E, 18 October 2026). No ethical
predicate, ranking or axiom occurs; every declaration has an empty axiom report.

`Coverage.Perm.mem` is in `Becoming.Decidedness`, so `Becoming.ListFootprints` does not import the
frame (board item W).
-/

namespace Becoming

open Generative

universe u

namespace Coverage

variable {C : Type u}

/-! ## Support: reordering, constructively -/

theorem Perm.length_eq {l l' : List C} (h : l.Perm l') : l.length = l'.length := by
  induction h with
  | nil => rfl
  | cons _ _ ih => exact congrArg Nat.succ ih
  | swap _ _ _ => rfl
  | trans _ _ ih ih' => exact ih.trans ih'

theorem Perm.eq_nil {l : List C} (h : l.Perm []) : l = [] :=
  match l, Perm.length_eq h with
  | [], _ => rfl

/-! ## Placement and the global cover -/

/-- The cells of a list of tiles. -/
def cells : List (C × C) → List C
  | [] => []
  | (a, b) :: ts => a :: b :: cells ts

/-- Every tile is allowed. -/
def Legal (tile : C → C → Prop) : List (C × C) → Prop
  | [] => True
  | (a, b) :: ts => tile a b ∧ Legal tile ts

/-- Placing an allowed tile removes its two cells from the board, in any order of the rest. -/
def placement (tile : C → C → Prop) : Process (List C) (C × C) where
  step board ab rest := tile ab.1 ab.2 ∧ board.Perm (ab.1 :: ab.2 :: rest)

/-- A course of placements ends at the rest, up to order. -/
def Realizes (tile : C → C → Prop) (board : List C) (ts : List (C × C)) (rest : List C) : Prop :=
  ∃ last, Trace (placement tile) board ts last ∧ last.Perm rest

/-- The global cover: the tiles are allowed and the board is their cells and the rest, up to
order. -/
def Global (tile : C → C → Prop) (board : List C) (ts : List (C × C)) (rest : List C) : Prop :=
  Legal tile ts ∧ board.Perm (cells ts ++ rest)

/-- A course of placements builds a global cover. -/
theorem trace_global {tile : C → C → Prop} {board last : List C} {ts : List (C × C)}
    (h : Trace (placement tile) board ts last) : Global tile board ts last := by
  induction h with
  | nil s => exact ⟨True.intro, List.Perm.refl s⟩
  | @cons s m t ab ts hs ht ih =>
    cases ab with
    | mk a b => exact ⟨⟨hs.1, ih.1⟩, hs.2.trans (.cons a (.cons b ih.2))⟩

/-- A global cover is reached by a course of placements. -/
theorem global_realized {tile : C → C → Prop} {board rest : List C} :
    ∀ {ts : List (C × C)}, Global tile board ts rest → Realizes tile board ts rest
  | [], h => ⟨board, .nil _, h.2⟩
  | (_, _) :: ts, h =>
    match global_realized (board := cells ts ++ rest) (ts := ts) ⟨h.1.2, List.Perm.refl _⟩ with
    | ⟨last, path, same⟩ => ⟨last, .cons ⟨h.1.1, h.2⟩ path, same⟩

/-- **A course of placements reaches a rest exactly where the global cover holds.** -/
theorem realizes_iff_global (tile : C → C → Prop) (board : List C) (ts : List (C × C))
    (rest : List C) : Realizes tile board ts rest ↔ Global tile board ts rest :=
  ⟨fun ⟨_, path, same⟩ => match trace_global path with
    | ⟨legal, perm⟩ => ⟨legal, perm.trans (List.Perm.append_left (cells ts) same)⟩,
   global_realized⟩

/-- **A course of placements covers the board exactly where the global cover with nothing left
holds.** -/
theorem complete_trace_iff (tile : C → C → Prop) (board : List C) (ts : List (C × C)) :
    Trace (placement tile) board ts [] ↔ Global tile board ts [] :=
  ⟨trace_global, fun h => match global_realized h with
    | ⟨_, path, same⟩ => (Perm.eq_nil same) ▸ path⟩

/-- **One cover, two orders of placement.** -/
theorem two_tile_orders (tile : C → C → Prop) (a b c d : C) (hab : tile a b) (hcd : tile c d) :
    Trace (placement tile) [a, b, c, d] [(a, b), (c, d)] [] ∧
      Trace (placement tile) [a, b, c, d] [(c, d), (a, b)] [] :=
  have swapped : [a, b, c, d].Perm [c, d, a, b] :=
    ((List.Perm.swap c b [d]).cons a).trans ((List.Perm.swap c a [b, d]).trans
      ((((List.Perm.swap d b []).cons a).trans (List.Perm.swap d a [b])).cons c))
  ⟨.cons ⟨hab, List.Perm.refl _⟩ (.cons ⟨hcd, List.Perm.refl _⟩ (.nil _)),
   .cons ⟨hcd, swapped⟩ (.cons ⟨hab, List.Perm.refl _⟩ (.nil _))⟩

/-! ## The balance of colours -/

/-- `+1` for one colour, `-1` for the other. -/
def charge (color : C → Bool) (c : C) : Int := if color c then 1 else -1

/-- The balance of colours of a list of cells. -/
def balance (color : C → Bool) : List C → Int
  | [] => 0
  | c :: rest => charge color c + balance color rest

/-- **The balance is kept under reordering.** -/
theorem balance_perm (color : C → Bool) {xs ys : List C} (h : xs.Perm ys) :
    balance color xs = balance color ys := by
  induction h with
  | nil => rfl
  | cons a _ ih => exact congrArg (fun z => charge color a + z) ih
  | swap a b xs => exact Integers.add_left_comm (charge color b) (charge color a) (balance color xs)
  | trans _ _ ih ih' => exact ih.trans ih'

/-- **A tile of two opposite colours keeps the balance.** -/
theorem opposite_pair_balance (color : C → Bool) (a b : C) (rest : List C)
    (h : color b = !color a) : balance color (a :: b :: rest) = balance color rest := by
  show charge color a + (charge color b + balance color rest) = balance color rest
  unfold charge
  rw [h]
  cases color a with
  | false =>
    exact (Integers.add_assoc (-1) 1 _).symm.trans
      ((congrArg (· + balance color rest) (Integers.add_left_neg 1)).trans (Integers.zero_add _))
  | true =>
    exact (Integers.add_assoc 1 (-1) _).symm.trans
      ((congrArg (· + balance color rest) (Integers.add_right_neg 1)).trans (Integers.zero_add _))

theorem legal_balance (tile : C → C → Prop) (color : C → Bool)
    (opposite : ∀ a b, tile a b → color b = !color a) :
    ∀ {ts : List (C × C)}, Legal tile ts → ∀ rest : List C,
      balance color (cells ts ++ rest) = balance color rest
  | [], _, _ => rfl
  | (a, b) :: ts, h, rest =>
    (opposite_pair_balance color a b (cells ts ++ rest) (opposite a b h.1)).trans
      (legal_balance tile color opposite h.2 rest)

/-- **A cover keeps the balance.** -/
theorem global_balance (tile : C → C → Prop) (color : C → Bool)
    (opposite : ∀ a b, tile a b → color b = !color a) {board rest : List C} {ts : List (C × C)}
    (h : Global tile board ts rest) : balance color board = balance color rest :=
  (balance_perm color h.2).trans (legal_balance tile color opposite h.1 rest)

/-- **A board whose balance is not `0` has no cover.** -/
theorem unbalanced_no_cover (tile : C → C → Prop) (color : C → Bool)
    (opposite : ∀ a b, tile a b → color b = !color a) (board : List C)
    (h : balance color board ≠ 0) : ¬ ∃ ts, Global tile board ts [] :=
  fun ⟨_, cover⟩ => h (global_balance tile color opposite cover)

/-- **and no course of placements covering it.** -/
theorem unbalanced_no_placement_history (tile : C → C → Prop) (color : C → Bool)
    (opposite : ∀ a b, tile a b → color b = !color a) (board : List C)
    (h : balance color board ≠ 0) : ¬ ∃ ts, Trace (placement tile) board ts [] :=
  fun ⟨ts, path⟩ => unbalanced_no_cover tile color opposite board h ⟨ts, trace_global path⟩

/-! ## The board with two opposite corners removed -/

/-- The cells of an eight-by-eight board. -/
abbrev Square := Fin 64

def chessColor (c : Square) : Bool := (c.val / 8 + c.val % 8) % 2 == 0

def adjacent (a b : Square) : Prop :=
  (a.val / 8 = b.val / 8 ∧ (a.val + 1 = b.val ∨ b.val + 1 = a.val)) ∨
    (a.val + 8 = b.val ∨ b.val + 8 = a.val)

/-- The board with the corners `0` and `63` removed. -/
def mutilated : List Square := (List.finRange 64).filter (fun c => c.val != 0 && c.val != 63)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 2000000 in
/-- **Adjacent cells have opposite colours.** -/
theorem adjacent_opposite : ∀ a b : Square, adjacent a b → chessColor b = !chessColor a := by
  unfold adjacent
  decide

set_option maxRecDepth 100000 in
theorem mutilated_balance : balance chessColor mutilated = -2 := by decide

/-- **The board with two opposite corners removed has no cover by adjacent pairs**, -/
theorem mutilated_no_cover : ¬ ∃ ts, Global adjacent mutilated ts [] :=
  unbalanced_no_cover adjacent chessColor adjacent_opposite mutilated
    fun zero => nomatch (mutilated_balance.symm.trans zero)

/-- **and no course of placements covering it.** -/
theorem mutilated_no_history : ¬ ∃ ts, Trace (placement adjacent) mutilated ts [] :=
  fun ⟨ts, path⟩ => mutilated_no_cover ⟨ts, trace_global path⟩

/-- Two cells three apart in the first row. -/
def separated : List Square := [⟨0, by decide⟩, ⟨3, by decide⟩]

theorem separated_balanced : balance chessColor separated = 0 := by decide

theorem first_or_fourth {x : Square} (mem : x ∈ separated) :
    x = ⟨0, by decide⟩ ∨ x = ⟨3, by decide⟩ :=
  have mem : List.Mem x [(⟨0, by decide⟩ : Square), ⟨3, by decide⟩] := mem
  match mem with
  | .head _ => .inl rfl
  | .tail _ (.head _) => .inr rfl
  | .tail _ (.tail _ mem) => nomatch mem

theorem separated_apart {a b : Square} (ha : a ∈ separated) (hb : b ∈ separated) :
    ¬ adjacent a b := by
  rcases first_or_fourth ha with ea | ea <;> rcases first_or_fourth hb with eb | eb <;>
    subst ea <;> subst eb <;> unfold adjacent <;> decide

/-- **Balanced and not coverable.** -/
theorem separated_not_coverable : ¬ ∃ ts, Global adjacent separated ts []
  | ⟨[], h⟩ => nomatch Perm.length_eq h.2
  | ⟨(a, b) :: _, h⟩ =>
    have ha : a ∈ separated := Perm.mem h.2 (.head _)
    have hb : b ∈ separated := Perm.mem h.2 (.tail _ (.head _))
    separated_apart ha hb h.1.1

/-- **The balance does not determine coverability.** -/
theorem balance_does_not_determine_coverability :
    balance chessColor separated = balance chessColor ([] : List Square) ∧
      (∃ ts, Global adjacent [] ts []) ∧ ¬ ∃ ts, Global adjacent separated ts [] :=
  ⟨separated_balanced, ⟨[], True.intro, List.Perm.nil⟩, separated_not_coverable⟩

end Coverage

end Becoming
