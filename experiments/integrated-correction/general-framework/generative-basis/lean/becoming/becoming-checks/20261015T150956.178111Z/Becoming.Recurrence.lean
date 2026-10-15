import Becoming.Frame

/-!
# Recurrence: what every law of change keeps, loses and returns to

The other modules state laws of amounts, flows and webs. This module states what holds of
every law of change on configurations of any kind, with no premise about it: no balance, no
dissipation, no enclosure and no decidability. A configuration is whatever an unfolding is at
a step. A law is a process of the spine (`Becoming.Frame`) or, where the change is a function
of the configuration, a determined law `next`. That a list holds the configurations is not
assumed of any unfolding; it is the condition written into each law that uses it.

* **Revisiting, with no decidability.** If a list holds the first `l.length + 1`
  configurations of a sequence, two of them coincide (`revisits_within`); membership is used
  as given and nothing about the configurations is decided. A sequence held by a list
  revisits from every step on (`revisits_from`), and so does every run of every process
  whose configurations a list holds (`Run.revisits_from`). Never revisiting needs openness:
  no list holds a sequence that never revisits (`unheld_of_new`, `unlisted_of_new`).
* **A marked change does not recur.** Where a quantity of the configuration never falls and rises
  across every change (`Marks`), change within finitely many configurations does not recur
  (`Marks.change_not_recurring`, `Run.change_not_recurring`); while change recurs there, no quantity
  marks it (`not_marks`).
* **What every law keeps and loses.** Under a determined law a possibility lost stays lost
  (`lost_stays`), and under every process a configuration no longer reachable stays so along
  every continuation (`Reach.lost_stays`). Every configuration reachable from `s` stays
  reachable from `t` exactly when `t` leads back to `s` (`keeps_reach_iff_returns`,
  `same_reach_iff_returns`), and no way back is a lost possibility, `s` itself being one
  (`not_returns_iff_loses`). Configurations merged stay merged: no later step
  tells them apart (`merged_stays`). A law under which every configuration returns merges
  nothing (`lossless_of_returns`), and a configuration that returns can be had at every step
  (`Returns.reachable`). Undoing is going on: where `s` returns, further steps of the same
  law lead from `next s` back to `s` (`Returns.undo`).
* **What can be realized together, and within how many moves.** A bundle of claims is realized
  together within `n` moves where a course of at most `n` moves ends at a configuration
  realizing every claim of it (`WithinMoves`). A course carries every such bound, its own
  moves counted (`WithinMoves.after_course`); some bound exists exactly where a configuration
  realizing the bundle is reachable (`withinMoves_iff_reach`), so along a course nothing becomes
  realizable together that was not before (`together_after_reach`), and a bundle no longer
  realizable together marks a course with no way back (`lost_together_not_returns`). The bound
  is not kept: a step can shorten it, as the bridge's joint-activation instance shows.
* **Within finitely many configurations, losing nothing is returning.** Where a list holds
  every configuration, three are one: the law merges nothing (`Lossless`), every
  configuration returns, and every configuration can be had at every step
  (`lossless_iff_returns`, `returns_iff_keeps`, `Lossless.returns`, `returns_of_reachable`).
  So a merge loses a possibility for good (`Merges.loses`), and a law that merges nothing
  while some configuration never returns has no list holding every configuration
  (`Lossless.unlisted`). Losing nothing, no quantity that never falls along an orbit rises on
  it (`Lossless.no_rise`), so a quantity that never falls along an orbit and rises at some
  step of it, an arrow, needs a law that merges (`rise_not_lossless`).
* **Open worlds separate the three.** Counting on (`Nat.succ`) merges nothing, never returns,
  cannot have its beginning again after one step, and rises at every step: an arrow without
  loss (`succ_open`). Counting down (`Nat.pred`) merges zero and one, yet every number can be
  had at every step (`pred_open`).
* **The history kept.** Keeping its history (`withHistory`: the present goes on by the law
  and passes into the past), every law merges nothing (`withHistory_lossless`), never
  revisits (`withHistory_new`) and never returns (`withHistory_never_returns`); its
  beginning cannot be had again after the first step (`withHistory_loses_beginning`), and no
  list holds the kept history of an unfolding (`withHistory_unlisted`). The present of the
  kept history goes on by the law itself (`present_orbit`). Where the present returns, it
  comes back with another history (`return_keeps_history`). Where a list holds the
  configurations an unfolding passes through, the present forgets: from every step on, two
  different histories share one present (`present_forgets`).
* **The law as a process.** A determined law is a process of the spine with one action, and
  its orbit is a run of it (`Law.process`, `Law.run`).

So, with no premise: within finitely many configurations a law that merges nothing returns
every configuration and raises nothing, an arrow needs a merge, a merge loses a possibility
for good, and a marked change does not recur. What is merged stays merged and what is lost stays
lost. Becoming that keeps what it passes through loses nothing, never returns and needs an
open world, while its present, held within finitely many configurations, forgets. Readings
of these laws as entropy, as the passing Ren names, or as thermodynamic recurrence belong to
the study, not to this module.

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming
open Generative

