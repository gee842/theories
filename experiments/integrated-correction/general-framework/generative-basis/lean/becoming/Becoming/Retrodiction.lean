import Becoming.Prelude

/-!
# Retrodiction: reading an earlier relation from later dated records

A source relation changes over dates; a history gives the relation at each date. Dated controls
record, at a date, a probe and the report the relation gave. A history fits the records where
it gives each record's report at its date. An earlier packet was produced at a date by the
relation then holding and a hidden source; reading it means naming the source's content. This
module states, for every type of histories, dates, relations, probes, reports, packets and
contents, when the records read the earlier packet right.

* **The actual history is always a candidate** (`actual_candidate`); a history fits the
  records another gave exactly when it gives the same records (`fits_iff_same`).
* **Reading an earlier packet right.** For the actual history and source: every explanation of
  the packet by a family history fitting the records and an admitted source gives the actual
  content exactly when every family history that, with some admitted source, gives the same
  packet with another content is told apart from the actual history by some dated control
  (`reading_right_iff`). The condition is local: one control per rival. The same holds of
  any reading of the relation at a date (`look_right_iff`). Where the actual history is in the
  family, a reading on which all explanations agree is the actual one (`agreed_reading_actual`);
  outside the family the agreement can be wrong (an instance in the periphery).
* **Change envelopes.** Over dates `0, 1, 2, …`, a course that returns at `a + n` to its value
  at `a` through a date where it was elsewhere has changed at least twice (`bracket`). So, where
  the relation takes two values, controls at both ends settle every date between exactly when
  at most one change is admitted or no date lies strictly between (`bracket_settles_iff`); the
  excursion that leaves for one date and returns is the counterexample (`excursion_changes`).
  Where the ends differ, every date strictly between may hold either value under one change
  (`change_unlocated`).

No premise is added; the module imports only the core and every declaration has an empty axiom
report.
-/

namespace Becoming.Retrodiction

universe u v w x y z p q

/-! ## Records and candidates -/

/-- A dated control: at a date, a probe and the report it gave. -/
structure Record (D : Type v) (Q : Type x) (O : Type y) where
  date : D
  probe : Q
  report : O

section Records

variable {H : Type u} {D : Type v} {R : Type w} {Q : Type x} {O : Type y}
variable (routeAt : H → D → R) (emit : R → Q → O)

/-- The history `h` gives each record's report at its date. -/
def Fits (h : H) : List (Record D Q O) → Prop
  | [] => True
  | r :: rs => emit (routeAt h r.date) r.probe = r.report ∧ Fits h rs

/-- The records the history `h` gives for the dated probes. -/
def acquire (h : H) : List (D × Q) → List (Record D Q O)
  | [] => []
  | p :: ps => ⟨p.1, p.2, emit (routeAt h p.1) p.2⟩ :: acquire h ps

/-- Some dated probe tells `g` and `h` apart. -/
def Separated (g h : H) : List (D × Q) → Prop
  | [] => False
  | p :: ps => emit (routeAt g p.1) p.2 ≠ emit (routeAt h p.1) p.2 ∨ Separated g h ps

/-- **The actual history is always a candidate.** -/
theorem actual_candidate (h : H) : ∀ ps : List (D × Q), Fits routeAt emit h (acquire routeAt emit h ps)
  | [] => trivial
  | _ :: ps => ⟨rfl, actual_candidate h ps⟩

/-- **A history fits the records another gave exactly when it gives the same records.** -/
theorem fits_iff_same (g h : H) : ∀ ps : List (D × Q),
    Fits routeAt emit g (acquire routeAt emit h ps) ↔ acquire routeAt emit g ps = acquire routeAt emit h ps
  | [] => ⟨fun _ => rfl, fun _ => trivial⟩
  | p :: ps =>
    ⟨fun ⟨e, rest⟩ =>
      (congrArg (fun o => (⟨p.1, p.2, o⟩ : Record D Q O) :: acquire routeAt emit g ps) e).trans
        (congrArg (List.cons (⟨p.1, p.2, emit (routeAt h p.1) p.2⟩ : Record D Q O))
          ((fits_iff_same g h ps).mp rest)),
     fun same =>
      ⟨congrArg Record.report (List.cons.inj same).1, (fits_iff_same g h ps).mpr (List.cons.inj same).2⟩⟩

