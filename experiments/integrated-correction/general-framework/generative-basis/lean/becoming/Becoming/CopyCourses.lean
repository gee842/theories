import Becoming.Courses

/-!
# Copy courses: the laws of copying on the courses and runs of its processes

`Becoming.Copying` states when a copy completes, what copies from one shared pool need, what local
draws a word uses, what inspection against a reference does to the product and what doubling
draws. `Becoming.Courses` reads them as processes: a copy's move is a determined law
(`Copying.tick`), whose `n` moves go along its orbit (`Courses.steps_orbit`); inspection is a
process whose moves are the sites inspected (`Courses.inspection`); copies from one shared pool are
a course of the release law (`Courses.release`, `Courses.every_released_iff_course`); doubling is a
process (`Copying.doubling`). This module states the remaining laws of `Becoming.Copying` of those
courses and runs.

* **The order of a course of copies does not decide whether it is a course.** Exchanging two
  adjacent words, which generates every reordering, leaves whether the words are a course of the
  release law as it was (`swap_course_iff`).
* **What a run of the copy draws.** A run of the copy's law from a supplied and covered word reaches,
  after as many moves as the word has tokens, the completed copy (`run_copies`), having drawn the
  word's use of support (`run_drawn`). Under local draws, of two such runs from the same support
  used, over words of one length, the run copying the word with more unlike pairs draws less
  exactly when an unlike attachment draws less (`runs_draw_lt_iff`); over three words whose unlike
  pairs are in arithmetic progression, what the runs have drawn is too (`runs_draw_midpoint`).
* **Inspection on its courses.** A step of the inspection process at a defective site leaves the
  reference's token exactly when the pool holds it and the support covers both draws
  (`inspection_step_matches_iff`). Every course of inspections keeps the count of every token across
  product and pool (`inspection_course_keeps_counts`) and the length of the product
  (`inspection_course_length`), and a course of inspections at faithful sites from the template
  keeps the product the template (`inspection_course_keeps_template`).