universe u v w

section Sequences

variable {S : Type u}

/-! ## Revisiting, with no decidability -/

/-- A step that comes no later than `K + 1` is no later than `K` or is `K + 1`. -/
theorem le_succ_cases {n K : Nat} (le : n ≤ K + 1) : n ≤ K ∨ n = K + 1 :=
  match Nat.lt_or_ge n (K + 1) with
  | .inl lt => Or.inl (Nat.le_of_lt_succ lt)
  | .inr ge => Or.inr (Nat.le_antisymm le ge)

/-- How far `k` lies beyond `t`. -/
theorem gap_of_le {t : Nat} : ∀ {k : Nat}, t ≤ k → ∃ d, k = t + d := by
  intro k le
  induction le with
  | refl => exact ⟨0, rfl⟩
  | step _ ih =>
    let ⟨d, same⟩ := ih
    exact ⟨d + 1, congrArg Nat.succ same⟩

/-- How far `j` lies beyond `i`, at least one step. -/
theorem gap_of_lt {i j : Nat} (lt : i < j) : ∃ d, j = i + (d + 1) :=
  let ⟨d, same⟩ := gap_of_le lt
  ⟨d, same.trans (Nat.succ_add i d)⟩

theorem mem_cons_split {x a : S} {l : List S} (mem : x ∈ a :: l) : x = a ∨ x ∈ l := by
  cases mem with
  | head => exact Or.inl rfl
  | tail _ mem => exact Or.inr mem

/-- The `n`-th number other than `m`, counting from zero. -/
def skipAt : Nat → Nat → Nat
  | 0, n => n + 1
  | _ + 1, 0 => 0
  | m + 1, n + 1 => skipAt m n + 1

theorem skipAt_ne : ∀ m n, skipAt m n ≠ m
  | 0, _ => fun same => Nat.noConfusion same
  | _ + 1, 0 => fun same => Nat.noConfusion same
  | m + 1, n + 1 => fun same => skipAt_ne m n (Nat.succ.inj same)

theorem skipAt_le : ∀ m n, skipAt m n ≤ n + 1
  | 0, _ => Nat.le_refl _
  | _ + 1, 0 => Nat.zero_le _
  | m + 1, n + 1 => Nat.succ_le_succ (skipAt_le m n)

theorem skipAt_lt : ∀ m {i j : Nat}, i < j → skipAt m i < skipAt m j
  | 0, _, _, lt => Nat.succ_lt_succ lt
  | _ + 1, 0, _ + 1, _ => Nat.succ_pos _
  | m + 1, _ + 1, _ + 1, lt => Nat.succ_lt_succ (skipAt_lt m (Nat.lt_of_succ_lt_succ lt))
  | _ + 1, _, 0, lt => absurd lt (Nat.not_lt_zero _)

/-- Sorting the first `K + 1` values of a sequence held by `a :: l`: two of them coincide, or
all of them lie in `l`, or all but one, which is `a`, lie in `l`. -/
theorem split_at_head {g : Nat → S} {a : S} {l : List S} :
    ∀ K, (∀ n, n ≤ K → g n = a ∨ g n ∈ l) →
      (∃ i j, i < j ∧ j ≤ K ∧ g i = g j) ∨ (∀ n, n ≤ K → g n ∈ l) ∨
        (∃ m, m ≤ K ∧ g m = a ∧ ∀ n, n ≤ K → n ≠ m → g n ∈ l)
  | 0, held =>
    match held 0 (Nat.le_refl 0) with
    | .inl at_a => Or.inr (Or.inr ⟨0, Nat.le_refl 0, at_a,
        fun n le other => absurd (Nat.le_antisymm le (Nat.zero_le n)) other⟩)
    | .inr mem => Or.inr (Or.inl fun n le => by
        have same : n = 0 := Nat.le_antisymm le (Nat.zero_le n)
        subst same
        exact mem)
  | K + 1, held =>
    match split_at_head K (fun n le => held n (Nat.le_succ_of_le le)) with
    | .inl ⟨i, j, lt, le, same⟩ => Or.inl ⟨i, j, lt, Nat.le_succ_of_le le, same⟩
    | .inr (.inl all) =>
      match held (K + 1) (Nat.le_refl _) with
      | .inl at_a => Or.inr (Or.inr ⟨K + 1, Nat.le_refl _, at_a, fun n le other =>
          match le_succ_cases le with
          | .inl le => all n le
          | .inr same => absurd same other⟩)
      | .inr mem => Or.inr (Or.inl fun n le =>
          match le_succ_cases le with
          | .inl le => all n le
          | .inr same => by subst same; exact mem)
    | .inr (.inr ⟨m, le_m, at_m, rest⟩) =>
      match held (K + 1) (Nat.le_refl _) with
      | .inl at_a =>
        Or.inl ⟨m, K + 1, Nat.lt_succ_of_le le_m, Nat.le_refl _, at_m.trans at_a.symm⟩
      | .inr mem => Or.inr (Or.inr ⟨m, Nat.le_succ_of_le le_m, at_m, fun n le other =>
          match le_succ_cases le with
          | .inl le => rest n le other
          | .inr same => by subst same; exact mem⟩)

