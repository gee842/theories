import ExplanatoryNecessity

/-! A matched structural rival: finite tilings, global coverage and local removal.
The target fixes the board, allowed tiles and exact coverage independently of
any claim about explanatory priority. List order is representational. -/
namespace Generative.ExplanatoryStructure
universe u
variable {C : Type u}

def cells : List (C × C) → List C
  | [] => []
  | (a, b) :: ts => a :: b :: cells ts

def Legal (tile : C → C → Prop) : List (C × C) → Prop
  | [] => True
  | (a, b) :: ts => tile a b ∧ Legal tile ts

def placement (tile : C → C → Prop) : Process (List C) (C × C) where
  step board ab rest := tile ab.1 ab.2 ∧ board.Perm (ab.1 :: ab.2 :: rest)

/-- The final list order is immaterial to the mathematical coverage question. -/
def Realizes (tile : C → C → Prop) (board : List C) (ts : List (C × C))
    (rest : List C) : Prop :=
  ∃ last, Trace (placement tile) board ts last ∧ last.Perm rest

def Global (tile : C → C → Prop) (board : List C) (ts : List (C × C))
    (rest : List C) : Prop := Legal tile ts ∧ board.Perm (cells ts ++ rest)

theorem trace_global {tile : C → C → Prop} {board last : List C} {ts : List (C × C)}
    (h : Trace (placement tile) board ts last) : Global tile board ts last := by
  induction h with
  | nil s => exact ⟨True.intro, List.Perm.refl s⟩
  | @cons s m t ab ts hs ht ih =>
    cases ab with
    | mk a b =>
      exact ⟨⟨hs.1, ih.1⟩, hs.2.trans (.cons a (.cons b ih.2))⟩

theorem global_realized {tile : C → C → Prop} {board rest : List C} {ts : List (C × C)}
    (h : Global tile board ts rest) : Realizes tile board ts rest := by
  induction ts generalizing board with
  | nil => exact ⟨board, .nil _, h.2⟩
  | cons ab ts ih =>
    cases ab with
    | mk a b =>
      have tail : Global tile (cells ts ++ rest) ts rest := ⟨h.1.2, List.Perm.refl _⟩
      obtain ⟨last, ht, hp⟩ := ih tail
      exact ⟨last, .cons ⟨h.1.1, h.2⟩ ht, hp⟩

theorem realizes_iff_global (tile : C → C → Prop) (board : List C)
    (ts : List (C × C)) (rest : List C) :
    Realizes tile board ts rest ↔ Global tile board ts rest := by
  constructor
  · rintro ⟨last, ht, hp⟩
    have hg := trace_global ht
    exact ⟨hg.1, hg.2.trans (List.Perm.append_left (cells ts) hp)⟩
  · exact global_realized

theorem complete_trace_iff (tile : C → C → Prop) (board : List C) (ts : List (C × C)) :
    Trace (placement tile) board ts [] ↔ Global tile board ts [] := by
  constructor
  · exact trace_global
  · intro h
    obtain ⟨last, ht, hp⟩ := global_realized h
    have he := hp.eq_nil
    subst last
    exact ht

/-- Structural balance is defined without an event order or a construction history. -/
def charge (color : C → Bool) (c : C) : Int := if color c then 1 else -1

def balance (color : C → Bool) : List C → Int
  | [] => 0
  | c :: rest => charge color c + balance color rest

theorem balance_perm (color : C → Bool) {xs ys : List C} (h : xs.Perm ys) :
    balance color xs = balance color ys := by
  induction h with
  | nil => rfl
  | cons a hp ih => exact congrArg (fun z => charge color a + z) ih
  | swap a b xs =>
    change charge color b + (charge color a + balance color xs) = _
    rw [← Int.add_assoc, Int.add_comm (charge color b) (charge color a), Int.add_assoc]
    rfl
  | trans hp hq ihp ihq => exact ihp.trans ihq

theorem opposite_pair_balance (color : C → Bool) (a b : C) (rest : List C)
    (h : color b = !color a) : balance color (a :: b :: rest) = balance color rest := by
  change charge color a + (charge color b + balance color rest) = _
  unfold charge
  rw [h]
  cases color a with
  | false => exact (Int.add_assoc (-1) 1 _).symm.trans (Int.zero_add _)
  | true => exact (Int.add_assoc 1 (-1) _).symm.trans (Int.zero_add _)

theorem legal_balance (tile : C → C → Prop) (color : C → Bool)
    (opposite : ∀ a b, tile a b → color b = !color a)
    {ts : List (C × C)} (h : Legal tile ts) (rest : List C) :
    balance color (cells ts ++ rest) = balance color rest := by
  induction ts with
  | nil => rfl
  | cons ab ts ih =>
    cases ab with
    | mk a b =>
      exact (opposite_pair_balance color a b (cells ts ++ rest) (opposite a b h.1)).trans (ih h.2)

theorem global_balance (tile : C → C → Prop) (color : C → Bool)
    (opposite : ∀ a b, tile a b → color b = !color a)
    {board rest : List C} {ts : List (C × C)} (h : Global tile board ts rest) :
    balance color board = balance color rest :=
  (balance_perm color h.2).trans (legal_balance tile color opposite h.1 rest)