* **What a course of doubling holds.** A course of `n` rounds from `k` units runs exactly when the
  stock covers what it draws for, and ends with the `k` units of the start and those drawn for
  (`doubling_course_iff`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative Assurance Copying

universe u

namespace CopyCourses

variable {α : Type u} [DecidableEq α]

/-! ## Copies from one shared pool -/

/-- **The order of a course of copies does not decide whether it is a course.** Exchanging two
adjacent words leaves whether the words are a course of the release law from the pool and support
held as it was. -/
theorem swap_course_iff (draw : Option α → α → Nat) (r : Nat) (pre post : List (List α))
    (u v pool : List α) (supply used : Nat) :
    (∃ c, Trace (ofPartial (Courses.release draw r)) (pool, supply, used) (pre ++ u :: v :: post) c) ↔
      ∃ c, Trace (ofPartial (Courses.release draw r)) (pool, supply, used) (pre ++ v :: u :: post) c :=
  (Courses.every_released_iff_course draw r _ pool supply used).symm.trans
    ((batch_all_swap draw r pre post u v pool supply used).trans
      (Courses.every_released_iff_course draw r _ pool supply used))

/-! ## Runs of the copy -/

/-- **A run of the copy's law from a supplied and covered word reaches the completed copy** after as
many moves as the word has tokens: the word added to the product, the pool without it, and the
support less what was drawn. -/
theorem run_copies (draw : Option α → α → Nat) (r : Run (Law.process (tick draw)))
    {prev : Option α} {built word pool : List α} {free used : Nat}
    (start : r.state 0 = ⟨prev, word, built, pool, free, used⟩) (supplies : Supplies word pool)
    (covered : use draw prev word ≤ free) :
    r.state word.length = ⟨lastOr prev word, [], built ++ word, removeAll word pool,
      free - use draw prev word, used + use draw prev word⟩ :=
  (Branching.law_run_state r word.length).trans
    ((congrArg (fun x => Law.orbit (tick draw) x word.length) start).trans
      ((Courses.steps_orbit draw word.length _).symm.trans
        (copies draw prev built word pool free used supplies covered)))

/-- What the completed run has drawn: the support used at the start and the word's use. -/
theorem run_drawn (draw : Option α → α → Nat) (r : Run (Law.process (tick draw)))
    {prev : Option α} {built word pool : List α} {free used : Nat}
    (start : r.state 0 = ⟨prev, word, built, pool, free, used⟩) (supplies : Supplies word pool)
    (covered : use draw prev word ≤ free) :
    (r.state word.length).used = used + use draw prev word :=
  congrArg Scan.used (run_copies draw r start supplies covered)

/-- **Of two runs copying words of one length under local draws, from the same support used, the
run copying the word with more unlike pairs draws less exactly when an unlike attachment draws
less than a like one.** -/
theorem runs_draw_lt_iff (first same differ : Nat) {x y : α} {l m built built' pool pool' : List α}
    {free free' used : Nat}
    (r r' : Run (Law.process (tick (pairDraw first same differ))))
    (start : r.state 0 = ⟨none, x :: l, built, pool, free, used⟩)
    (supplies : Supplies (x :: l) pool)
    (covered : use (pairDraw first same differ) none (x :: l) ≤ free)
    (start' : r'.state 0 = ⟨none, y :: m, built', pool', free', used⟩)
    (supplies' : Supplies (y :: m) pool')
    (covered' : use (pairDraw first same differ) none (y :: m) ≤ free')
    (lm : l.length = m.length) {d : Nat} (more : unlikeFrom y m = unlikeFrom x l + d)
    (pos : 0 < d) :
    (r'.state (m.length + 1)).used < (r.state (l.length + 1)).used ↔ differ < same :=
  have e := run_drawn (pairDraw first same differ) r start supplies covered
  have e' := run_drawn (pairDraw first same differ) r' start' supplies' covered'
  ⟨fun lt => (use_lt_iff first same differ lm more pos).mp
      (Nat.lt_of_add_lt_add_left
        (Nat.lt_of_le_of_lt (Nat.le_of_eq e'.symm) (Nat.lt_of_lt_of_le lt (Nat.le_of_eq e)))),
   fun lt => Nat.lt_of_le_of_lt (Nat.le_of_eq e')
      (Nat.lt_of_lt_of_le
        (Nat.add_lt_add_left ((use_lt_iff first same differ lm more pos).mpr lt) used)
        (Nat.le_of_eq e.symm))⟩

/-- **Over three runs copying words of one length under local draws, from the same support used,
whose unlike pairs are in arithmetic progression, what the runs have drawn is in arithmetic
progression too.** -/
theorem runs_draw_midpoint (first same differ : Nat) {x y z : α}
    {l m k built₁ built₂ built₃ pool₁ pool₂ pool₃ : List α} {free₁ free₂ free₃ used : Nat}
    (r₁ r₂ r₃ : Run (Law.process (tick (pairDraw first same differ))))
    (start₁ : r₁.state 0 = ⟨none, x :: l, built₁, pool₁, free₁, used⟩)
    (supplies₁ : Supplies (x :: l) pool₁)
    (covered₁ : use (pairDraw first same differ) none (x :: l) ≤ free₁)
    (start₂ : r₂.state 0 = ⟨none, y :: m, built₂, pool₂, free₂, used⟩)
    (supplies₂ : Supplies (y :: m) pool₂)
    (covered₂ : use (pairDraw first same differ) none (y :: m) ≤ free₂)
    (start₃ : r₃.state 0 = ⟨none, z :: k, built₃, pool₃, free₃, used⟩)
    (supplies₃ : Supplies (z :: k) pool₃)
    (covered₃ : use (pairDraw first same differ) none (z :: k) ≤ free₃)
    (lm : l.length = m.length) (km : k.length = m.length)
    (mid : unlikeFrom x l + unlikeFrom z k = 2 * unlikeFrom y m) :
    (r₁.state (l.length + 1)).used + (r₃.state (k.length + 1)).used =
      2 * (r₂.state (m.length + 1)).used :=
  (congrArg (· + (r₃.state (k.length + 1)).used)
      (run_drawn (pairDraw first same differ) r₁ start₁ supplies₁ covered₁)).trans
    ((congrArg (used + use (pairDraw first same differ) none (x :: l) + ·)
        (run_drawn (pairDraw first same differ) r₃ start₃ supplies₃ covered₃)).trans
      ((Nat.add_add_add_comm used _ used _).trans
        ((congrArg (used + used + ·) (use_midpoint first same differ lm km mid)).trans
          ((congrArg (· + 2 * use (pairDraw first same differ) none (y :: m))
              (Nat.two_mul used).symm).trans
            ((Nat.left_distrib 2 used _).symm.trans
              (congrArg (2 * ·)
                (run_drawn (pairDraw first same differ) r₂ start₂ supplies₂ covered₂).symm))))))

/-! ## Inspection on its courses -/

/-- **A step of the inspection process at a defective site leaves the reference's token** exactly
when the pool holds it and the support covers the draws of inspection and exchange. -/
theorem inspection_step_matches_iff (ci ce : Nat) {ref : Nat → Option α} {i : Nat} {x old : α}
    {s u : Scan α} (moved : (Courses.inspection ci ce ref).step s i u) (hr : ref i = some x)
    (hb : nth s.built i = some old) (ne : old ≠ x) :
    nth u.built i = some x ↔ ci + ce ≤ s.free ∧ 0 < countOf x s.pool :=
  Eq.mpr
    (congrArg (fun y : Scan α => (nth y.built i = some x ↔ ci + ce ≤ s.free ∧ 0 < countOf x s.pool))
      moved)
    (inspect_matches_iff ci ce s hr hb ne)

/-- **Every course of inspections keeps the count of every token across product and pool.** -/
theorem inspection_course_keeps_counts (ci ce : Nat) (ref : Nat → Option α) (a : α) :
    ∀ {s u : Scan α} {sites : List Nat}, Trace (Courses.inspection ci ce ref) s sites u →
      countOf a (u.built ++ u.pool) = countOf a (s.built ++ s.pool)
  | _, _, [], .nil _ => rfl
  | s, _, i :: _, .cons moved tail =>
    (inspection_course_keeps_counts ci ce ref a tail).trans
      (moved ▸ inspect_keeps_counts ci ce ref i s a)

omit [DecidableEq α] in
theorem length_setAt : ∀ (b : List α) (i : Nat) (x : α), (setAt b i x).length = b.length
  | [], _, _ => rfl
  | _ :: _, 0, _ => rfl
  | _ :: xs, i + 1, x => congrArg Nat.succ (length_setAt xs i x)

theorem exchangeAt_length (ce i : Nat) (x : α) (s : Scan α) :
    ∀ o : Option α, (exchangeAt ce i x s o).built.length = s.built.length
  | none => rfl
  | some _ => ite_cases (fun r : Scan α => r.built.length = s.built.length)
      (fun _ => length_setAt s.built i x) (fun _ => rfl)

theorem inspectAt_length (ci ce i : Nat) (s : Scan α) :
    ∀ o o' : Option α, (inspectAt ci ce i s o o').built.length = s.built.length
  | none, _ => rfl
  | some _, none => rfl
  | some x, some _ => ite_cases (fun r : Scan α => r.built.length = s.built.length)
      (fun _ => exchangeAt_length ce i x (drawSupport ci s) _) (fun _ => rfl)

/-- **Every course of inspections keeps the length of the product.** -/
theorem inspection_course_length (ci ce : Nat) (ref : Nat → Option α) :
    ∀ {s u : Scan α} {sites : List Nat}, Trace (Courses.inspection ci ce ref) s sites u →
      u.built.length = s.built.length
  | _, _, [], .nil _ => rfl
  | s, _, i :: _, .cons moved tail =>
    (inspection_course_length ci ce ref tail).trans
      (moved ▸ inspectAt_length ci ce i s (ref i) (nth s.built i))

/-- **A course of inspections at faithful sites from the template keeps the product the
template**: it raises no defect, and a product of the template's length with no defect is the
template. -/
theorem inspection_course_keeps_template {t : List α} {ref : Nat → Option α} (ci ce : Nat)
    {s u : Scan α} {sites : List Nat} (faithful : ∀ i, i ∈ sites → FaithfulAt ref t i)
    (path : Trace (Courses.inspection ci ce ref) s sites u) (template : s.built = t) :
    u.built = t :=
  (defects_zero_iff t u.built
      ((inspection_course_length ci ce ref path).trans (congrArg List.length template))).mp
    (Nat.le_antisymm
      (Nat.le_trans (Courses.inspection_course_le ci ce faithful path)
        (Nat.le_of_eq ((congrArg (defects t) template).trans (defects_self t))))
      (Nat.zero_le _))

/-! ## Doubling -/

/-- **What a course of doubling holds.** A course of `n` rounds from `k` units with stock `m` runs
exactly when the stock covers `d * required n k`, and ends with the `k` units of the start and the
`required n k` units drawn for, with what the stock has left. -/
theorem doubling_course_iff (d n k m : Nat) (t : Nat × Nat) :
    Trace (doubling d) (k, m) (rounds n) t ↔
      d * required n k ≤ m ∧ t = (required n k + k, m - d * required n k) :=
  (doubling_iff d n k m t).trans
    (Eq.subst
      (motive := fun x => (d * required n k ≤ m ∧ t = (k * 2 ^ n, m - d * required n k)) ↔
        (d * required n k ≤ m ∧ t = (x, m - d * required n k)))
      (required_add n k).symm Iff.rfl)

end CopyCourses

end Becoming
