import Becoming.Context

/-!
# The quantum realization of the Mermin–Peres square (P72q)

P72's `Becoming.Context` states the Mermin–Peres square (Mermin 1990, Peres 1990) as claims
registered in context: nine cells (`Square.Cell`), six lines (`Square.Line`), each line a context
registering its three cells, the parity each line's values must have (`Square.odd`: odd in the
third column only), and `Square.noGlobal`: no single assignment of values to the nine cells has
every line's parity. This module gives the quantum registrations that realize the square. Cell
`(i, j)` holds the observable at row `i`, column `j`:

```
X⊗I   I⊗X   X⊗X
I⊗Z   Z⊗I   Z⊗Z
X⊗Z   Z⊗X   Y⊗Y
```

Every observable here is a real matrix: `X`, `Z` and `I` are, and `Y⊗Y = -(W⊗W)` with
`W = iY = [[0, 1], [-1, 0]]` real (`yy_entries`). So the square is stated with explicit integer
4×4 matrices and checked by evaluation, with nothing beyond Lean's prelude and P72.

* **The operators.** Each observable squares to the identity (`obs_sq`), so it registers one of
  two values, `+1` or `-1`. The three observables of a line commute pairwise (`row_commute`,
  `column_commute`, `line_commute`), so a line is a context that can be registered together,
  while two observables sharing no line anticommute (`off_line_anticommute`), so no larger
  context holds them. Each line multiplies to `-I` where it is odd and to `+I` elsewhere
  (`row_product`, `column_product`, `line_product`).
* **The registrations.** Each observable is a signed permutation matrix (`obs_signed`), acting on
  a vector as `act` (`mulVec_obs`). A vector shows the value `b` at a cell (`true` meaning `-1`)
  where the cell's observable sends it to itself with that sign (`Shows`). Wherever a nonzero
  vector shows values at the three cells of a line, their parity is the line's (`row_parity`,
  `column_parity`, `line_parity`), so what a quantum state shows jointly on a line is a support
  of the line in P72's sense (`shows_support`). Conversely every support of a line is shown
  jointly by an explicit integer vector (`line_realized`, `support_shown`).
* **Quantum registrations are contextual.** No assignment of values to the nine cells is shown
  jointly on every line by quantum states (`no_context_free_values`): it would be a support of
  every line, which `Square.noGlobal` excludes. Within each context the registrations are
  definite and every value the context allows occurs; across contexts they do not come from one
  context-free assignment. This is the Kochen–Specker theorem for two qubits in Mermin and
  Peres's form, with the operator algebra checked rather than cited.

Values are compared entry by entry (`Same`), since equality of functions needs `funext`, which
depends on `Quot.sound`. The integer arithmetic on vectors uses only lemmas proved here by
cases, since most of the prelude's ring lemmas for `Int` depend on `propext`. Every constant has
an empty axiom report.
-/

namespace Becoming
namespace Square

/-! Basis indices are written as constructors, as P72's positions `i0`, `i1`, `i2` are: a numeral
of type `Fin n` goes through `NeZero`, whose instance depends on `propext`. -/

/-- The basis index `|00⟩`. -/
def q₀ : Fin 4 := ⟨0, by decide⟩
/-- The basis index `|01⟩`. -/
def q₁ : Fin 4 := ⟨1, by decide⟩
/-- The basis index `|10⟩`. -/
def q₂ : Fin 4 := ⟨2, by decide⟩
/-- The basis index `|11⟩`. -/
def q₃ : Fin 4 := ⟨3, by decide⟩
/-- A 2×2 integer matrix. -/
def Mat2 : Type := Fin 2 → Fin 2 → Int

/-- A 4×4 integer matrix: a real operator on two qubits, rows and columns indexed by the basis
`|00⟩, |01⟩, |10⟩, |11⟩`. -/
def Mat4 : Type := Fin 4 → Fin 4 → Int

namespace Mat2

/-- The identity. -/
def id : Mat2 := fun i j => if i = j then 1 else 0
/-- Pauli `X`. -/
def x : Mat2 := fun i j => if i = j then 0 else 1
/-- Pauli `Z`. -/
def z : Mat2 := fun i j => if i = j then (if i.val = 0 then 1 else -1) else 0
/-- `W = iY = [[0, 1], [-1, 0]]`, real; Pauli `Y` is `-iW`. -/
def w : Mat2 := fun i j => if i = j then 0 else (if i.val = 0 then 1 else -1)