/-- **Pigeonhole, with no decidability.** If a list holds the first `l.length + 1` values of a
sequence, two of them coincide. Nothing is decided about the configurations: membership
in the list is used as it is given. -/
theorem revisits_within : ∀ (l : List S) (g : Nat → S), (∀ n, n ≤ l.length → g n ∈ l) →
    ∃ i j, i < j ∧ j ≤ l.length ∧ g i = g j
  | [], _, held => nomatch held 0 (Nat.le_refl 0)
  | _ :: l, g, held =>
    match split_at_head (l.length + 1) (fun n le => mem_cons_split (held n le)) with
    | .inl found => found
    | .inr (.inl all) =>
      let ⟨i, j, lt, le, same⟩ :=
        revisits_within l g (fun n le => all n (Nat.le_succ_of_le le))
      ⟨i, j, lt, Nat.le_succ_of_le le, same⟩
    | .inr (.inr ⟨m, _, _, rest⟩) =>
      let ⟨i, j, lt, le, same⟩ := revisits_within l (fun n => g (skipAt m n)) (fun n le =>
        rest (skipAt m n) (Nat.le_trans (skipAt_le m n) (Nat.succ_le_succ le)) (skipAt_ne m n))
      ⟨skipAt m i, skipAt m j, skipAt_lt m lt, Nat.le_trans (skipAt_le m j) (Nat.succ_le_succ le),
        same⟩

/-- Two steps of a sequence at one configuration. -/
def Revisits (g : Nat → S) : Prop := ∃ i j, i < j ∧ g i = g j

/-- A sequence held by a list revisits. -/
theorem revisits_of_held {g : Nat → S} {l : List S} (held : ∀ n, g n ∈ l) : Revisits g :=
  let ⟨i, j, lt, _, same⟩ := revisits_within l g (fun n _ => held n)
  ⟨i, j, lt, same⟩

/-- A sequence held by a list revisits from every step on. -/
theorem revisits_from {g : Nat → S} {l : List S} (held : ∀ n, g n ∈ l) (T : Nat) :
    ∃ i j, T ≤ i ∧ i < j ∧ g i = g j :=
  let ⟨i, j, lt, same⟩ := revisits_of_held (g := fun n => g (T + n)) (fun n => held (T + n))
  ⟨T + i, T + j, Nat.le_add_right T i, Nat.add_lt_add_left lt T, same⟩

/-- **Never revisiting needs openness.** A sequence that never revisits a configuration has
no list holding its first `l.length + 1` values, for any list `l`. -/
theorem unheld_of_new {g : Nat → S} (new : ∀ i j, i < j → g i ≠ g j) (l : List S) :
    ¬ ∀ n, n ≤ l.length → g n ∈ l := fun held =>
  let ⟨i, j, lt, _, same⟩ := revisits_within l g held
  new i j lt same

/-- No list holds a sequence that never revisits. -/
theorem unlisted_of_new {g : Nat → S} (new : ∀ i j, i < j → g i ≠ g j) :
    ¬ ∃ l : List S, ∀ n, g n ∈ l := fun ⟨l, held⟩ =>
  unheld_of_new new l (fun n _ => held n)

/-! ## A mark of every change -/

/-- `q` marks the changes of `g`: a quantity of the configuration that never falls along `g`
and rises across every step at which the configuration changes. -/
def Marks (q : S → Nat) (g : Nat → S) : Prop :=
  ∀ n, q (g n) ≤ q (g (n + 1)) ∧ (g (n + 1) ≠ g n → q (g n) < q (g (n + 1)))

/-- The sum of `q` over a list, which bounds `q` on its members. -/
def sumOver (q : S → Nat) : List S → Nat
  | [] => 0
  | a :: l => q a + sumOver q l

theorem le_sumOver (q : S → Nat) {s : S} {l : List S} (mem : s ∈ l) : q s ≤ sumOver q l := by
  induction mem with
  | head => exact Nat.le_add_right _ _
  | tail _ _ ih => exact Nat.le_trans ih (Nat.le_add_left _ _)

/-- A quantity that never falls along a sequence never falls over any stretch. -/
theorem never_falls_over {q : S → Nat} {g : Nat → S} (step : ∀ n, q (g n) ≤ q (g (n + 1)))
    (T : Nat) : ∀ k, q (g T) ≤ q (g (T + k))
  | 0 => Nat.le_refl _
  | k + 1 => Nat.le_trans (never_falls_over step T k) (step (T + k))

theorem Marks.mono {q : S → Nat} {g : Nat → S} (marks : Marks q g) (T : Nat) :
    ∀ k, q (g T) ≤ q (g (T + k)) :=
  never_falls_over (fun n => (marks n).1) T