/-- A separated history does not fit. -/
theorem not_fits_of_separated {g h : H} : ∀ {ps : List (D × Q)},
    Separated routeAt emit g h ps → ¬ Fits routeAt emit g (acquire routeAt emit h ps)
  | [], s, _ => s
  | _ :: _, .inl ne, ⟨e, _⟩ => ne e
  | _ :: _, .inr s, ⟨_, rest⟩ => not_fits_of_separated s rest

/-- With reports compared, a history either fits or is separated. -/
theorem fits_or_separated [DecidableEq O] (g h : H) : ∀ ps : List (D × Q),
    Fits routeAt emit g (acquire routeAt emit h ps) ∨ Separated routeAt emit g h ps
  | [] => .inl trivial
  | p :: ps =>
    match decEq (emit (routeAt g p.1) p.2) (emit (routeAt h p.1) p.2), fits_or_separated g h ps with
    | isTrue e, .inl rest => .inl ⟨e, rest⟩
    | isTrue _, .inr s => .inr (.inr s)
    | isFalse ne, _ => .inr (.inl ne)

end Records

/-! ## Reading an earlier packet -/

section Reading

variable {H : Type u} {D : Type v} {R : Type w} {Q : Type x} {O : Type y}
variable (routeAt : H → D → R) (emit : R → Q → O)

/-- **Reading an earlier packet right.** The packet at date `d` was produced by the actual
relation `routeAt h d` and the hidden source `s`. Every explanation of it by a family history
fitting the records and an admitted source gives the actual content exactly when every family
history that, with some admitted source, gives the same packet with another content is told
apart from `h` by some dated control. -/
theorem reading_right_iff {X : Type z} {P : Type p} {V : Type q} [DecidableEq O] [DecidableEq V]
    (packet : R → X → P) (content : X → V) (F : H → Prop) (Admitted : X → Prop)
    (d : D) (h : H) (s : X) (ps : List (D × Q)) :
    (∀ g t, F g → Fits routeAt emit g (acquire routeAt emit h ps) → Admitted t →
        packet (routeAt g d) t = packet (routeAt h d) s → content t = content s) ↔
      (∀ g t, F g → Admitted t → packet (routeAt g d) t = packet (routeAt h d) s →
        content t ≠ content s → Separated routeAt emit g h ps) :=
  ⟨fun right g t inF admitted same differs =>
    match fits_or_separated routeAt emit g h ps with
    | .inl fits => absurd (right g t inF fits admitted same) differs
    | .inr separated => separated,
   fun separate g t inF fits admitted same =>
    match decEq (content t) (content s) with
    | isTrue e => e
    | isFalse differs =>
      absurd fits (not_fits_of_separated routeAt emit (separate g t inF admitted same differs))⟩

/-- **An agreed reading is the actual one** where the actual history is in the family and its
source admitted. -/
theorem agreed_reading_actual {X : Type z} {P : Type p} {V : Type q} (packet : R → X → P) (content : X → V)
    (F : H → Prop) (Admitted : X → Prop) (d : D) (h : H) (s : X) (ps : List (D × Q)) (v : V)
    (inF : F h) (admitted : Admitted s)
    (agree : ∀ g t, F g → Fits routeAt emit g (acquire routeAt emit h ps) → Admitted t →
      packet (routeAt g d) t = packet (routeAt h d) s → content t = v) :
    content s = v :=
  agree h s inF (actual_candidate routeAt emit h ps) admitted rfl