end Mat2

namespace Mat4

/-- The identity. -/
def one : Mat4 := fun i j => if i = j then 1 else 0

/-- The negative. -/
def neg (A : Mat4) : Mat4 := fun i j => -A i j

/-- The product. -/
def mul (A B : Mat4) : Mat4 := fun i j =>
  A i q₀ * B q₀ j + A i q₁ * B q₁ j + A i q₂ * B q₂ j + A i q₃ * B q₃ j

/-- Two matrices are the same entry by entry. -/
def Same (A B : Mat4) : Prop := ∀ i j, A i j = B i j

instance (A B : Mat4) : Decidable (Same A B) :=
  inferInstanceAs (Decidable (∀ i j : Fin 4, A i j = B i j))

/-- The first qubit of a basis index. -/
def high (i : Fin 4) : Fin 2 := if i.val < 2 then ⟨0, by decide⟩ else ⟨1, by decide⟩
/-- The second qubit of a basis index. -/
def low (i : Fin 4) : Fin 2 := if i.val % 2 = 0 then ⟨0, by decide⟩ else ⟨1, by decide⟩

/-- The tensor product of two 2×2 matrices. -/
def kron (A B : Mat2) : Mat4 := fun i j => A (high i) (high j) * B (low i) (low j)

/-- The product with a vector. -/
def mulVec (A : Mat4) (v : Fin 4 → Int) (i : Fin 4) : Int :=
  A i q₀ * v q₀ + A i q₁ * v q₁ + A i q₂ * v q₂ + A i q₃ * v q₃

end Mat4

open Mat4

/-- `Y⊗Y`, real: `Y⊗Y = (-iW)⊗(-iW) = -(W⊗W)`. -/
def yy : Mat4 := neg (kron Mat2.w Mat2.w)

/-- The observable at each cell of the square, row by row. -/
def obs (c : Cell) : Mat4 :=
  match c.1.val, c.2.val with
  | 0, 0 => kron Mat2.x Mat2.id
  | 0, 1 => kron Mat2.id Mat2.x
  | 0, 2 => kron Mat2.x Mat2.x
  | 1, 0 => kron Mat2.id Mat2.z
  | 1, 1 => kron Mat2.z Mat2.id
  | 1, 2 => kron Mat2.z Mat2.z
  | 2, 0 => kron Mat2.x Mat2.z
  | 2, 1 => kron Mat2.z Mat2.x
  | _, _ => yy

/-- The product of a row, in order. -/
def rowProduct (i : Fin 3) : Mat4 := mul (mul (obs (i, i0)) (obs (i, i1))) (obs (i, i2))

/-- The product of a column, in order. -/
def columnProduct (j : Fin 3) : Mat4 := mul (mul (obs (i0, j)) (obs (i1, j))) (obs (i2, j))

/-! ## The operators -/

/-- `Y⊗Y` as stated: the matrix with `-1` at `|00⟩⟨11|` and `|11⟩⟨00|`, and `+1` at `|01⟩⟨10|`
and `|10⟩⟨01|`. -/
theorem yy_entries : Same yy (fun i j =>
    if i.val + j.val = 3 then (if i.val = 0 ∨ i.val = 3 then -1 else 1) else 0) := by decide

/-- Every observable squares to the identity, so it registers `+1` or `-1`. -/
theorem obs_sq : ∀ i j : Fin 3, Same (mul (obs (i, j)) (obs (i, j))) one := by decide

/-- The observables of a row commute pairwise. -/
theorem row_commute : ∀ i j j' : Fin 3,
    Same (mul (obs (i, j)) (obs (i, j'))) (mul (obs (i, j')) (obs (i, j))) := by decide

/-- The observables of a column commute pairwise. -/
theorem column_commute : ∀ j i i' : Fin 3,
    Same (mul (obs (i, j)) (obs (i', j))) (mul (obs (i', j)) (obs (i, j))) := by decide

/-- Two observables that share no row and no column anticommute: no context larger than a line
holds them. -/
theorem off_line_anticommute : ∀ i j i' j' : Fin 3, i ≠ i' → j ≠ j' →
    Same (mul (obs (i, j)) (obs (i', j'))) (neg (mul (obs (i', j')) (obs (i, j)))) := by decide