/-- **Within finitely many configurations, a marked change does not recur.** Where a list holds the
configurations of `g` and a quantity marks each of its changes, change does not recur. -/
theorem Marks.change_not_recurring {q : S → Nat} {g : Nat → S} (marks : Marks q g) {l : List S}
    (held : ∀ n, g n ∈ l) : ¬ ∀ T, ∃ k, T ≤ k ∧ g (k + 1) ≠ g k := fun recurs =>
  have climb : ∀ m, ∃ t, m ≤ q (g t) := fun m => by
    induction m with
    | zero => exact ⟨0, Nat.zero_le _⟩
    | succ m ih =>
      let ⟨t, le⟩ := ih
      let ⟨k, after, change⟩ := recurs t
      let ⟨d, same⟩ := gap_of_le after
      have up : q (g t) ≤ q (g k) := by rw [same]; exact marks.mono t d
      exact ⟨k + 1, Nat.lt_of_le_of_lt (Nat.le_trans le up) ((marks k).2 change)⟩
  let ⟨t, above⟩ := climb (sumOver q l + 1)
  Nat.lt_irrefl _ (Nat.lt_of_lt_of_le above (le_sumOver q (held t)))

/-- While change recurs within finitely many configurations, no quantity marks it. -/
theorem not_marks {g : Nat → S} {l : List S} (held : ∀ n, g n ∈ l)
    (recurs : ∀ T, ∃ k, T ≤ k ∧ g (k + 1) ≠ g k) (q : S → Nat) : ¬ Marks q g :=
  fun marks => marks.change_not_recurring held recurs

end Sequences

/-! ## A determined law -/

namespace Law

variable {S : Type u}

/-- The configuration `n` steps after `s` under the law `next`. -/
def orbit (next : S → S) (s : S) : Nat → S
  | 0 => s
  | n + 1 => next (orbit next s n)

theorem orbit_add (next : S → S) (s : S) (m : Nat) :
    ∀ n, orbit next s (m + n) = orbit next (orbit next s m) n
  | 0 => rfl
  | n + 1 => congrArg next (orbit_add next s m n)

theorem orbit_shift (next : S → S) (s : S) (n : Nat) :
    orbit next s (n + 1) = orbit next (next s) n :=
  (congrArg (orbit next s) (Nat.add_comm n 1)).trans (orbit_add next s 1 n)

theorem orbit_mul {next : S → S} {s : S} {p : Nat} (back : orbit next s p = s) :
    ∀ k, orbit next s (p * k) = s
  | 0 => rfl
  | k + 1 => (orbit_add next s (p * k) p).trans
      ((congrArg (fun x => orbit next x p) (orbit_mul back k)).trans back)

/-- `next` merges nothing: distinct configurations go on to distinct configurations. -/
def Lossless (next : S → S) : Prop := ∀ x y, next x = next y → x = y

/-- `next` takes two distinct configurations to one. -/
def Merges (next : S → S) : Prop := ∃ x y, x ≠ y ∧ next x = next y

/-- `s` comes back after some steps. -/
def Returns (next : S → S) (s : S) : Prop := ∃ p, 0 < p ∧ orbit next s p = s

/-- `s` can still be had `n` steps on: some configuration leads to it in `n` steps. -/
def Reachable (next : S → S) (n : Nat) (s : S) : Prop := ∃ x, orbit next x n = s

/-- Every configuration can be had at every step: no possibility is ever lost. -/
def KeepsPossibilities (next : S → S) : Prop := ∀ n s, Reachable next n s

theorem Merges.not_lossless {next : S → S} (merges : Merges next) : ¬ Lossless next :=
  fun lossless => let ⟨x, y, apart, merged⟩ := merges; apart (lossless x y merged)

/-! ### What every law keeps and loses -/

theorem Reachable.earlier {next : S → S} {n : Nat} {s : S} (reach : Reachable next (n + 1) s) :
    Reachable next n s :=
  let ⟨x, to⟩ := reach
  ⟨next x, (orbit_shift next x n).symm.trans to⟩

/-- **A possibility lost stays lost**, under every law. -/
theorem lost_stays {next : S → S} {n : Nat} {s : S} (lost : ¬ Reachable next n s) :
    ∀ k, ¬ Reachable next (n + k) s
  | 0 => lost
  | k + 1 => fun reach => lost_stays lost k reach.earlier

/-- **Configurations merged stay merged**: no later step tells them apart. -/
theorem merged_stays {next : S → S} {x y : S} (merged : next x = next y) (n : Nat) :
    orbit next x (n + 1) = orbit next y (n + 1) :=
  (orbit_shift next x n).trans
    ((congrArg (fun z => orbit next z n) merged).trans (orbit_shift next y n).symm)

/-- Merging nothing at a step, a law merges nothing over any number of steps. -/
theorem Lossless.cancel {next : S → S} (lossless : Lossless next) {x y : S} :
    ∀ n, orbit next x n = orbit next y n → x = y
  | 0, same => same
  | n + 1, same => Lossless.cancel lossless n (lossless _ _ same)

