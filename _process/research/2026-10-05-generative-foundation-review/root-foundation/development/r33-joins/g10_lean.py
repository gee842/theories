#!/usr/bin/env python3
"""R33 (G10): from a LocalLaw and an interleaving, the World; what of it the interleaving does not
fix. Appended to Becoming.Interleavings, which now imports Becoming.World (L0) for the World."""
from pathlib import Path
B = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
p = B / 'Interleavings.lean'
s = p.read_text()
assert s.startswith('import Becoming.Frame\n')
s = s.replace('import Becoming.Frame\n', 'import Becoming.World\n', 1)
block = '''
/-! ## Each relatum's course of standings -/

variable (law) in
/-- What a relatum stands at after each exchange of its own course, in order. -/
def standings (x : X) : List E → (X → σ) → List σ
  | [], _ => []
  | e :: es, s => match law.touches e x with
    | true => law.act e s x :: standings x es (law.act e s)
    | false => standings x es (law.act e s)

theorem standings_true {x : X} {e : E} (es : List E) (s : X → σ) (touch : law.touches e x = true) :
    law.standings x (e :: es) s = law.act e s x :: law.standings x es (law.act e s) := by
  show (match law.touches e x with
    | true => law.act e s x :: law.standings x es (law.act e s)
    | false => law.standings x es (law.act e s)) = _
  rw [touch]

theorem standings_false {x : X} {e : E} (es : List E) (s : X → σ)
    (touch : law.touches e x = false) :
    law.standings x (e :: es) s = law.standings x es (law.act e s) := by
  show (match law.touches e x with
    | true => law.act e s x :: law.standings x es (law.act e s)
    | false => law.standings x es (law.act e s)) = _
  rw [touch]

/-- Agreeing configurations give every relatum the same course of standings. -/
theorem standings_agree (x : X) : ∀ (L : List E) {s s' : X → σ}, (∀ y, s y = s' y) →
    law.standings x L s = law.standings x L s'
  | [], _, _, _ => rfl
  | e :: L, s, s', same => by
    cases touch : law.touches e x with
    | true =>
      rw [standings_true L s touch, standings_true L s' touch, act_agree e same x,
        standings_agree x L (act_agree e same)]
    | false =>
      rw [standings_false L s touch, standings_false L s' touch,
        standings_agree x L (act_agree e same)]

/-- **Moving an exchange forward past exchanges sharing no relatum with it** leaves every relatum's
course of standings as it was. -/
theorem standings_move (x : X) {e : E} (B : List E) : ∀ (A : List E), (∀ a, a ∈ A → law.Apart e a) →
    ∀ s, law.standings x (A ++ e :: B) s = law.standings x (e :: (A ++ B)) s
  | [], _, _ => rfl
  | a :: A, apart, s => by
    have apartA : law.Apart e a := apart a (.head A)
    have rest := standings_move x B A (fun b mem => apart b (.tail a mem)) (law.act a s)
    have tail : law.standings x (A ++ B) (law.act e (law.act a s)) =
        law.standings x (A ++ B) (law.act a (law.act e s)) :=
      standings_agree x (A ++ B) (fun y => (act_comm apartA s y).symm)
    show law.standings x (a :: (A ++ e :: B)) s = law.standings x (e :: a :: (A ++ B)) s
    cases touchA : law.touches a x with
    | true =>
      have touchE : law.touches e x = false := apartA.symm x touchA
      rw [standings_true (A ++ e :: B) s touchA, rest, standings_false (A ++ B) (law.act a s) touchE,
        standings_false (a :: (A ++ B)) s touchE, standings_true (A ++ B) (law.act e s) touchA, tail,
        law.reads a (law.act e s) s x (fun y touchY => law.keeps e s y (apartA.symm y touchY))
          touchA]
    | false =>
      rw [standings_false (A ++ e :: B) s touchA, rest]
      cases touchE : law.touches e x with
      | true =>
        rw [standings_true (A ++ B) (law.act a s) touchE, standings_true (a :: (A ++ B)) s touchE,
          standings_false (A ++ B) (law.act e s) touchA, tail,
          law.reads e (law.act a s) s x (fun y touchY => law.keeps a s y (apartA y touchY)) touchE]
      | false =>
        rw [standings_false (A ++ B) (law.act a s) touchE, standings_false (a :: (A ++ B)) s touchE,
          standings_false (A ++ B) (law.act e s) touchA, tail]

/-- A list of exchanges touching no relatum gives no relatum a standing. -/
theorem standings_idle (x : X) : ∀ {L : List E}, (∀ y, law.ownCourse y L = []) →
    ∀ s, law.standings x L s = []
  | [], _, _ => rfl
  | e :: L, idle, s => by
    have untouched : ∀ y, law.touches e y = false := by
      intro y
      cases touch : law.touches e y with
      | false => rfl
      | true => exact absurd ((ownCourse_true L touch).symm.trans (idle y)) cons_ne_nil
    rw [standings_false L s (untouched x)]
    exact standings_idle x (fun y => (ownCourse_false L (untouched y)).symm.trans (idle y)) _

/-- **Equal own courses, equal courses of standings.** With the relata listed, two lists of
exchanges giving every relatum the same own course give every relatum, from the same start, the
same standings after each of its own exchanges, in the same order. -/
theorem standings_of_courses {xs : List X} (listed : ∀ x, x ∈ xs) : ∀ (L M : List E),
    (∀ x, law.ownCourse x L = law.ownCourse x M) → ∀ s x, law.standings x L s = law.standings x M s
  | [], M, same, s, x => (standings_idle x (fun y => (same y).symm) s).symm
  | e :: L, M, same, s, x => by
    cases hit : law.shares xs e e with
    | false =>
      have untouched := untouched_of_shares listed hit
      have rest : ∀ y, law.ownCourse y L = law.ownCourse y M := fun y =>
        (ownCourse_false L (untouched y)).symm.trans (same y)
      rw [standings_false L s (untouched x),
        standings_agree x L (fun y => law.keeps e s y (untouched y))]
      exact standings_of_courses listed L M rest s x
    | true =>
      match exists_of_shares hit with
      | ⟨x₀, touch, _⟩ =>
        match split_heads listed touch (M := M)
          (fun y touchY => ⟨law.ownCourse y L, ((same y).symm.trans (ownCourse_true L touchY))⟩)
        with
        | ⟨A, B, split, apartA, onTouched, onOther⟩ =>
          have rest : ∀ y, law.ownCourse y L = law.ownCourse y (A ++ B) := fun y => by
            cases touchY : law.touches e y with
            | true =>
              have h := (ownCourse_true L touchY).symm.trans ((same y).trans (onTouched y touchY))
              exact cons_tails h
            | false =>
              exact (ownCourse_false L touchY).symm.trans ((same y).trans (onOther y touchY))
          rw [split, standings_move x B A apartA s]
          cases touchX : law.touches e x with
          | true =>
            rw [standings_true L s touchX, standings_true (A ++ B) s touchX,
              standings_of_courses listed L (A ++ B) rest (law.act e s) x]
          | false =>
            rw [standings_false L s touchX, standings_false (A ++ B) s touchX]
            exact standings_of_courses listed L (A ++ B) rest (law.act e s) x

/-- **Two interleavings of the same courses give every relatum the same course of standings.** -/
theorem standings_of_interleavings {xs : List X} (listed : ∀ x, x ∈ xs) {c : X → List E}
    {L M : List E} (inL : law.Interleaves c L) (inM : law.Interleaves c M) (s : X → σ) (x : X) :
    law.standings x L s = law.standings x M s :=
  standings_of_courses listed L M (fun y => (inL y).trans (inM y).symm) s x

/-! ## The world an interleaving builds -/

/-- The exchange at step `t` of a list, if the list has one there. -/
def exchangeAt : List E → Nat → Option E
  | [], _ => none
  | e :: _, 0 => some e
  | _ :: L, t + 1 => exchangeAt L t

variable (law) in
/-- The configuration after the first `t` exchanges of a list. -/
def runUpTo : List E → (X → σ) → Nat → (X → σ)
  | [], s, _ => s
  | _ :: _, s, 0 => s
  | e :: L, s, t + 1 => runUpTo L (law.act e s) t

/-- Across step `t`, the configuration changes by the exchange at `t`, if any. -/
theorem runUpTo_succ : ∀ (L : List E) (s : X → σ) (t : Nat),
    law.runUpTo L s (t + 1) = match exchangeAt L t with
      | none => law.runUpTo L s t
      | some e => law.act e (law.runUpTo L s t)
  | [], _, _ => rfl
  | [_], _, 0 => rfl
  | _ :: _ :: _, _, 0 => rfl
  | _ :: L, _, t + 1 => runUpTo_succ L _ t

/-- From the list's length on, the configuration is the one the whole list reaches. -/
theorem runUpTo_whole : ∀ (L : List E) (s : X → σ) (t : Nat), L.length ≤ t →
    law.runUpTo L s t = law.run L s
  | [], _, _, _ => rfl
  | _ :: _, _, 0, le => absurd le (Nat.not_succ_le_zero _)
  | _ :: L, _, t + 1, le => runUpTo_whole L _ t (Nat.le_of_succ_le_succ le)

/-- Up to a list's length, appending more changes nothing. -/
theorem runUpTo_append_le : ∀ (A R : List E) (s : X → σ) (t : Nat), t ≤ A.length →
    law.runUpTo (A ++ R) s t = law.runUpTo A s t
  | [], [], _, _, _ => rfl
  | [], _ :: _, _, 0, _ => rfl
  | [], _ :: _, _, _ + 1, le => absurd le (Nat.not_succ_le_zero _)
  | _ :: _, _, _, 0, _ => rfl
  | _ :: A, R, _, t + 1, le => runUpTo_append_le A R _ t (Nat.le_of_succ_le_succ le)

/-- After a list, the configuration is the rest's from where the list ends. -/
theorem runUpTo_append : ∀ (A R : List E) (s : X → σ) (t : Nat),
    law.runUpTo (A ++ R) s (A.length + t) = law.runUpTo R (law.run A s) t
  | [], _, _, _ => (congrArg (law.runUpTo _ _) (Nat.zero_add _))
  | _ :: A, R, s, t =>
    (congrArg (law.runUpTo _ s) (Nat.succ_add A.length t)).trans (runUpTo_append A R _ t)

/-- Agreeing configurations agree after the first `t` exchanges. -/
theorem runUpTo_agree : ∀ (L : List E) {s s' : X → σ}, (∀ y, s y = s' y) → ∀ t y,
    law.runUpTo L s t y = law.runUpTo L s' t y
  | [], _, _, same, _, y => same y
  | _ :: _, _, _, same, 0, y => same y
  | e :: L, _, _, same, t + 1, y => runUpTo_agree L (act_agree e same) t y

variable (law) in
/-- The relata of a list that an exchange touches. -/
def touchedIn (e : E) : List X → List X
  | [] => []
  | x :: xs => match law.touches e x with
    | true => x :: touchedIn e xs
    | false => touchedIn e xs

variable [DecidableEq X]

/-- What each relatum present takes from itself across a step from `l` to `l'`: its fall. -/
def fall (l l' : X → Nat) (f c : X) : Nat := if f = c then l c - l' c else 0

/-- What each relatum present gives to itself across a step from `l` to `l'`: its rise. -/
def rise (l l' : X → Nat) (f c : X) : Nat := if f = c then l' c - l c else 0

/-- The world an interleaving builds, from a local law on whole-number standings, the relata
listed, a list of exchanges and a start. Its relata are the relata; at step `t` each stands at
what the first `t` exchanges make of the start, and is active where the exchange at `t` touches
it; its move at `t` has present the listed relata the exchange touches, each taking from itself
its fall and giving to itself its rise. Nothing is required, needed or drawn. -/
def world (law : LocalLaw X E Nat) (xs : List X) (L : List E) (s : X → Nat) : World :=
  World.of X
    ⟨fun t => match exchangeAt L t with
      | none => []
      | some e => law.touchedIn e xs,
     fun t => fall (law.runUpTo L s t) (law.runUpTo L s (t + 1)),
     fun t => rise (law.runUpTo L s t) (law.runUpTo L s (t + 1))⟩
    ⟨fun t => law.runUpTo L s t,
     fun t x => ∃ e, exchangeAt L t = some e ∧ law.touches e x = true,
     fun _ _ _ => False, fun _ _ _ => 0, fun _ _ _ => False⟩

variable {law' : LocalLaw X E Nat}

/-- **The world's standing at step `t` is what the first `t` exchanges make of the start.** -/
theorem world_level (xs : List X) (L : List E) (s : X → Nat) (t : Nat) :
    (world law' xs L s).web.level t = law'.runUpTo L s t :=
  rfl

omit [DecidableEq X] in
theorem total_zero_of : ∀ (l : List X) (q : X → Nat), (∀ f, f ∈ l → q f = 0) → Becoming.total l q = 0
  | [], _, _ => rfl
  | f :: l, q, zero => by
    show q f + Becoming.total l q = 0
    rw [zero f (.head l), total_zero_of l q fun g mem => zero g (.tail f mem)]

/-- Over a list with no repeats, a quantity that is nothing but at `c` totals to its value at `c`
where `c` is in the list. -/
theorem total_single {c : X} {v : Nat} : ∀ {l : List X}, List.Pairwise (fun a b => a ≠ b) l →
    c ∈ l → Becoming.total l (fun f => if f = c then v else 0) = v
  | f :: l, .cons apart rest, mem => by
    show (if f = c then v else 0) + Becoming.total l (fun f => if f = c then v else 0) = v
    match mem_cons_cases mem with
    | .inl same =>
      subst same
      rw [if_pos rfl, total_zero_of l _ fun g memG => if_neg (fun same => apart g memG same.symm),
        Nat.add_zero]
    | .inr later =>
      have other : f ≠ c := fun same => apart c later same
      rw [if_neg other, total_single rest later, Nat.zero_add]

/-- A quantity that is nothing but at `c` totals to nothing over a list without `c`. -/
theorem total_absent {c : X} {v : Nat} : ∀ {l : List X}, ¬ c ∈ l →
    Becoming.total l (fun f => if f = c then v else 0) = 0
  | [], _ => rfl
  | f :: l, out => by
    show (if f = c then v else 0) + Becoming.total l (fun f => if f = c then v else 0) = 0
    rw [if_neg (fun (same : f = c) => out (by subst same; exact .head l)), total_absent (fun mem => out (.tail f mem))]

omit [DecidableEq X] in
theorem touchedIn_mem {e : E} {c : X} : ∀ {xs : List X}, c ∈ xs → law.touches e c = true →
    c ∈ law.touchedIn e xs
  | x :: xs, mem, touch => by
    show c ∈ (match law.touches e x with
      | true => x :: law.touchedIn e xs
      | false => law.touchedIn e xs)
    match mem_cons_cases mem with
    | .inl same =>
      subst same
      rw [touch]
      exact .head _
    | .inr later =>
      cases law.touches e x with
      | true => exact .tail x (touchedIn_mem later touch)
      | false => exact touchedIn_mem later touch

omit [DecidableEq X] in
theorem touchedIn_not_mem {e : E} {c : X} (untouched : law.touches e c = false) :
    ∀ {xs : List X}, ¬ c ∈ law.touchedIn e xs
  | [], mem => nomatch mem
  | x :: xs, mem => by
    have h : c ∈ (match law.touches e x with
      | true => x :: law.touchedIn e xs
      | false => law.touchedIn e xs) := mem
    cases touchX : law.touches e x with
    | true =>
      rw [touchX] at h
      match mem_cons_cases h with
      | .inl same => exact Bool.noConfusion ((same ▸ untouched).symm.trans touchX)
      | .inr later => exact touchedIn_not_mem untouched later
    | false =>
      rw [touchX] at h
      exact touchedIn_not_mem untouched h

omit [DecidableEq X] in
theorem touchedIn_mem_of {e : E} {c : X} : ∀ {xs : List X}, c ∈ law.touchedIn e xs → c ∈ xs
  | x :: xs, mem => by
    have h : c ∈ (match law.touches e x with
      | true => x :: law.touchedIn e xs
      | false => law.touchedIn e xs) := mem
    cases touchX : law.touches e x with
    | true =>
      rw [touchX] at h
      match mem_cons_cases h with
      | .inl same => exact same ▸ .head xs
      | .inr later => exact .tail x (touchedIn_mem_of later)
    | false =>
      rw [touchX] at h
      exact .tail x (touchedIn_mem_of h)

omit [DecidableEq X] in
theorem touchedIn_pairwise {e : E} : ∀ {xs : List X}, List.Pairwise (fun a b => a ≠ b) xs →
    List.Pairwise (fun a b => a ≠ b) (law.touchedIn e xs)
  | [], _ => .nil
  | x :: xs, .cons apart rest => by
    show List.Pairwise _ (match law.touches e x with
      | true => x :: law.touchedIn e xs
      | false => law.touchedIn e xs)
    cases law.touches e x with
    | true => exact .cons (fun b mem => apart b (touchedIn_mem_of mem)) (touchedIn_pairwise rest)
    | false => exact touchedIn_pairwise rest

/-- **The world balances.** With every relatum listed once, at every step each relatum's standing
after the step, with what it took, is its standing before, with what it gave. -/
theorem world_balances {xs : List X} (listed : ∀ x, x ∈ xs)
    (once : List.Pairwise (fun a b => a ≠ b) xs) (L : List E) (s : X → Nat) (t : Nat) (c : X) :
    (world law' xs L s).web.level (t + 1) c + ((world law' xs L s).move t).taken c =
      (world law' xs L s).web.level t c + ((world law' xs L s).move t).given c := by
  show law'.runUpTo L s (t + 1) c +
      Becoming.total (match exchangeAt L t with
        | none => []
        | some e => law'.touchedIn e xs)
        (fun f => fall (law'.runUpTo L s t) (law'.runUpTo L s (t + 1)) f c) =
    law'.runUpTo L s t c +
      Becoming.total (match exchangeAt L t with
        | none => []
        | some e => law'.touchedIn e xs)
        (fun f => rise (law'.runUpTo L s t) (law'.runUpTo L s (t + 1)) f c)
  have step := runUpTo_succ (law := law') L s t
  cases at_t : exchangeAt L t with
  | none =>
    rw [at_t] at step
    show law'.runUpTo L s (t + 1) c + 0 = law'.runUpTo L s t c + 0
    rw [step]
  | some e =>
    rw [at_t] at step
    have step : law'.runUpTo L s (t + 1) = law'.act e (law'.runUpTo L s t) := step
    show law'.runUpTo L s (t + 1) c +
        Becoming.total (law'.touchedIn e xs)
          (fun f => if f = c then law'.runUpTo L s t c - law'.runUpTo L s (t + 1) c else 0) =
      law'.runUpTo L s t c +
        Becoming.total (law'.touchedIn e xs)
          (fun f => if f = c then law'.runUpTo L s (t + 1) c - law'.runUpTo L s t c else 0)
    cases touch : law'.touches e c with
    | true =>
      rw [total_single (touchedIn_pairwise (law := law') (e := e) once)
          (touchedIn_mem (law := law') (listed c) touch),
        total_single (touchedIn_pairwise (law := law') (e := e) once)
          (touchedIn_mem (law := law') (listed c) touch)]
      exact add_sub_turn _ _
    | false =>
      rw [total_absent (touchedIn_not_mem (law := law') (xs := xs) touch),
        total_absent (touchedIn_not_mem (law := law') (xs := xs) touch), step,
        law'.keeps e _ c touch]

/-- **Which interleaving is taken does not change where the world ends.** With the relata listed,
the worlds of two lists giving every relatum the same own course stand alike at every step from both
lengths on. -/
theorem world_final {xs xs' : List X} (listed : ∀ x, x ∈ xs) {L M : List E}
    (same : ∀ x, law'.ownCourse x L = law'.ownCourse x M) (s : X → Nat) {t : Nat}
    (afterL : L.length ≤ t) (afterM : M.length ≤ t) (x : X) :
    (world law' xs' L s).web.level t x = (world law' xs' M s).web.level t x :=
  (congrArg (· x) (runUpTo_whole (law := law') L s t afterL)).trans
    ((run_of_courses listed L M same s x).trans
      (congrArg (· x) (runUpTo_whole (law := law') M s t afterM)).symm)

/-- **Two exchanges sharing no relatum, taken in either order: the worlds stand alike at every step
but the one between them.** -/
theorem world_swap {xs : List X} (A B : List E) {e f : E} (apart : law'.Apart e f) (s : X → Nat)
    {t : Nat} (other : t ≠ A.length + 1) (x : X) :
    (world law' xs (A ++ e :: f :: B) s).web.level t x =
      (world law' xs (A ++ f :: e :: B) s).web.level t x := by
  show law'.runUpTo (A ++ e :: f :: B) s t x = law'.runUpTo (A ++ f :: e :: B) s t x
  cases Nat.lt_or_ge (A.length + 1) t with
  | inl late =>
    match le_dest late with
    | ⟨j, eq⟩ =>
      have at_t : t = A.length + (j + 2) :=
        eq.trans ((Nat.add_assoc A.length 2 j).trans (congrArg (A.length + ·) (Nat.add_comm 2 j)))
      rw [at_t, runUpTo_append (law := law'), runUpTo_append (law := law')]
      exact runUpTo_agree (law := law') B (fun y => act_comm apart (law'.run A s) y) j x
  | inr early =>
    cases Nat.lt_or_ge t (A.length + 1) with
    | inl before =>
      rw [runUpTo_append_le (law := law') A _ s t (Nat.le_of_lt_succ before),
        runUpTo_append_le (law := law') A _ s t (Nat.le_of_lt_succ before)]
    | inr after => exact absurd (Nat.le_antisymm early after) other

/-- **At the step between them, each relatum stands in one world where it stands in the other a
step before or after**: one the first exchange touches stands, in the world taking it first, where
it stands after both in the other, and in the other where it stood before both; and the same with
the two exchanged; one neither touches stands alike. -/
theorem world_swap_between {xs : List X} (A B : List E) {e f : E} (apart : law'.Apart e f)
    (s : X → Nat) (x : X) :
    (law'.touches e x = true →
      (world law' xs (A ++ e :: f :: B) s).web.level (A.length + 1) x =
          (world law' xs (A ++ f :: e :: B) s).web.level (A.length + 2) x ∧
        (world law' xs (A ++ f :: e :: B) s).web.level (A.length + 1) x =
          (world law' xs (A ++ e :: f :: B) s).web.level A.length x) ∧
    (law'.touches f x = true →
      (world law' xs (A ++ f :: e :: B) s).web.level (A.length + 1) x =
          (world law' xs (A ++ e :: f :: B) s).web.level (A.length + 2) x ∧
        (world law' xs (A ++ e :: f :: B) s).web.level (A.length + 1) x =
          (world law' xs (A ++ f :: e :: B) s).web.level A.length x) ∧
    (law'.touches e x = false → law'.touches f x = false →
      (world law' xs (A ++ e :: f :: B) s).web.level (A.length + 1) x =
        (world law' xs (A ++ f :: e :: B) s).web.level (A.length + 1) x) := by
  have at1 : ∀ (g h : E), law'.runUpTo (A ++ g :: h :: B) s (A.length + 1) =
      law'.act g (law'.run A s) := fun g h =>
    (runUpTo_append (law := law') A _ s 1).trans rfl
  have at2 : ∀ (g h : E), law'.runUpTo (A ++ g :: h :: B) s (A.length + 2) =
      law'.runUpTo B (law'.act h (law'.act g (law'.run A s))) 0 := fun g h =>
    (runUpTo_append (law := law') A _ s 2).trans rfl
  have at0 : ∀ (g h : E), law'.runUpTo (A ++ g :: h :: B) s A.length = law'.run A s := fun g h =>
    ((congrArg (law'.runUpTo _ s) (Nat.add_zero A.length).symm).trans
      (runUpTo_append (law := law') A _ s 0)).trans rfl
  have zero : ∀ (r : X → Nat), law'.runUpTo B r 0 = r := fun r => by
    cases B with
    | nil => rfl
    | cons _ _ => rfl
  refine ⟨fun touchE => ⟨?_, ?_⟩, fun touchF => ⟨?_, ?_⟩, fun touchE touchF => ?_⟩
  · show law'.runUpTo (A ++ e :: f :: B) s (A.length + 1) x =
      law'.runUpTo (A ++ f :: e :: B) s (A.length + 2) x
    rw [at1, at2, zero]
    exact (law'.reads e (law'.act f (law'.run A s)) (law'.run A s) x
      (fun y touchY => law'.keeps f _ y (apart y touchY)) touchE).symm
  · show law'.runUpTo (A ++ f :: e :: B) s (A.length + 1) x =
      law'.runUpTo (A ++ e :: f :: B) s A.length x
    rw [at1, at0]
    exact law'.keeps f _ x (apart x touchE)
  · show law'.runUpTo (A ++ f :: e :: B) s (A.length + 1) x =
      law'.runUpTo (A ++ e :: f :: B) s (A.length + 2) x
    rw [at1, at2, zero]
    exact (law'.reads f (law'.act e (law'.run A s)) (law'.run A s) x
      (fun y touchY => law'.keeps e _ y (apart.symm y touchY)) touchF).symm
  · show law'.runUpTo (A ++ e :: f :: B) s (A.length + 1) x =
      law'.runUpTo (A ++ f :: e :: B) s A.length x
    rw [at1, at0]
    exact law'.keeps e _ x (apart.symm x touchF)
  · show law'.runUpTo (A ++ e :: f :: B) s (A.length + 1) x =
      law'.runUpTo (A ++ f :: e :: B) s (A.length + 1) x
    rw [at1, at1, law'.keeps e _ x touchE, law'.keeps f _ x touchF]
'''
anchor = '\nend LocalLaw\n\nend Interleavings\n\nend Becoming'
assert s.count(anchor) == 1
s = s.replace(anchor, '\n' + block + anchor)
hb = """  from any configuration `traced_unique_iff`). Two exchanges sharing no relatum have the same own
  courses in either order (`swap_courses`).
"""
assert s.count(hb) == 1
s = s.replace(hb, hb + """* **The world an interleaving builds.** From a local law on whole-number standings, the relata
  listed and a list of exchanges, `world` is a `World` of the spine (`World.of`): at step `t` each
  relatum stands where the first `t` exchanges leave it (`runUpTo`, `world_level`), is active where
  the exchange at `t` touches it, and takes or gives to itself what the step changes, so with every
  relatum listed once each step balances (`world_balances`). Two interleavings of the same own
  courses give every relatum the same course of standings, the standings after each of its own
  exchanges in order (`standings_of_courses`, `standings_of_interleavings`), and the same standing
  from both lengths on (`world_final`). Exchanging two adjacent exchanges sharing no relatum leaves
  the world alike at every step but the one between them (`world_swap`); at that step each relatum
  either of them touches stands, in one world, where it stands one step later or earlier in the
  other, and one neither touches stands alike (`world_swap_between`).
""", 1)
nb = """Not shown: courses without end (the courses here are finite lists); exchanges that read relata
they do not change, in a footprint of their own (here what an exchange reads and what it may
change are one footprint); the correspondence with a world's footprint of `Becoming.Order`. No
ethical predicate, ranking or axiom occurs."""
assert s.count(nb) == 1
s = s.replace(nb, """Not shown: courses without end (the courses here are finite lists); exchanges that read relata
they do not change, in a footprint of their own (here what an exchange reads and what it may
change are one footprint); the correspondence with a world's footprint of `Becoming.Order`; for
two interleavings of the same courses that differ by more than one exchange of adjacent
exchanges, a step-by-step relation between their worlds (what is shown for them is the course of
standings and the end). No ethical predicate, ranking or axiom occurs.""", 1)
p.write_text(s)