/-- Every row multiplies to `+I`. -/
theorem row_product : ∀ i : Fin 3, Same (rowProduct i) one := by decide

/-- The columns multiply to `+I`, `+I` and `-I`. -/
theorem column_product : ∀ j : Fin 3,
    Same (columnProduct j) (if Nat.beq j.val 2 then neg one else one) := by decide

/-! ## The registrations -/

/-- `-x` where `b`, else `x`: the value `-1` where `b` is `true`. -/
def flip (b : Bool) (x : Int) : Int := if b then -x else x

/-- The value a Boolean stands for: `true` is `-1`. -/
def sign (b : Bool) : Int := if b then -1 else 1

/-- The basis index each observable's row `k` reads. -/
def src (c : Cell) (k : Fin 4) : Fin 4 :=
  if obs c k q₀ ≠ 0 then q₀ else if obs c k q₁ ≠ 0 then q₁ else if obs c k q₂ ≠ 0 then q₂ else q₃

/-- Whether row `k` of the observable reads with the sign `-1`. -/
def neg' (c : Cell) (k : Fin 4) : Bool := obs c k (src c k) == -1

/-- Every observable is a signed permutation matrix: row `k` has `sign (neg' c k)` at column
`src c k` and zero elsewhere. -/
theorem obs_signed : ∀ i j : Fin 3, ∀ k m : Fin 4,
    obs (i, j) k m = if src (i, j) k = m then sign (neg' (i, j) k) else 0 := by decide

/-- How an observable acts on a vector, as a signed permutation. -/
def act (c : Cell) (v : Fin 4 → Int) (k : Fin 4) : Int := flip (neg' c k) (v (src c k))

theorem zero_mul' (x : Int) : 0 * x = 0 := by
  cases x with
  | ofNat n => exact congrArg Int.ofNat (Nat.zero_mul n)
  | negSucc n => exact congrArg Int.negOfNat (Nat.zero_mul (n + 1))

theorem zero_add' (x : Int) : 0 + x = x := by
  cases x with
  | ofNat n => exact congrArg Int.ofNat (Nat.zero_add n)
  | negSucc n => rfl

theorem neg_one_mul' (x : Int) : -1 * x = -x := by
  cases x with
  | ofNat n => exact congrArg Int.negOfNat (Nat.one_mul n)
  | negSucc n => exact congrArg Int.ofNat (Nat.one_mul (n + 1))

theorem sign_mul (b : Bool) (x : Int) : sign b * x = flip b x := by
  cases b
  · exact Int.one_mul x
  · exact neg_one_mul' x

/-- A row of a signed permutation matrix applied to a vector. -/
theorem mulVec_signed (A : Mat4) (v : Fin 4 → Int) (k j : Fin 4) (b : Bool)
    (row : ∀ m, A k m = if j = m then sign b else 0) : mulVec A v k = flip b (v j) := by
  unfold mulVec
  rw [row q₀, row q₁, row q₂, row q₃]
  have four : ∀ j : Fin 4, j = q₀ ∨ j = q₁ ∨ j = q₂ ∨ j = q₃ := by decide
  rcases four j with h | h | h | h
  · subst h
    show sign b * v q₀ + 0 * v q₁ + 0 * v q₂ + 0 * v q₃ = _
    repeat rw [zero_mul']
    repeat rw [Int.add_zero]
    repeat rw [zero_add']
    exact sign_mul b _
  · subst h
    show 0 * v q₀ + sign b * v q₁ + 0 * v q₂ + 0 * v q₃ = _
    repeat rw [zero_mul']
    repeat rw [Int.add_zero]
    repeat rw [zero_add']
    exact sign_mul b _
  · subst h
    show 0 * v q₀ + 0 * v q₁ + sign b * v q₂ + 0 * v q₃ = _
    repeat rw [zero_mul']
    repeat rw [Int.add_zero]
    repeat rw [zero_add']
    exact sign_mul b _
  · subst h
    show 0 * v q₀ + 0 * v q₁ + 0 * v q₂ + sign b * v q₃ = _
    repeat rw [zero_mul']
    repeat rw [Int.add_zero]
    repeat rw [zero_add']
    exact sign_mul b _

/-- The observable applied to a vector is its action as a signed permutation. -/
theorem mulVec_obs (i j : Fin 3) (v : Fin 4 → Int) (k : Fin 4) :
    mulVec (obs (i, j)) v k = act (i, j) v k :=
  mulVec_signed _ v k _ _ (obs_signed i j k)

/-- A vector shows the value `b` at a cell (`true` meaning `-1`) where the cell's observable
sends it to itself with that sign: a registration of the cell's observable with value `b`. -/
def Shows (v : Fin 4 → Int) (c : Cell) (b : Bool) : Prop :=
  ∀ k, mulVec (obs c) v k = sign b * v k

instance (v : Fin 4 → Int) (c : Cell) (b : Bool) : Decidable (Shows v c b) :=
  inferInstanceAs (Decidable (∀ k : Fin 4, mulVec (obs c) v k = sign b * v k))

theorem flip_flip (a b : Bool) (x : Int) : flip a (flip b x) = flip (a ^^ b) x := by
  cases a <;> cases b
  · rfl
  · rfl
  · rfl
  · exact Int.neg_neg x

theorem flip_comm (a b : Bool) (x : Int) : flip a (flip b x) = flip b (flip a x) := by
  rw [flip_flip, flip_flip, Bool.xor_comm]

theorem eq_zero_of_neg_eq (x : Int) (h : -x = x) : x = 0 := by
  cases x with
  | ofNat n =>
    cases n with
    | zero => rfl
    | succ n => exact absurd h (fun h' => by cases h')
  | negSucc n => exact absurd h (fun h' => by cases h')

theorem flip_cancel {a b : Bool} {x : Int} (h : flip a x = flip b x) (ne : a ≠ b) : x = 0 := by
  cases a <;> cases b
  · exact absurd rfl ne
  · exact eq_zero_of_neg_eq x h.symm
  · exact eq_zero_of_neg_eq x h
  · exact absurd rfl ne

/-- A vector showing `b` at a cell is acted on by the cell's observable as the flip by `b`. -/
theorem Shows.act {v : Fin 4 → Int} {i j : Fin 3} {b : Bool} (shows : Shows v (i, j) b) (k : Fin 4) :
    act (i, j) v k = flip b (v k) := by
  rw [← mulVec_obs, shows k, sign_mul]

/-- Three signed permutations applied in turn. -/
theorem act_three (c₀ c₁ c₂ : Cell) (v : Fin 4 → Int) (k : Fin 4) :
    act c₀ (act c₁ (act c₂ v)) k =
      flip (neg' c₀ k ^^ neg' c₁ (src c₀ k) ^^ neg' c₂ (src c₁ (src c₀ k)))
        (v (src c₂ (src c₁ (src c₀ k)))) := by
  show flip _ (flip _ (flip _ _)) = _
  rw [flip_flip, flip_flip]

/-- The signed permutation of a row's product is the identity with no sign. -/
theorem row_signed : ∀ i : Fin 3, ∀ k : Fin 4,
    src (i, i2) (src (i, i1) (src (i, i0) k)) = k ∧
    (neg' (i, i0) k ^^ neg' (i, i1) (src (i, i0) k) ^^ neg' (i, i2) (src (i, i1) (src (i, i0) k))) =
      false := by decide

/-- The signed permutation of a column's product is the identity, with the sign `-1` exactly in
the third column. -/
theorem column_signed : ∀ j : Fin 3, ∀ k : Fin 4,
    src (i2, j) (src (i1, j) (src (i0, j) k)) = k ∧
    (neg' (i0, j) k ^^ neg' (i1, j) (src (i0, j) k) ^^ neg' (i2, j) (src (i1, j) (src (i0, j) k))) =
      (Nat.beq j.val 2) := by decide

/-- Acting by an observable on a vector that is a flip of another flips the action. -/
theorem act_congr (c : Cell) {u v : Fin 4 → Int} {b : Bool} (h : ∀ m, u m = flip b (v m))
    (k : Fin 4) : act c u k = flip b (act c v k) := by
  show flip (neg' c k) (u (src c k)) = flip b (flip (neg' c k) (v (src c k)))
  rw [h, flip_comm]

/-- Registered jointly at three cells, the three observables applied in turn flip by the
parity of the values shown. -/
theorem shows_three {v : Fin 4 → Int} {c₀ c₁ c₂ : Cell} {b₀ b₁ b₂ : Bool}
    (s₀ : ∀ k, act c₀ v k = flip b₀ (v k)) (s₁ : ∀ k, act c₁ v k = flip b₁ (v k))
    (s₂ : ∀ k, act c₂ v k = flip b₂ (v k)) (k : Fin 4) :
    act c₀ (act c₁ (act c₂ v)) k = flip (b₀ ^^ (b₁ ^^ b₂)) (v k) := by
  have two : ∀ m, act c₁ (act c₂ v) m = flip (b₂ ^^ b₁) (v m) := fun m => by
    rw [act_congr c₁ s₂ m, s₁ m, flip_flip]
  rw [act_congr c₀ two k, s₀ k, flip_flip]
  cases b₀ <;> cases b₁ <;> cases b₂ <;> rfl

/-- **Quantum registrations keep each row's parity.** Wherever a nonzero vector shows values at
the three cells of a row, their parity is even, as the row's product `+I` gives. -/
theorem row_parity {v : Fin 4 → Int} {i : Fin 3} {b₀ b₁ b₂ : Bool} (nonzero : ¬ ∀ k, v k = 0)
    (s₀ : Shows v (i, i0) b₀) (s₁ : Shows v (i, i1) b₁) (s₂ : Shows v (i, i2) b₂) :
    (b₀ ^^ (b₁ ^^ b₂)) = false := by
  have e : ∀ k, flip (b₀ ^^ (b₁ ^^ b₂)) (v k) = flip false (v k) := fun k => by
    have h := act_three (i, i0) (i, i1) (i, i2) v k
    rw [(row_signed i k).1, (row_signed i k).2] at h
    exact (shows_three s₀.act s₁.act s₂.act k).symm.trans h
  cases hp : (b₀ ^^ (b₁ ^^ b₂))
  · rfl
  · exact absurd (fun k => flip_cancel (hp ▸ e k) Bool.noConfusion) nonzero

/-- **Quantum registrations keep each column's parity.** Wherever a nonzero vector shows values
at the three cells of a column, their parity is even in the first two columns and odd in the
third, as the column's product `+I` or `-I` gives. -/
theorem column_parity {v : Fin 4 → Int} {j : Fin 3} {b₀ b₁ b₂ : Bool} (nonzero : ¬ ∀ k, v k = 0)
    (s₀ : Shows v (i0, j) b₀) (s₁ : Shows v (i1, j) b₁) (s₂ : Shows v (i2, j) b₂) :
    (b₀ ^^ (b₁ ^^ b₂)) = (Nat.beq j.val 2) := by
  have e : ∀ k, flip (b₀ ^^ (b₁ ^^ b₂)) (v k) = flip (Nat.beq j.val 2) (v k) := fun k => by
    have h := act_three (i0, j) (i1, j) (i2, j) v k
    rw [(column_signed j k).1, (column_signed j k).2] at h
    exact (shows_three s₀.act s₁.act s₂.act k).symm.trans h
  cases hp : (b₀ ^^ (b₁ ^^ b₂)) <;> cases hj : (Nat.beq j.val 2)
  · rfl
  · exact absurd (fun k => flip_cancel (hj ▸ hp ▸ e k) Bool.noConfusion) nonzero
  · exact absurd (fun k => flip_cancel (hj ▸ hp ▸ e k) Bool.noConfusion) nonzero
  · rfl

/-- A row's joint registration with the values `b₀`, `b₁` at its first two cells and the value
the line's parity gives at the third: an integer vector, explicit. -/
def rowWitness (n : Fin 3) (b₀ b₁ : Bool) : Fin 4 → Int :=
  match n.val, b₀, b₁ with
  | 0, false, false => fun k => match k.val with | 0 => 1 | 1 => 1 | 2 => 1 | _ => 1
  | 0, false, true => fun k => match k.val with | 0 => 1 | 1 => -1 | 2 => 1 | _ => -1
  | 0, true, false => fun k => match k.val with | 0 => 1 | 1 => 1 | 2 => -1 | _ => -1
  | 0, true, true => fun k => match k.val with | 0 => 1 | 1 => -1 | 2 => -1 | _ => 1
  | 1, false, false => fun k => match k.val with | 0 => 1 | 1 => 0 | 2 => 0 | _ => 0
  | 1, false, true => fun k => match k.val with | 0 => 0 | 1 => 0 | 2 => 1 | _ => 0
  | 1, true, false => fun k => match k.val with | 0 => 0 | 1 => 1 | 2 => 0 | _ => 0
  | 1, true, true => fun k => match k.val with | 0 => 0 | 1 => 0 | 2 => 0 | _ => 1
  | 2, false, false => fun k => match k.val with | 0 => 1 | 1 => 1 | 2 => 1 | _ => -1
  | 2, false, true => fun k => match k.val with | 0 => 1 | 1 => -1 | 2 => 1 | _ => 1
  | 2, true, false => fun k => match k.val with | 0 => 1 | 1 => 1 | 2 => -1 | _ => 1
  | 2, true, true => fun k => match k.val with | 0 => 1 | 1 => -1 | 2 => -1 | _ => -1
  | _, _, _ => fun _ => 0

/-- A column's joint registration with the values `b₀`, `b₁` at its first two cells and the value
the line's parity gives at the third: an integer vector, explicit. -/
def columnWitness (n : Fin 3) (b₀ b₁ : Bool) : Fin 4 → Int :=
  match n.val, b₀, b₁ with
  | 0, false, false => fun k => match k.val with | 0 => 1 | 1 => 0 | 2 => 1 | _ => 0
  | 0, false, true => fun k => match k.val with | 0 => 0 | 1 => 1 | 2 => 0 | _ => 1
  | 0, true, false => fun k => match k.val with | 0 => 1 | 1 => 0 | 2 => -1 | _ => 0
  | 0, true, true => fun k => match k.val with | 0 => 0 | 1 => 1 | 2 => 0 | _ => -1
  | 1, false, false => fun k => match k.val with | 0 => 1 | 1 => 1 | 2 => 0 | _ => 0
  | 1, false, true => fun k => match k.val with | 0 => 0 | 1 => 0 | 2 => 1 | _ => 1
  | 1, true, false => fun k => match k.val with | 0 => 1 | 1 => -1 | 2 => 0 | _ => 0
  | 1, true, true => fun k => match k.val with | 0 => 0 | 1 => 0 | 2 => 1 | _ => -1
  | 2, false, false => fun k => match k.val with | 0 => 1 | 1 => 0 | 2 => 0 | _ => 1
  | 2, false, true => fun k => match k.val with | 0 => 0 | 1 => 1 | 2 => 1 | _ => 0
  | 2, true, false => fun k => match k.val with | 0 => 1 | 1 => 0 | 2 => 0 | _ => -1
  | 2, true, true => fun k => match k.val with | 0 => 0 | 1 => 1 | 2 => -1 | _ => 0
  | _, _, _ => fun _ => 0

/-- **Every showing of a row's parity is realized.** For every row and every values `b₀`, `b₁`,
some nonzero integer vector shows `b₀`, `b₁` and `b₀ xor b₁` at its three cells. -/
theorem row_realized : ∀ i : Fin 3, ∀ b₀ b₁ : Bool,
    (¬ ∀ k, rowWitness i b₀ b₁ k = 0) ∧ Shows (rowWitness i b₀ b₁) (i, i0) b₀ ∧
      Shows (rowWitness i b₀ b₁) (i, i1) b₁ ∧ Shows (rowWitness i b₀ b₁) (i, i2) (parity b₀ b₁ false) := by
  decide

/-- **Every showing of a column's parity is realized.** For every column and every values `b₀`,
`b₁`, some nonzero integer vector shows `b₀`, `b₁` at the first two cells and, at the third, the
value that makes the column's parity odd exactly in the third column. -/
theorem column_realized : ∀ j : Fin 3, ∀ b₀ b₁ : Bool,
    (¬ ∀ k, columnWitness j b₀ b₁ k = 0) ∧ Shows (columnWitness j b₀ b₁) (i0, j) b₀ ∧
      Shows (columnWitness j b₀ b₁) (i1, j) b₁ ∧
      Shows (columnWitness j b₀ b₁) (i2, j) (parity b₀ b₁ (Nat.beq j.val 2)) := by
  decide

/-! ## Lines: the registrations are the supports, and no context-free assignment fits -/

/-- The product of a line's observables, in order along the line. -/
def lineProduct (l : Line) : Mat4 := mul (mul (obs (at_ l i0)) (obs (at_ l i1))) (obs (at_ l i2))

/-- **Each line multiplies to `-I` where it is odd and to `+I` elsewhere.** -/
theorem line_product : ∀ l : Line, Same (lineProduct l) (if odd l then neg one else one)
  | .row i => row_product i
  | .column j => column_product j

/-- The observables of a line commute pairwise: a line is a context. -/
theorem line_commute : ∀ (l : Line) (q q' : Fin 3),
    Same (mul (obs (at_ l q)) (obs (at_ l q'))) (mul (obs (at_ l q')) (obs (at_ l q)))
  | .row i, q, q' => row_commute i q q'
  | .column j, q, q' => column_commute j q q'

/-- **Quantum registrations keep each line's parity.** Wherever a nonzero vector shows values
at the three cells of a line, their parity is the line's. -/
theorem line_parity {v : Fin 4 → Int} {l : Line} {b₀ b₁ b₂ : Bool} (nonzero : ¬ ∀ k, v k = 0)
    (s₀ : Shows v (at_ l i0) b₀) (s₁ : Shows v (at_ l i1) b₁) (s₂ : Shows v (at_ l i2) b₂) :
    parity b₀ b₁ b₂ = odd l := by
  cases l with
  | row i => exact row_parity nonzero s₀ s₁ s₂
  | column j => exact column_parity nonzero s₀ s₁ s₂

/-- **What a quantum state shows jointly on a line is a support of the line**, in P72's sense. -/
theorem shows_support {v : Fin 4 → Int} {l : Line} {f : Cell → Bool} (nonzero : ¬ ∀ k, v k = 0)
    (shows : ∀ q, Shows v (at_ l q) (f (at_ l q))) : support l f :=
  line_parity nonzero (shows i0) (shows i1) (shows i2)

/-- A line's joint registration with the values `b₀`, `b₁` at its first two cells. -/
def lineWitness : Line → Bool → Bool → Fin 4 → Int
  | .row i => rowWitness i
  | .column j => columnWitness j

/-- Every showing of a line's parity is realized, by an explicit integer vector. -/
theorem line_realized : ∀ (l : Line) (b₀ b₁ : Bool),
    (¬ ∀ k, lineWitness l b₀ b₁ k = 0) ∧ Shows (lineWitness l b₀ b₁) (at_ l i0) b₀ ∧
      Shows (lineWitness l b₀ b₁) (at_ l i1) b₁ ∧
      Shows (lineWitness l b₀ b₁) (at_ l i2) (parity b₀ b₁ (odd l))
  | .row i, b₀, b₁ => row_realized i b₀ b₁
  | .column j, b₀, b₁ => column_realized j b₀ b₁

theorem parity_third : ∀ a b c d : Bool, parity a b c = d → c = parity a b d := by decide

theorem three : ∀ q : Fin 3, q = i0 ∨ q = i1 ∨ q = i2 := by decide

/-- **Every support of a line is shown jointly by some quantum state.** -/
theorem support_shown {l : Line} {f : Cell → Bool} (h : support l f) :
    ∃ v : Fin 4 → Int, (¬ ∀ k, v k = 0) ∧ ∀ q, Shows v (at_ l q) (f (at_ l q)) := by
  obtain ⟨nonzero, s₀, s₁, s₂⟩ := line_realized l (f (at_ l i0)) (f (at_ l i1))
  refine ⟨_, nonzero, fun q => ?_⟩
  rcases three q with e | e | e
  · subst e; exact s₀
  · subst e; exact s₁
  · subst e
    rw [parity_third _ _ _ _ h]
    exact s₂

/-- **Quantum registrations are contextual.** On every line, the values quantum states show
jointly are exactly the line's supports (`shows_support`, `support_shown`); so no single
assignment of values to the nine cells is shown jointly on every line, since it would be a
support of every line, which P72's `noGlobal` excludes. -/
theorem no_context_free_values :
    ¬ ∃ f : Cell → Bool, ∀ l : Line,
      ∃ v : Fin 4 → Int, (¬ ∀ k, v k = 0) ∧ ∀ q, Shows v (at_ l q) (f (at_ l q)) :=
  fun ⟨f, hf⟩ => noGlobal ⟨f, fun l =>
    let ⟨_, nonzero, shows⟩ := hf l
    shows_support nonzero shows⟩

end Square
end Becoming