/-- A law under which every configuration returns merges nothing. -/
theorem lossless_of_returns {next : S → S} (returns : ∀ s, Returns next s) : Lossless next :=
  fun x y merged =>
    match returns x, returns y with
    | ⟨0, pos, _⟩, _ => absurd pos (Nat.lt_irrefl 0)
    | _, ⟨0, pos, _⟩ => absurd pos (Nat.lt_irrefl 0)
    | ⟨p + 1, _, back_x⟩, ⟨q + 1, _, back_y⟩ =>
      calc x = orbit next x ((p + 1) * q + p + 1) := (orbit_mul back_x (q + 1)).symm
        _ = orbit next y ((p + 1) * q + p + 1) := merged_stays merged _
        _ = orbit next y ((q + 1) * (p + 1)) :=
          congrArg (orbit next y) (Nat.mul_comm (p + 1) (q + 1))
        _ = y := orbit_mul back_y (p + 1)

/-- A configuration that returns can be had at every step. -/
theorem Returns.reachable {next : S → S} {s : S} (returns : Returns next s) (n : Nat) :
    Reachable next n s :=
  match returns with
  | ⟨0, pos, _⟩ => absurd pos (Nat.lt_irrefl 0)
  | ⟨p + 1, _, back⟩ =>
    ⟨orbit next s (p * n), (orbit_add next s (p * n) n).symm.trans
      ((congrArg (orbit next s) (Nat.succ_mul p n)).symm.trans (orbit_mul back n))⟩

/-- **Undoing is going on.** Where `s` returns, the step from `s` is undone only by going on
under the same law: further steps lead from `next s` back to `s`. -/
theorem Returns.undo {next : S → S} {s : S} (returns : Returns next s) :
    ∃ k, orbit next (next s) k = s :=
  match returns with
  | ⟨0, pos, _⟩ => absurd pos (Nat.lt_irrefl 0)
  | ⟨k + 1, _, back⟩ => ⟨k, (orbit_shift next s k).symm.trans back⟩

/-! ### Finitely many configurations -/

/-- **Losing nothing, everything returns**, where a list holds every configuration. -/
theorem Lossless.returns {next : S → S} (lossless : Lossless next) {all : List S}
    (every : ∀ s, s ∈ all) (s : S) : Returns next s :=
  let ⟨i, _, lt, _, same⟩ := revisits_within all (orbit next s) (fun _ _ => every _)
  let ⟨d, gap⟩ := gap_of_lt lt
  ⟨d + 1, Nat.succ_pos d, lossless.cancel i
    ((orbit_add next s (d + 1) i).symm.trans
      ((congrArg (orbit next s) (Nat.add_comm (d + 1) i)).trans
        ((congrArg (orbit next s) gap.symm).trans same.symm)))⟩

/-- Where a list holds every configuration, a configuration that can be had as many steps on
as the list is long returns. -/
theorem returns_of_reachable {next : S → S} {all : List S} (every : ∀ s, s ∈ all) {s : S}
    (reach : Reachable next all.length s) : Returns next s :=
  let ⟨x, to⟩ := reach
  let ⟨i, _, lt, le, same⟩ := revisits_within all (orbit next x) (fun _ _ => every _)
  let ⟨d, gap⟩ := gap_of_lt lt
  let ⟨e, rest⟩ := gap_of_le (Nat.le_trans (Nat.le_of_lt lt) le)
  have back : orbit next (orbit next x i) (d + 1) = orbit next x i :=
    (orbit_add next x i (d + 1)).symm.trans ((congrArg (orbit next x) gap.symm).trans same.symm)
  have reached : orbit next (orbit next x i) e = s :=
    (orbit_add next x i e).symm.trans ((congrArg (orbit next x) rest.symm).trans to)
  ⟨d + 1, Nat.succ_pos d,
    calc orbit next s (d + 1)
        = orbit next (orbit next (orbit next x i) e) (d + 1) :=
          congrArg (fun w => orbit next w (d + 1)) reached.symm
      _ = orbit next (orbit next x i) (e + (d + 1)) := (orbit_add next _ e (d + 1)).symm
      _ = orbit next (orbit next x i) ((d + 1) + e) :=
          congrArg (orbit next (orbit next x i)) (Nat.add_comm e (d + 1))
      _ = orbit next (orbit next (orbit next x i) (d + 1)) e := orbit_add next _ (d + 1) e
      _ = orbit next (orbit next x i) e := congrArg (fun w => orbit next w e) back
      _ = s := reached⟩

/-- **Losing nothing within finitely many configurations, nothing rises.** Where a list holds
every configuration and the law merges nothing, a quantity that never falls along an orbit
keeps its value along it. -/
theorem Lossless.no_rise {next : S → S} (lossless : Lossless next) {all : List S}
    (every : ∀ s, s ∈ all) {q : S → Nat} {s : S}
    (step : ∀ n, q (orbit next s n) ≤ q (orbit next s (n + 1))) (n : Nat) :
    q (orbit next s n) = q s :=
  match lossless.returns every s with
  | ⟨0, pos, _⟩ => absurd pos (Nat.lt_irrefl 0)
  | ⟨p + 1, _, back⟩ =>
    have far : q (orbit next s n) ≤ q (orbit next s (n + p * n)) :=
      never_falls_over step n (p * n)
    have whole : orbit next s (n + p * n) = s :=
      (congrArg (orbit next s) ((Nat.add_comm n (p * n)).trans (Nat.succ_mul p n).symm)).trans
        (orbit_mul back n)
    Nat.le_antisymm (Nat.le_trans far (Nat.le_of_eq (congrArg q whole)))
      (Nat.le_trans (never_falls_over step 0 n)
        (Nat.le_of_eq (congrArg (fun k => q (orbit next s k)) (Nat.zero_add n))))