theorem unbalanced_no_cover (tile : C → C → Prop) (color : C → Bool)
    (opposite : ∀ a b, tile a b → color b = !color a)
    (board : List C) (h : balance color board ≠ 0) :
    ¬ ∃ ts, Global tile board ts [] := by
  rintro ⟨ts, ht⟩
  exact h (global_balance tile color opposite ht)

theorem unbalanced_no_placement_history (tile : C → C → Prop) (color : C → Bool)
    (opposite : ∀ a b, tile a b → color b = !color a)
    (board : List C) (h : balance color board ≠ 0) :
    ¬ ∃ ts, Trace (placement tile) board ts [] := by
  rintro ⟨ts, ht⟩
  exact unbalanced_no_cover tile color opposite board h ⟨ts, trace_global ht⟩

/-- A fixed 8×8 board with opposite corner squares removed. No geometrical
condition is defined by the desired color invariant. -/
abbrev Square := Fin 64

def chessColor (c : Square) : Bool := (c.val / 8 + c.val % 8) % 2 == 0

def adjacent (a b : Square) : Prop :=
  (a.val / 8 = b.val / 8 ∧ (a.val + 1 = b.val ∨ b.val + 1 = a.val)) ∨
  (a.val + 8 = b.val ∨ b.val + 8 = a.val)

def mutilated : List Square := (List.finRange 64).filter (fun c => c.val != 0 && c.val != 63)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 2000000 in
theorem adjacent_opposite : ∀ a b : Square, adjacent a b → chessColor b = !chessColor a := by
  unfold adjacent
  decide

set_option maxRecDepth 100000 in
theorem mutilated_balance : balance chessColor mutilated = -2 := by decide

theorem mutilated_no_cover : ¬ ∃ ts, Global adjacent mutilated ts [] := by
  apply unbalanced_no_cover adjacent chessColor adjacent_opposite mutilated
  rw [mutilated_balance]
  intro h
  cases h

theorem mutilated_no_history : ¬ ∃ ts, Trace (placement adjacent) mutilated ts [] := by
  rintro ⟨ts, ht⟩
  exact mutilated_no_cover ⟨ts, trace_global ht⟩

/-- Balance is necessary but not sufficient once geometrical adjacency matters. -/
def separated : List Square := [⟨0, by decide⟩, ⟨3, by decide⟩]

theorem separated_balanced : balance chessColor separated = 0 := by decide

theorem separated_not_coverable : ¬ ∃ ts, Global adjacent separated ts [] := by
  rintro ⟨ts, h⟩
  have len := h.2.length_eq
  cases ts with
  | nil => cases len
  | cons ab rest =>
    cases ab with
    | mk a b =>
      have ha : a ∈ separated := h.2.mem_iff.mpr (by exact .head _)
      have hb : b ∈ separated := h.2.mem_iff.mpr (by exact .tail _ (.head _))
      have hadj := h.1.1
      have bad : ∀ a b : Square, a ∈ separated → b ∈ separated → ¬ adjacent a b := by
        unfold adjacent separated
        decide
      exact bad a b ha hb hadj


/-- The same finite tiling allows more than one placement order. -/
theorem two_tile_orders (tile : C → C → Prop) (a b c d : C)
    (hab : tile a b) (hcd : tile c d) :
    Trace (placement tile) [a, b, c, d] [(a, b), (c, d)] [] ∧
    Trace (placement tile) [a, b, c, d] [(c, d), (a, b)] [] := by
  constructor
  · exact .cons ⟨hab, List.Perm.refl _⟩ (.cons ⟨hcd, List.Perm.refl _⟩ (.nil _))
  · have hp : [a, b, c, d].Perm [c, d, a, b] :=
      List.perm_append_comm (l₁ := [a, b]) (l₂ := [c, d])
    exact .cons ⟨hcd, hp⟩ (.cons ⟨hab, List.Perm.refl _⟩ (.nil _))

end Generative.ExplanatoryStructure

#print axioms Generative.ExplanatoryStructure.trace_global
#print axioms Generative.ExplanatoryStructure.global_realized
#print axioms Generative.ExplanatoryStructure.realizes_iff_global
#print axioms Generative.ExplanatoryStructure.complete_trace_iff
#print axioms Generative.ExplanatoryStructure.balance_perm
#print axioms Generative.ExplanatoryStructure.opposite_pair_balance
#print axioms Generative.ExplanatoryStructure.legal_balance
#print axioms Generative.ExplanatoryStructure.global_balance
#print axioms Generative.ExplanatoryStructure.unbalanced_no_cover
#print axioms Generative.ExplanatoryStructure.unbalanced_no_placement_history
#print axioms Generative.ExplanatoryStructure.adjacent_opposite
#print axioms Generative.ExplanatoryStructure.mutilated_balance
#print axioms Generative.ExplanatoryStructure.mutilated_no_cover
#print axioms Generative.ExplanatoryStructure.mutilated_no_history
#print axioms Generative.ExplanatoryStructure.separated_balanced
#print axioms Generative.ExplanatoryStructure.separated_not_coverable

#print axioms Generative.ExplanatoryStructure.two_tile_orders