/-- **Reading the relation at a date right.** Every family history fitting the records agrees
with `h` on what `look` reads of the relation at `d` exactly when every family history that
disagrees there is told apart from `h` by some dated control. -/
theorem look_right_iff {V : Type q} [DecidableEq O] [DecidableEq V] (look : R → V) (F : H → Prop)
    (d : D) (h : H) (ps : List (D × Q)) :
    (∀ g, F g → Fits routeAt emit g (acquire routeAt emit h ps) → look (routeAt g d) = look (routeAt h d)) ↔
      (∀ g, F g → look (routeAt g d) ≠ look (routeAt h d) → Separated routeAt emit g h ps) :=
  ⟨fun right g inF differs =>
    match fits_or_separated routeAt emit g h ps with
    | .inl fits => absurd (right g inF fits) differs
    | .inr separated => separated,
   fun separate g inF fits =>
    match decEq (look (routeAt g d)) (look (routeAt h d)) with
    | isTrue e => e
    | isFalse differs => absurd fits (not_fits_of_separated routeAt emit (separate g inF differs))⟩

end Reading

/-! ## Change envelopes -/

section Changes

variable {R : Type w} [DecidableEq R]

/-- Changes of the course `c` over the `n` steps from date `a`. -/
def changes (c : Nat → R) (a : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => changes c a n + (if c (a + n) = c (a + n + 1) then 0 else 1)

theorem changes_split (c : Nat → R) (a j : Nat) :
    ∀ k, changes c a (j + k) = changes c a j + changes c (a + j) k
  | 0 => rfl
  | k + 1 => by
    show changes c a (j + k) + (if c (a + (j + k)) = c (a + (j + k) + 1) then 0 else 1) =
      changes c a j + (changes c (a + j) k + (if c (a + j + k) = c (a + j + k + 1) then 0 else 1))
    rw [changes_split c a j k, Nat.add_assoc (changes c a j), Nat.add_assoc a j k]

theorem changes_le (c : Nat → R) (a : Nat) : ∀ n, changes c a n ≤ n
  | 0 => Nat.le_refl 0
  | n + 1 => by
    show changes c a n + (if c (a + n) = c (a + n + 1) then 0 else 1) ≤ n + 1
    match decEq (c (a + n)) (c (a + n + 1)) with
    | isTrue e =>
      rw [if_pos e]
      exact Nat.le_succ_of_le (changes_le c a n)
    | isFalse ne =>
      rw [if_neg ne]
      exact Nat.succ_le_succ (changes_le c a n)

/-- A course that is elsewhere after `n` steps has changed at least once. -/
theorem moved_changes (c : Nat → R) (a : Nat) : ∀ n, c (a + n) ≠ c a → 1 ≤ changes c a n
  | 0, moved => absurd rfl moved
  | n + 1, moved => by
    show 1 ≤ changes c a n + (if c (a + n) = c (a + n + 1) then 0 else 1)
    match decEq (c (a + n)) (c (a + n + 1)) with
    | isTrue same =>
      rw [if_pos same]
      exact moved_changes c a n fun e => moved (same.symm.trans e)
    | isFalse ne =>
      rw [if_neg ne]
      exact Nat.le_add_left 1 _

/-- A course constant over the steps has not changed. -/
theorem changes_const (c : Nat → R) (a : Nat) (v : R) :
    ∀ n, (∀ i, i ≤ n → c (a + i) = v) → changes c a n = 0
  | 0, _ => rfl
  | n + 1, const => by
    show changes c a n + (if c (a + n) = c (a + n + 1) then 0 else 1) = 0
    have e1 : c (a + n + 1) = v := const (n + 1) (Nat.le_refl _)
    rw [if_pos ((const n (Nat.le_succ n)).trans e1.symm),
      changes_const c a v n fun i le => const i (Nat.le_succ_of_le le)]

/-- **A return brackets every date between.** A course back at `a + (j + k)` to its value at
`a`, elsewhere at `a + j`, has changed at least twice. -/
theorem bracket (c : Nat → R) (a j k : Nat) (back : c (a + (j + k)) = c a)
    (away : c (a + j) ≠ c a) : 2 ≤ changes c a (j + k) := by
  rw [changes_split]
  have first := moved_changes c a j away
  have second := moved_changes c (a + j) k fun e =>
    away ((back.symm.trans ((congrArg c (Nat.add_assoc a j k)).symm.trans e)).symm)
  exact Nat.add_le_add first second

/-- The course at `r` except one date `a + 1` at `r'`. -/
def excursion (r r' : R) (a : Nat) (i : Nat) : R := if i = a + 1 then r' else r

theorem excursion_changes {r r' : R} (two : r ≠ r') (a : Nat) :
    ∀ m, changes (excursion r r' a) a (m + 2) = 2
  | 0 => by
    have n0 : a ≠ a + 1 := Nat.ne_of_lt (Nat.lt_succ_self a)
    have n2 : a + 1 + 1 ≠ a + 1 := Nat.ne_of_gt (Nat.lt_succ_self (a + 1))
    show (0 + (if excursion r r' a (a + 0) = excursion r r' a (a + 0 + 1) then 0 else 1)) +
      (if excursion r r' a (a + 1) = excursion r r' a (a + 1 + 1) then 0 else 1) = 2
    have e0 : excursion r r' a (a + 0) = r := if_neg n0
    have e1 : excursion r r' a (a + 0 + 1) = r' := if_pos rfl
    have e2 : excursion r r' a (a + 1 + 1) = r := if_neg n2
    rw [e0, e1, e2, if_neg two, if_neg (fun h => two h.symm)]
  | m + 1 => by
    have lt1 : a + 1 < a + (m + 2) :=
      Nat.add_lt_add_left (Nat.succ_lt_succ (Nat.zero_lt_succ m)) a
    have lt2 : a + 1 < a + (m + 2) + 1 := Nat.lt_succ_of_lt lt1
    show changes (excursion r r' a) a (m + 2) +
      (if excursion r r' a (a + (m + 2)) = excursion r r' a (a + (m + 2) + 1) then 0 else 1) = 2
    rw [show excursion r r' a (a + (m + 2)) = r from if_neg (Nat.ne_of_gt lt1),
      show excursion r r' a (a + (m + 2) + 1) = r from if_neg (Nat.ne_of_gt lt2), if_pos rfl,
      excursion_changes two a m]

/-- **Controls at both ends settle the dates between exactly when at most one change is
admitted, or no date lies strictly between.** Where the relation takes two values, every
course with at most `k` changes over the `n` steps from `a` that returns to its value at `a`
keeps that value at every date between exactly when `k < 2` or `n < 2`. -/
theorem bracket_settles_iff {r r' : R} (two : r ≠ r') (a n k : Nat) :
    (∀ c : Nat → R, changes c a n ≤ k → c (a + n) = c a → ∀ j, j ≤ n → c (a + j) = c a) ↔
      (k < 2 ∨ n < 2) :=
  ⟨fun settles =>
    match Nat.decLt k 2, Nat.decLt n 2 with
    | isTrue lt, _ => .inl lt
    | isFalse _, isTrue lt => .inr lt
    | isFalse nk, isFalse nn => by
      have ⟨m, e⟩ := le_dest (Nat.le_of_not_lt nn)
      subst e
      have within : changes (excursion r r' a) a (2 + m) ≤ k := by
        rw [Nat.add_comm 2 m, excursion_changes two a m]
        exact Nat.le_of_not_lt nk
      have far : a + (2 + m) ≠ a + 1 := Nat.ne_of_gt
        (Nat.add_lt_add_left (Nat.lt_of_lt_of_le (Nat.lt_succ_self 1) (Nat.le_add_right 2 m)) a)
      have back : excursion r r' a (a + (2 + m)) = excursion r r' a a :=
        (if_neg far).trans (if_neg (Nat.ne_of_lt (Nat.lt_succ_self a))).symm
      have at1 := settles (excursion r r' a) within back 1
        (Nat.le_trans (Nat.le_succ 1) (Nat.le_add_right 2 m))
      have e1 : excursion r r' a (a + 1) = r' := if_pos rfl
      have e0 : excursion r r' a a = r := if_neg (Nat.ne_of_lt (Nat.lt_succ_self a))
      exact absurd (e1.symm.trans (at1.trans e0)) (fun h => two h.symm),
   fun few c within back j le =>
    match decEq (c (a + j)) (c a) with
    | isTrue e => e
    | isFalse away => by
      have ⟨m, e⟩ := le_dest le
      subst e
      have twice := bracket c a j m back away
      exact match few with
        | .inl lt => absurd (Nat.le_trans twice within) (Nat.not_le_of_lt lt)
        | .inr lt => absurd (Nat.le_trans twice (changes_le c a (j + m))) (Nat.not_le_of_lt lt)⟩

/-- The course at `r` before date `t` and at `r'` from `t` on. -/
def stepAt (r r' : R) (t : Nat) (i : Nat) : R := if i < t then r else r'

/-- A course changing once, between `a + j` and `a + j + 1`, has one change over every span
from `a` containing that step. -/
theorem step_changes {r r' : R} (two : r ≠ r') (a j m : Nat) :
    changes (stepAt r r' (a + j + 1)) a (j + 1 + m) = 1 := by
  rw [changes_split]
  have before : changes (stepAt r r' (a + j + 1)) a j = 0 :=
    changes_const _ a r j fun i le => if_pos (Nat.lt_succ_of_le (Nat.add_le_add_left le a))
  have after : changes (stepAt r r' (a + j + 1)) (a + (j + 1)) m = 0 :=
    changes_const _ (a + (j + 1)) r' m fun i _ =>
      if_neg (Nat.not_lt_of_le (Nat.le_add_right (a + (j + 1)) i))
  rw [after]
  show changes (stepAt r r' (a + j + 1)) a j +
    (if stepAt r r' (a + j + 1) (a + j) = stepAt r r' (a + j + 1) (a + j + 1) then 0 else 1) + 0 = 1
  rw [before, show stepAt r r' (a + j + 1) (a + j) = r from if_pos (Nat.lt_succ_self _),
    show stepAt r r' (a + j + 1) (a + j + 1) = r' from if_neg (Nat.lt_irrefl _), if_neg two]

/-- **A change seen at both ends is not located.** Where the relation is `r` at `a` and `r'` at
`a + n`, each date strictly between holds `r'` on one course and `r` on another, both with one
change: the controls at the ends do not settle it. -/
theorem change_unlocated {r r' : R} (two : r ≠ r') (a j m : Nat) :
    changes (stepAt r r' (a + j + 1)) a (j + 1 + (m + 1)) = 1 ∧
      changes (stepAt r r' (a + (j + 1) + 1)) a (j + 1 + 1 + m) = 1 ∧
      stepAt r r' (a + j + 1) a = r ∧ stepAt r r' (a + (j + 1) + 1) a = r ∧
      stepAt r r' (a + j + 1) (a + (j + 1 + (m + 1))) = r' ∧
      stepAt r r' (a + (j + 1) + 1) (a + (j + 1 + 1 + m)) = r' ∧
      stepAt r r' (a + j + 1) (a + j + 1) = r' ∧ stepAt r r' (a + (j + 1) + 1) (a + j + 1) = r :=
  ⟨step_changes two a j (m + 1), step_changes two a (j + 1) m,
   if_pos (Nat.lt_succ_of_le (Nat.le_add_right a j)),
   if_pos (Nat.lt_succ_of_le (Nat.le_add_right a (j + 1))),
   if_neg (show ¬ a + (j + 1 + (m + 1)) < a + j + 1 from Nat.not_lt_of_le
     (Nat.le_trans (Nat.le_add_right (a + j + 1) (m + 1)) (Nat.le_of_eq (Nat.add_assoc a (j + 1) (m + 1))))),
   if_neg (show ¬ a + (j + 1 + 1 + m) < a + (j + 1) + 1 from Nat.not_lt_of_le
     (Nat.add_le_add_left (Nat.le_add_right (j + 1 + 1) m) a)),
   if_neg (Nat.lt_irrefl _),
   if_pos (Nat.lt_succ_self _)⟩

end Changes

end Becoming.Retrodiction