/-- **Within finitely many configurations, a rise needs a merge.** Where a list holds every
configuration and a quantity never falls along an orbit yet rises at some step of it, the law
does not merge nothing. -/
theorem rise_not_lossless {next : S → S} {all : List S} (every : ∀ s, s ∈ all) {q : S → Nat}
    {s : S} (step : ∀ n, q (orbit next s n) ≤ q (orbit next s (n + 1))) {n : Nat}
    (rises : q (orbit next s n) < q (orbit next s (n + 1))) : ¬ Lossless next := fun lossless =>
  Nat.ne_of_lt rises
    ((lossless.no_rise every step n).trans (lossless.no_rise every step (n + 1)).symm)

/-- **Within finitely many configurations, losing nothing is returning.** Where a list holds
every configuration, a law merges nothing exactly where every configuration returns. -/
theorem lossless_iff_returns {next : S → S} {all : List S} (every : ∀ s, s ∈ all) :
    Lossless next ↔ ∀ s, Returns next s :=
  ⟨fun lossless => lossless.returns every, lossless_of_returns⟩

/-- **Within finitely many configurations, returning is keeping every possibility.** -/
theorem returns_iff_keeps {next : S → S} {all : List S} (every : ∀ s, s ∈ all) :
    (∀ s, Returns next s) ↔ KeepsPossibilities next :=
  ⟨fun returns n s => (returns s).reachable n,
    fun keeps s => returns_of_reachable every (keeps all.length s)⟩

/-- Within finitely many configurations, keeping the possibilities of one more step than
there are configurations already keeps every possibility, and merges nothing. -/
theorem lossless_of_reachable {next : S → S} {all : List S} (every : ∀ s, s ∈ all)
    (reach : ∀ s, Reachable next all.length s) : Lossless next :=
  lossless_of_returns fun s => returns_of_reachable every (reach s)

/-- **Within finitely many configurations, a merge loses a possibility for good**: some
configuration cannot be had as many steps on as there are configurations, nor at any later
step (`lost_stays`). -/
theorem Merges.loses {next : S → S} (merges : Merges next) {all : List S}
    (every : ∀ s, s ∈ all) : ¬ ∀ s, Reachable next all.length s :=
  fun reach => merges.not_lossless (lossless_of_reachable every reach)

/-- **Losing nothing without return needs openness.** A law that merges nothing and under
which some configuration never returns has no list holding every configuration. -/
theorem Lossless.unlisted {next : S → S} (lossless : Lossless next) {s : S}
    (never : ¬ Returns next s) : ¬ ∃ all : List S, ∀ x, x ∈ all :=
  fun ⟨_, every⟩ => never (lossless.returns every s)

/-! ### Open witnesses -/

theorem succ_orbit (s : Nat) : ∀ n, orbit Nat.succ s n = s + n
  | 0 => rfl
  | n + 1 => congrArg Nat.succ (succ_orbit s n)

/-- **Counting on loses nothing and never returns.** Under `Nat.succ` nothing merges, nothing
returns, and the beginning can no longer be had after one step. -/
theorem succ_open :
    Lossless Nat.succ ∧ (∀ s, ¬ Returns Nat.succ s) ∧ ¬ Reachable Nat.succ 1 0 ∧
      ∀ s n, orbit Nat.succ s n < orbit Nat.succ s (n + 1) :=
  ⟨fun _ _ same => Nat.succ.inj same,
    fun s ⟨p, pos, back⟩ => Nat.lt_irrefl s (Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right pos)
      (Nat.le_of_eq ((succ_orbit s p).symm.trans back))),
    fun ⟨x, to⟩ => Nat.add_one_ne_zero x to, fun _ _ => Nat.lt_succ_self _⟩

theorem pred_orbit : ∀ n t, orbit Nat.pred (t + n) n = t
  | 0, _ => rfl
  | n + 1, t => congrArg Nat.pred
      ((congrArg (fun x => orbit Nat.pred x n) (Nat.succ_add t n).symm).trans
        (pred_orbit n (t + 1)))

/-- **Counting down merges and keeps every possibility.** Under `Nat.pred` zero and one go to
zero, yet every number can be had at every step: in an open world a merge need not lose a
possibility. -/
theorem pred_open : Merges Nat.pred ∧ KeepsPossibilities Nat.pred :=
  ⟨⟨0, 1, fun same => Nat.noConfusion same, rfl⟩, fun n t => ⟨t + n, pred_orbit n t⟩⟩

/-! ### The history kept -/

/-- The law with its history kept: the present goes on by `next` and passes into the past. -/
def withHistory (next : S → S) (h : S × List S) : S × List S := (next h.1, h.1 :: h.2)

/-- **Keeping its history, every law loses nothing.** -/
theorem withHistory_lossless (next : S → S) : Lossless (withHistory next) := by
  intro ⟨a, p⟩ ⟨b, q⟩ same
  have tails : a :: p = b :: q := congrArg Prod.snd same
  have ⟨ha, hp⟩ := List.cons.inj tails
  subst ha
  subst hp
  rfl

theorem past_length (next : S → S) (h : S × List S) :
    ∀ n, (orbit (withHistory next) h n).2.length = h.2.length + n
  | 0 => rfl
  | n + 1 => congrArg Nat.succ (past_length next h n)

/-- The present of the kept history goes on by the law itself. -/
theorem present_orbit (next : S → S) (h : S × List S) :
    ∀ n, (orbit (withHistory next) h n).1 = orbit next h.1 n
  | 0 => rfl
  | n + 1 => congrArg next (present_orbit next h n)

/-- **The kept history never revisits.** -/
theorem withHistory_new (next : S → S) (h : S × List S) {i j : Nat} (lt : i < j) :
    orbit (withHistory next) h i ≠ orbit (withHistory next) h j := fun same =>
  Nat.ne_of_lt (Nat.add_lt_add_left lt h.2.length)
    ((past_length next h i).symm.trans
      ((congrArg (fun x => x.2.length) same).trans (past_length next h j)))

/-- **Keeping its history, nothing returns.** -/
theorem withHistory_never_returns (next : S → S) (h : S × List S) :
    ¬ Returns (withHistory next) h :=
  fun ⟨_, pos, back⟩ => withHistory_new next h pos back.symm

/-- **Keeping its history, the beginning is lost at the first step.** No kept history with
nothing past can be had one or more steps on. -/
theorem withHistory_loses_beginning (next : S → S) (s : S) (n : Nat) :
    ¬ Reachable (withHistory next) (n + 1) (s, []) := fun ⟨x, to⟩ =>
  Nat.add_one_ne_zero (x.2.length + n)
    ((past_length next x (n + 1)).symm.trans (congrArg (fun y => y.2.length) to))

/-- **Keeping its history needs openness.** No list holds the kept history of an unfolding. -/
theorem withHistory_unlisted (next : S → S) (h : S × List S) :
    ¬ ∃ l : List (S × List S), ∀ n, orbit (withHistory next) h n ∈ l :=
  fun ⟨_, held⟩ =>
    let ⟨_, _, lt, same⟩ := revisits_of_held held
    withHistory_new next h lt same

/-- **A finite present forgets.** Where a list holds the configurations an unfolding passes
through, from every step on two different kept histories share one present. -/
theorem present_forgets (next : S → S) {s : S} {l : List S} (held : ∀ n, orbit next s n ∈ l)
    (T : Nat) :
    ∃ i j, T ≤ i ∧ i < j ∧
      (orbit (withHistory next) (s, []) i).1 = (orbit (withHistory next) (s, []) j).1 ∧
      orbit (withHistory next) (s, []) i ≠ orbit (withHistory next) (s, []) j :=
  let ⟨i, j, le, lt, same⟩ := revisits_from held T
  ⟨i, j, le, lt,
    (present_orbit next (s, []) i).trans (same.trans (present_orbit next (s, []) j).symm),
    withHistory_new next (s, []) lt⟩

/-- **The present comes back; the history does not.** Where `s` returns after `p` steps, the
kept history from `s` with any past has, `p` steps on, the present `s` again and another
history. -/
theorem return_keeps_history {next : S → S} {s : S} {p : Nat} (pos : 0 < p)
    (back : orbit next s p = s) (past : List S) :
    (orbit (withHistory next) (s, past) p).1 = s ∧
      orbit (withHistory next) (s, past) p ≠ (s, past) :=
  ⟨(present_orbit next (s, past) p).trans back,
    fun same => withHistory_new next (s, past) pos same.symm⟩

/-! ### The law as a process -/

/-- A determined law as a process of the spine: one action, the step to `next s`. -/
def process (next : S → S) : Process S Unit := ⟨fun s _ t => t = next s⟩

/-- The run of a determined law from `s`. -/
def run (next : S → S) (s : S) : Run (process next) :=
  ⟨orbit next s, fun _ => (), fun _ => rfl⟩

theorem run_state (next : S → S) (s : S) : (run next s).state = orbit next s := rfl

end Law

/-! ## Every run of every process -/

section Runs

variable {S : Type u} {A : Type v} {P : Process S A}

/-- A run of any process whose configurations a list holds revisits from every step on. -/
theorem Run.revisits_from (r : Run P) {l : List S} (held : ∀ n, r.state n ∈ l) (T : Nat) :
    ∃ i j, T ≤ i ∧ i < j ∧ r.state i = r.state j :=
  Becoming.revisits_from held T

/-- A run whose configurations a list holds and whose changes a quantity marks: change does not
recur. -/
theorem Run.change_not_recurring (r : Run P) {l : List S} (held : ∀ n, r.state n ∈ l) {q : S → Nat}
    (marks : Marks q r.state) : ¬ ∀ T, ∃ k, T ≤ k ∧ r.state (k + 1) ≠ r.state k :=
  marks.change_not_recurring held

/-- A possibility lost along an admissible path stays lost along every continuation. -/
theorem Reach.lost_stays {t u t' : S} (lost : ¬ Reach P t u) (onward : Reach P t t') :
    ¬ Reach P t' u :=
  fun back => lost (onward.trans back)

/-- **What can be had from a configuration is kept exactly where it can be had again.** Every
configuration reachable from `s` is reachable from `t` exactly when `t` leads back to `s`. -/
theorem keeps_reach_iff_returns {s t : S} : (∀ u, Reach P s u → Reach P t u) ↔ Reach P t s :=
  ⟨fun keeps => keeps s (Reach.refl P s), fun back _ there => back.trans there⟩

/-- **Along a path, the same possibilities exactly where it can be undone.** For `t` reached
from `s`, the configurations reachable from both are the same exactly when `t` leads back to
`s`. -/
theorem same_reach_iff_returns {s t : S} (onward : Reach P s t) :
    (∀ u, Reach P s u ↔ Reach P t u) ↔ Reach P t s :=
  ⟨fun same => (same s).mp (Reach.refl P s),
   fun back _ => ⟨fun there => back.trans there, fun there => onward.trans there⟩⟩

/-- **No way back is a lost possibility, with a witness.** `t` does not lead back to `s` exactly
when some configuration reachable from `s` is not reachable from `t`: `s` itself is one. -/
theorem not_returns_iff_loses {s t : S} : ¬ Reach P t s ↔ ∃ u, Reach P s u ∧ ¬ Reach P t u :=
  ⟨fun away => ⟨s, Reach.refl P s, away⟩, fun ⟨_, there, lost⟩ back => lost (back.trans there)⟩

end Runs


section Together

variable {S : Type u} {A : Type v} {C : Type w}

/-- A bundle of claims realized together, at one configuration, at the end of a course of at most
`n` moves from `s`. -/
def WithinMoves (P : Process S A) (realized : S → C → Prop) (s : S) (n : Nat)
    (bundle : C → Prop) : Prop :=
  ∃ word t, Trace P s word t ∧ word.length ≤ n ∧ ∀ c, bundle c → realized t c

variable {P : Process S A} {realized : S → C → Prop} {bundle : C → Prop}

/-- One step before adds one move to the bound. -/
theorem WithinMoves.before {s m : S} {a : A} {n : Nat} (step : P.step s a m) :
    WithinMoves P realized m n bundle → WithinMoves P realized s (n + 1) bundle
  | ⟨word, t, path, short, holds⟩ => ⟨a :: word, t, .cons step path, Nat.succ_le_succ short, holds⟩

/-- **A course carries every bound on realizing a bundle together, its own moves counted.** -/
theorem WithinMoves.after_course {n : Nat} :
    ∀ {s t : S} {xs : List A}, Trace P s xs t → WithinMoves P realized t n bundle →
      WithinMoves P realized s (xs.length + n) bundle
  | _, _, _, .nil _, within =>
    Eq.subst (motive := fun k => WithinMoves P realized _ k bundle) (Nat.zero_add n).symm within
  | _, _, _, .cons step path, within =>
    Eq.subst (motive := fun k => WithinMoves P realized _ k bundle) (Nat.succ_add _ n).symm
      (WithinMoves.before step (WithinMoves.after_course path within))

/-- **Realizable together within some bound is a reachable configuration realizing the
bundle.** -/
theorem withinMoves_iff_reach {s : S} :
    (∃ n, WithinMoves P realized s n bundle) ↔ ∃ t, Reach P s t ∧ ∀ c, bundle c → realized t c :=
  ⟨fun ⟨_, word, t, path, _, holds⟩ => ⟨t, ⟨word, path⟩, holds⟩,
   fun ⟨t, ⟨word, path⟩, holds⟩ => ⟨word.length, word, t, path, Nat.le_refl _, holds⟩⟩

/-- **Along a course nothing becomes realizable together that was not before.** -/
theorem together_after_reach {s t : S} (onward : Reach P s t) :
    (∃ n, WithinMoves P realized t n bundle) → ∃ n, WithinMoves P realized s n bundle
  | ⟨n, within⟩ => match onward with
    | ⟨xs, path⟩ => ⟨xs.length + n, WithinMoves.after_course path within⟩

/-- **A bundle no longer realizable together marks a course with no way back.** -/
theorem lost_together_not_returns {s t : S}
    (before : ∃ n, WithinMoves P realized s n bundle)
    (after : ¬ ∃ n, WithinMoves P realized t n bundle) : ¬ Reach P t s :=
  fun back => after (together_after_reach back before)

end Together

end Becoming
