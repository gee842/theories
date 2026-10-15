import Becoming.Description

/-!
# Identification: what a bounded record fixes

Read as a truth that modelling projects, the projection being where the limit lies, an
unfolding leaves three questions: whether it has a law of this kind, deriving the law from a
finite record, and naming the classes of the split that makes sense without an axiom.
`Becoming.Description` answers the first: every registered
history is a law read through a registration, and its states are read off it
(`alike_moments_iff`, `finitely_many_states_iff`). `Becoming.Learning` shows that no record
fixes the next value, not even among worlds a list holds; that a learner by refutation that
is not given how many configurations there are comes to rest is unrefuted
(`held_rest_unrefuted`), and its record never shows that it has: given two values, every claim
it makes is refuted, at that step, on a course of a world held by a list sharing its record
(`no_record_fixes_next_finite`). This module states what the situation adds: a bound on its
states. With no premise beyond the bound:

* **Two periods.** A course with period `p + 1` that comes back after `Q` steps at each of its
  first `p` steps comes back after `Q` steps at every step (`period_extends`; Fine and Wilf,
  1965). So two courses repeating from steps `i`, `i'` with periods `q + 1`, `q' + 1` that agree
  before `(i + q + 1) + (i' + q')` agree at every step (`lassos_agree`).
* **A bounded record fixes the course.** A history has at most `N` states exactly where it
  repeats from some step `i` with some period `q + 1`, `i + q + 1 ≤ N`
  (`statesBelow_iff_lasso`). Two histories with at most `N` and `N'` states that agree before
  `N + N' - 1` agree at every step (`bounded_agree`): their records before `N + N' - 1` fix
  them (`record_fixes`). Before `N + N' - 2` they do not: for every `T` a history with one
  state and one with `T + 1` share their record before `T` and differ at `T`
  (`record_short`), for every `N ≥ 2` two histories with at most `N` states share their
  record before `N + N - 2` and differ there (`record_short_twice`), and for every `N` and `N'`
  a history with at most `N` states and one with at most `N'` share their record before
  `N + N' - 2` and differ there (`bounded_agree_exact`): the length `N + N' - 1` is exact for
  every pair of bounds. Records are equal exactly where the courses agree before their length
  (`record_eq_iff`).
* **Induction is deduction where the bound is given.** On a history with at most `N` states, a
  lasso hypothesis within `N` that the record before `N + N - 1` bears out is the law of the
  whole course (`lasso_of_fits`, `bounded_induction`), and one always is
  (`bounded_hypothesis`). The learner given `N` (`withBound`), silent before step
  `N + N - 1` and from then on claiming by the first hypothesis within `N` that the record bears
  out, is refuted at no step of any history with at most `N` states and is right at every step
  from `N + N - 1` on (`withBound_holds`, `withBound_exact`). No learner refuted at no step of every
  history with at most `N ≥ 2` states claims at step `N + N - 2` on each of them
  (`withBound_earliest`): the learner given the bound speaks as early as any can. The
  two-valued negation, on which no fixed value is borne out (`Diagonal.revision_never_rests`), is
  derived from step `3` on by the learner given two states (`negation_derived`).
* **The learner not given the bound rests within it.** A lasso hypothesis within `N`
  refuted at no step of a stretch of `N + N - 1` steps is refuted at no later step
  (`unrefuted_persists`). So on a history with at most `N` states the learner by refutation
  over the lasso hypotheses, given neither `N` nor the course, claims at every step from
  `N + (N + N - 1) * tri N` on and is right (`learner_rests`); in a world a list holds, `N` is
  the list's length (`held_learner_rests`), and on a lasso course the rest that
  `Becoming.Learning` leaves unrefuted is found (`rests_of_lasso`). The step is a function of
  the bound, which the learner does not have: its record does not show it.
* **A world answering its own learner exceeds the bound.** The course that answers every claim
  of the learner given `N` has more than `N` states (`answer_exceeds_bound`): a world that
  includes the learner and answers it is not within the bound the learner is given.
* **The split that makes sense, named with no quotient.** In a world a list holds, under a
  determined law, two configurations have the same registered future exactly where their
  registered futures agree before `2N - 1` (`Law.sameFuture_iff_below`). Naming each
  configuration by its registered future before that step, a finite list, makes sense
  (`Law.name_identifiesAlike`); the names carry the law (`Law.name_carries`) and likeness is decided
  by comparing them (`Law.decideAlike`). Naming by the whole registered future would need
  function extensionality, which Lean proves from the quotient axiom `Quot.sound`; the bound
  makes the finite name enough. The states of a history with at most `N` states are read the same way
  (`sameAhead_iff_below`, `statesBelow_shift`).

The world in these statements is any world a list holds: a controller or a cognition inside it
is part of what is registered, as in `Becoming.Description`'s `Law.adaptive_identifiesAlike_iff`.
The bound `N + N' - 1` is the one of Fine and Wilf, and for two histories it is Moore's bound
(1956) for the two systems taken together, attained for every pair of bounds; the sharper bound
for two moments of one history, or two configurations of one world, is not stated here.
-/

namespace Becoming

open Generative

universe u v w

namespace Identification

/-! ## Two periods -/

section Periods

variable {O : Type u}

/-- Every step is a remainder up to `p` and a number of whole periods `p + 1`. -/
theorem residue (p : Nat) : ∀ n, ∃ r k, r ≤ p ∧ n = r + (p + 1) * k
  | 0 => ⟨0, 0, Nat.zero_le p, rfl⟩
  | n + 1 =>
    match residue p n with
    | ⟨r, k, le, at_n⟩ =>
      match Nat.lt_or_ge r p with
      | .inl lt => ⟨r + 1, k, lt,
          (congrArg Nat.succ at_n).trans (Nat.succ_add r ((p + 1) * k)).symm⟩
      | .inr ge =>
        have top : r = p := Nat.le_antisymm le ge
        ⟨0, k + 1, Nat.zero_le p,
          (congrArg Nat.succ at_n).trans ((Nat.succ_add r ((p + 1) * k)).symm.trans
            ((congrArg (fun m => m + 1 + (p + 1) * k) top).trans
              ((Nat.add_comm (p + 1) ((p + 1) * k)).trans
                (Nat.zero_add ((p + 1) * k + (p + 1))).symm)))⟩

/-- A course with period `p + 1` takes, after whole periods, the value it took. -/
theorem periodic_whole {x : Nat → O} {p : Nat} (per : ∀ n, x (n + (p + 1)) = x n) (r : Nat) :
    ∀ k, x (r + (p + 1) * k) = x r
  | 0 => rfl
  | k + 1 =>
    (congrArg x (Nat.add_assoc r ((p + 1) * k) (p + 1)).symm).trans
      ((per (r + (p + 1) * k)).trans (periodic_whole per r k))

/-- **Two periods (Fine and Wilf).** A course with period `p + 1` that comes back after `Q`
steps at each of its first `p` steps comes back after `Q` steps at every step. The remainders
of `p + Q, p + 2Q, …` walk through one cycle; the one step not given, at `p`, is passed round
the rest of the cycle. -/
theorem period_extends {x : Nat → O} {p Q : Nat} (per : ∀ n, x (n + (p + 1)) = x n)
    (first : ∀ n, n < p → x (n + Q) = x n) : ∀ n, x (n + Q) = x n := by
  have walk : ∀ t, ∃ r k, r ≤ p ∧ p + Q * (t + 1) = r + (p + 1) * k ∧
      (x (p + Q) = x p ∨ x (p + Q) = x r) := by
    intro t
    induction t with
    | zero =>
      match residue p (p + Q) with
      | ⟨r, k, le, at_pQ⟩ =>
        exact ⟨r, k, le, (congrArg (p + ·) (Nat.mul_one Q)).trans at_pQ,
          Or.inr ((congrArg x at_pQ).trans (periodic_whole per r k))⟩
    | succ t ih =>
      match ih with
      | ⟨r, k, le, at_t, said⟩ =>
        have step : p + Q * (t + 1 + 1) = r + Q + (p + 1) * k :=
          (Nat.add_assoc p (Q * (t + 1)) Q).symm.trans
            ((congrArg (· + Q) at_t).trans (Nat.add_right_comm r ((p + 1) * k) Q))
        match residue p (r + Q) with
        | ⟨r', k', le', at_rQ⟩ =>
          have next : p + Q * (t + 1 + 1) = r' + (p + 1) * (k' + k) :=
            step.trans ((congrArg (· + (p + 1) * k) at_rQ).trans
              ((Nat.add_assoc r' ((p + 1) * k') ((p + 1) * k)).trans
                (congrArg (r' + ·) (Nat.left_distrib (p + 1) k' k).symm)))
          have moved : x r' = x (r + Q) :=
            (periodic_whole per r' k').symm.trans (congrArg x at_rQ.symm)
          match Nat.decEq r p with
          | isTrue at_p =>
            exact ⟨r', k' + k, le', next, Or.inl (match said with
              | .inl done => done
              | .inr to_r => to_r.trans (congrArg x at_p))⟩
          | isFalse off =>
            have kept : x r' = x r := moved.trans (first r (Nat.lt_of_le_of_ne le off))
            exact ⟨r', k' + k, le', next, match said with
              | .inl done => Or.inl done
              | .inr to_r => Or.inr (to_r.trans kept.symm)⟩
  have back : x (p + Q) = x p :=
    match walk p with
    | ⟨r, k, _, at_end, said⟩ =>
      have closes : x r = x p :=
        (periodic_whole per r k).symm.trans ((congrArg x at_end.symm).trans
          ((congrArg (fun m => x (p + m)) (Nat.mul_comm Q (p + 1))).trans
            (periodic_whole per p Q)))
      match said with
      | .inl done => done
      | .inr to_r => to_r.trans closes
  intro n
  match residue p n with
  | ⟨r, k, le, at_n⟩ =>
    have at_r : x (r + Q) = x r :=
      match Nat.decEq r p with
      | isTrue at_p => Eq.subst (motive := fun m => x (m + Q) = x m) at_p.symm back
      | isFalse off => first r (Nat.lt_of_le_of_ne le off)
    calc x (n + Q) = x (r + Q + (p + 1) * k) :=
          congrArg x ((congrArg (· + Q) at_n).trans (Nat.add_right_comm r ((p + 1) * k) Q))
      _ = x (r + Q) := periodic_whole per (r + Q) k
      _ = x r := at_r
      _ = x n := (periodic_whole per r k).symm.trans (congrArg x at_n.symm)

/-- **Two lassos that agree long enough agree at every step.** Courses repeating from steps
`i`, `i'` with periods `q + 1`, `q' + 1` that agree before `(i + q + 1) + (i' + q')` agree at
every step. -/
theorem lassos_agree {o o' : Nat → O} {i q i' q' : Nat} (lasso : Learning.Lasso o i q)
    (lasso' : Learning.Lasso o' i' q')
    (agree : ∀ n, n < (i + q + 1) + (i' + q') → o n = o' n) : ∀ n, o n = o' n := by
  have shuffle : i + i' + (q + q' + 1) = (i + q + 1) + (i' + q') :=
    ((congrArg (i + i' + ·) (Nat.succ_add q q')).symm.trans
      (Nat.add_add_add_comm i i' (q + 1) q')).trans
      (congrArg (· + (i' + q')) (rfl : i + (q + 1) = i + q + 1))
  have per : ∀ n, o (i + i' + n + (q + 1)) = o (i + i' + n) := fun n =>
    lasso (i + i' + n) (Nat.le_trans (Nat.le_add_right i i') (Nat.le_add_right _ n))
  have per' : ∀ n, o' (i + i' + n + (q' + 1)) = o' (i + i' + n) := fun n =>
    lasso' (i + i' + n) (Nat.le_trans (Nat.le_add_left i' i) (Nat.le_add_right _ n))
  have perx : ∀ n, o (i + i' + (n + (q + 1))) = o (i + i' + n) := fun n =>
    (congrArg o (Nat.add_assoc (i + i') n (q + 1)).symm).trans (per n)
  have pery : ∀ n, o' (i + i' + (n + (q' + 1))) = o' (i + i' + n) := fun n =>
    (congrArg o' (Nat.add_assoc (i + i') n (q' + 1)).symm).trans (per' n)
  have early : ∀ n, n < q + q' + 1 → o (i + i' + n) = o' (i + i' + n) := fun n lt =>
    agree _ (Eq.subst (motive := fun m => i + i' + n < m) shuffle (Nat.add_lt_add_left lt _))
  have comes_back : ∀ n, o (i + i' + (n + (q' + 1))) = o (i + i' + n) :=
    period_extends (x := fun n => o (i + i' + n)) perx fun n lt =>
      (early (n + (q' + 1)) (Nat.add_lt_add_right lt (q' + 1))).trans
        ((pery n).trans (early n (Nat.lt_of_lt_of_le lt
          (Nat.le_trans (Nat.le_add_right q q') (Nat.le_succ _)))).symm)
  have late : ∀ n, o (i + i' + n) = o' (i + i' + n) := fun n =>
    match residue q' n with
    | ⟨r, k, le, at_n⟩ =>
      (congrArg (fun m => o (i + i' + m)) at_n).trans
        ((periodic_whole (x := fun n => o (i + i' + n)) comes_back r k).trans
          ((early r (Nat.lt_of_lt_of_le (Nat.lt_succ_of_le le)
            (Nat.succ_le_succ (Nat.le_add_left q' q)))).trans
            ((periodic_whole (x := fun n => o' (i + i' + n)) pery r k).symm.trans
              (congrArg (fun m => o' (i + i' + m)) at_n.symm))))
  intro n
  match Nat.lt_or_ge n (i + i') with
  | .inl before =>
    exact agree n (Nat.lt_of_lt_of_le before
      (Nat.add_le_add (Nat.le_add_right i (q + 1)) (Nat.le_add_right i' q')))
  | .inr after =>
    match gap_of_le after with
    | ⟨d, at_n⟩ => exact (congrArg o at_n).trans ((late d).trans (congrArg o' at_n.symm))

end Periods

/-! ## Strong induction and the lasso world -/

section Positions

/-- Strong induction, from the steps before each step. -/
theorem below_upto {P : Nat → Prop} (step : ∀ m, (∀ n, n < m → P n) → P m) :
    ∀ m n, n < m → P n
  | 0, n, lt => absurd lt (Nat.not_lt_zero n)
  | m + 1, n, lt =>
    step n fun k before => below_upto step m k (Nat.lt_of_lt_of_le before (Nat.le_of_lt_succ lt))

theorem below_all {P : Nat → Prop} (step : ∀ m, (∀ n, n < m → P n) → P m) : ∀ n, P n :=
  fun n => below_upto step (n + 1) n (Nat.lt_succ_self n)

/-- Along `Becoming.Learning`'s lasso world, the position is the step up to `i + q`. -/
theorem lassoPos_early {i q : Nat} :
    ∀ n, n ≤ i + q → Law.orbit (Learning.lassoNext i q) 0 n = n
  | 0, _ => rfl
  | n + 1, le =>
    (congrArg (Learning.lassoNext i q) (lassoPos_early n (Nat.le_of_succ_le le))).trans
      (if_pos (Nat.lt_of_succ_le le))

/-- From `i` on, the lasso world's position comes back after `q + 1` steps. -/
theorem lassoPos_period {i q : Nat} :
    ∀ d, Law.orbit (Learning.lassoNext i q) 0 (i + d + (q + 1)) =
      Law.orbit (Learning.lassoNext i q) 0 (i + d)
  | 0 =>
    (congrArg (Learning.lassoNext i q) (lassoPos_early (i + q) (Nat.le_refl _))).trans
      ((if_neg (Nat.lt_irrefl (i + q))).trans (lassoPos_early i (Nat.le_add_right i q)).symm)
  | d + 1 =>
    (congrArg (Law.orbit (Learning.lassoNext i q) 0)
      (Nat.add_right_comm (i + d) 1 (q + 1))).trans
      (congrArg (Learning.lassoNext i q) (lassoPos_period d))

end Positions

/-! ## What a bounded record fixes -/

section Bounded

variable {O : Type u}

/-- Fewer states before a smaller bound are fewer before a larger one. -/
theorem statesBelow_mono {o : Nat → O} {L N : Nat} (below : StatesBelow o L) (le : L ≤ N) :
    StatesBelow o N :=
  fun t => match below t with
    | ⟨i, lt, same⟩ => ⟨i, Nat.lt_of_lt_of_le lt le, same⟩

/-- **A history has at most `N` states exactly where it repeats from some step `i` with some
period `q + 1`, `i + q + 1 ≤ N`.** The bounded form of `finitely_many_states_iff` and of
`finitely_many_states_iff_lasso`. -/
theorem statesBelow_iff_lasso {o : Nat → O} {N : Nat} :
    StatesBelow o N ↔ ∃ i q, i + q + 1 ≤ N ∧ Learning.Lasso o i q :=
  ⟨fun below =>
    match shared_below N (fun t i => SameAhead o t i) (fun n _ => below n) with
    | ⟨t, _, _, lt, le, h, h'⟩ =>
      match gap_of_lt lt with
      | ⟨q, at_t'⟩ =>
        ⟨t, q, Eq.subst (motive := fun n => n ≤ N) at_t' le,
          lasso_iff_sameAhead.mpr
            (Eq.subst (motive := fun n => SameAhead o t n) at_t' (h.trans h'.symm))⟩,
   fun ⟨i, q, within, lasso⟩ =>
    statesBelow_mono
      (statesBelow_of_same (Nat.lt_succ_of_le (Nat.le_add_right i q))
        (lasso_iff_sameAhead.mp lasso)) within⟩

/-- A history with at most `N` states has a state: the bound is at least one. -/
theorem statesBelow_pos {o : Nat → O} {N : Nat} (below : StatesBelow o N) : 0 < N :=
  match below 0 with
  | ⟨_, lt, _⟩ => Nat.lt_of_le_of_lt (Nat.zero_le _) lt

/-- A positive bound is at most twice itself less one. -/
theorem le_twice_less_one : ∀ {N : Nat}, 0 < N → N ≤ N + N - 1
  | 0, lt => absurd lt (Nat.lt_irrefl 0)
  | m + 1, _ => Nat.le_add_right (m + 1) m

/-- **Two bounded histories are fixed by their agreement before `N + N' - 1`.** -/
theorem bounded_agree {o o' : Nat → O} {N N' : Nat} (bound : StatesBelow o N)
    (bound' : StatesBelow o' N') (agree : ∀ n, n < N + N' - 1 → o n = o' n) :
    ∀ n, o n = o' n :=
  match statesBelow_iff_lasso.mp bound, statesBelow_iff_lasso.mp bound' with
  | ⟨i, q, within, lasso⟩, ⟨i', q', within', lasso'⟩ =>
    have short : (i + q + 1) + (i' + q') ≤ N + N' - 1 :=
      Nat.sub_le_sub_right (Nat.add_le_add within within') 1
    lassos_agree lasso lasso' fun n lt => agree n (Nat.lt_of_lt_of_le lt short)

/-- **Records are equal exactly where the courses agree before their length.** -/
theorem record_eq_iff {o o' : Nat → O} : ∀ {T : Nat},
    Learning.record o T = Learning.record o' T ↔ ∀ n, n < T → o n = o' n
  | 0 => ⟨fun _ n lt => absurd lt (Nat.not_lt_zero n), fun _ => rfl⟩
  | T + 1 =>
    ⟨fun same n lt =>
      match List.cons.inj
          (show o T :: Learning.record o T = o' T :: Learning.record o' T from same) with
      | ⟨now, before⟩ =>
        match Nat.lt_or_ge n T with
        | .inl lt' => record_eq_iff.mp before n lt'
        | .inr ge =>
          have at_T : n = T := Nat.le_antisymm (Nat.le_of_lt_succ lt) ge
          (congrArg o at_T).trans (now.trans (congrArg o' at_T).symm),
     Learning.record_congr⟩

/-- **The record before `N + N' - 1` fixes a history with at most `N` states among those with at
most `N'`.** -/
theorem record_fixes {o o' : Nat → O} {N N' : Nat} (bound : StatesBelow o N)
    (bound' : StatesBelow o' N')
    (same : Learning.record o (N + N' - 1) = Learning.record o' (N + N' - 1)) :
    ∀ n, o n = o' n :=
  bounded_agree bound bound' (record_eq_iff.mp same)

/-- **The record before `N + N' - 2` does not.** For every `T`, given two values, a history
with one state and one with at most `T + 1` share their record before `T` and differ at `T`
(`Becoming.Learning`'s `holdFrom`). -/
theorem record_short {x y : O} (two : x ≠ y) (T : Nat) :
    ∃ o o' : Nat → O, StatesBelow o 1 ∧ StatesBelow o' (T + 1) ∧
      Learning.record o T = Learning.record o' T ∧ o T ≠ o' T :=
  ⟨fun _ => x, Learning.holdFrom (fun _ => x) T y,
   statesBelow_iff_lasso.mpr ⟨0, 0, Nat.le_refl 1, fun _ _ => rfl⟩,
   statesBelow_iff_lasso.mpr ⟨T, 0, Nat.le_refl (T + 1), Learning.holdFrom_lasso _ T y⟩,
   Learning.record_congr fun _ before => (Learning.holdFrom_before (fun _ => x) y before).symm,
   fun same => two (same.trans (Learning.holdFrom_after _ y (Nat.le_refl T)))⟩

/-- The course of `Becoming.Learning`'s lasso world on positions `0, …, i + q` that registers `y`
at position `m` and `x` elsewhere. -/
def mark (i q m : Nat) (x y : O) (n : Nat) : O :=
  if Law.orbit (Learning.lassoNext i q) 0 n = m then y else x

/-- **For two histories with at most `N` states each, the record before `N + N - 2` does not fix
the course.** With `N = M + 2`: the course marking every `N`-th step from step `M + 1`, and the
course marking every `(N - 1)`-th step from step `M + 1`, share their record before `M + M + 2`
and differ at it. So `N + N - 1` is exact for two histories with the same bound. -/
theorem record_short_twice {x y : O} (two : x ≠ y) (M : Nat) :
    ∃ o o' : Nat → O, StatesBelow o (M + 2) ∧ StatesBelow o' (M + 2) ∧
      Learning.record o (M + M + 2) = Learning.record o' (M + M + 2) ∧
        o (M + M + 2) ≠ o' (M + M + 2) := by
  let pos := Law.orbit (Learning.lassoNext 0 (M + 1)) 0
  let pos' := Law.orbit (Learning.lassoNext 1 M) 0
  have early : ∀ n, n ≤ M + 1 → pos n = n := fun n le =>
    lassoPos_early (i := 0) (q := M + 1) n
      (Eq.subst (motive := fun k => n ≤ k) (Nat.zero_add (M + 1)).symm le)
  have early' : ∀ n, n ≤ M + 1 → pos' n = n := fun n le =>
    lassoPos_early (i := 1) (q := M) n
      (Eq.subst (motive := fun k => n ≤ k) (Nat.add_comm M 1) le)
  have period : ∀ u, pos (u + (M + 2)) = pos u := fun u =>
    Eq.subst (motive := fun k => pos (k + (M + 2)) = pos k) (Nat.zero_add u)
      (lassoPos_period (i := 0) (q := M + 1) u)
  have period' : ∀ d, pos' (1 + d + (M + 1)) = pos' (1 + d) := fun d =>
    lassoPos_period (i := 1) (q := M) d
  have later : ∀ d, d ≤ M → pos (M + 2 + d) = d ∧ pos' (M + 2 + d) = 1 + d := fun d le =>
    have at_n : M + 2 + d = 1 + d + (M + 1) :=
      (Nat.add_assoc (M + 1) 1 d).trans (Nat.add_comm (M + 1) (1 + d))
    ⟨(congrArg pos (Nat.add_comm (M + 2) d)).trans
        ((period d).trans (early d (Nat.le_succ_of_le le))),
     (congrArg pos' at_n).trans ((period' d).trans
        (early' (1 + d) (Eq.subst (motive := fun k => 1 + d ≤ k) (Nat.add_comm 1 M)
          (Nat.add_le_add_left le 1))))⟩
  have twice : M + M + 2 = M + 2 + M :=
    (Nat.add_assoc M M 2).trans (Nat.add_comm M (M + 2))
  let o : Nat → O := mark 0 (M + 1) (M + 1) x y
  let o' : Nat → O := mark 1 M (M + 1) x y
  have lasso : Learning.Lasso o 0 (M + 1) := fun u _ =>
    congrArg (fun k => if k = M + 1 then y else x) (period u)
  have lasso' : Learning.Lasso o' 1 M := fun u le =>
    match gap_of_le le with
    | ⟨d, at_u⟩ =>
      congrArg (fun k => if k = M + 1 then y else x)
        ((congrArg (fun n => pos' (n + (M + 1))) at_u).trans
          ((period' d).trans (congrArg pos' at_u.symm)))
  have agree : ∀ n, n < M + M + 2 → o n = o' n := fun n lt =>
    match Nat.lt_or_ge n (M + 2) with
    | .inl first =>
      have le : n ≤ M + 1 := Nat.le_of_lt_succ first
      congrArg (fun k => if k = M + 1 then y else x) ((early n le).trans (early' n le).symm)
    | .inr beyond =>
      match gap_of_le beyond with
      | ⟨d, at_n⟩ =>
        have short : d < M :=
          Nat.lt_of_add_lt_add_left
            (Eq.subst (motive := fun k => k < M + 2 + M) at_n
              (Eq.subst (motive := fun k => n < k) twice lt))
        have off : pos n ≠ M + 1 := fun same =>
          have at_d : d = M + 1 :=
            (later d (Nat.le_of_lt short)).1.symm.trans ((congrArg pos at_n).symm.trans same)
          Nat.lt_irrefl M (Nat.lt_trans (Nat.lt_succ_self M)
            (Eq.subst (motive := fun k => k < M) at_d short))
        have off' : pos' n ≠ M + 1 := fun same =>
          have at_d : 1 + d = M + 1 :=
            (later d (Nat.le_of_lt short)).2.symm.trans ((congrArg pos' at_n).symm.trans same)
          Nat.lt_irrefl M (Eq.subst (motive := fun k => k < M)
            (Nat.succ.inj ((Nat.add_comm d 1).trans at_d)) short)
        (if_neg off).trans (if_neg off').symm
  have at_end := later M (Nat.le_refl M)
  have left : o (M + M + 2) = x :=
    if_neg fun same => Nat.succ_ne_self M
      (at_end.1.symm.trans ((congrArg pos twice).symm.trans same)).symm
  have right : o' (M + M + 2) = y :=
    if_pos (((congrArg pos' twice).trans at_end.2).trans (Nat.add_comm 1 M))
  exact ⟨o, o',
    statesBelow_iff_lasso.mpr
      ⟨0, M + 1, Nat.le_of_eq (congrArg (· + 1) (Nat.zero_add (M + 1))), lasso⟩,
    statesBelow_iff_lasso.mpr ⟨1, M, Nat.le_of_eq (congrArg (· + 1) (Nat.add_comm 1 M)), lasso'⟩,
    record_eq_iff.mpr agree,
    fun same => two (left.symm.trans (same.trans right))⟩

/-- **The length `N + N' - 1` is exact for every pair of bounds.** Given two values, for all `M`
and `M'`, a history with at most `M + 1` states and one with at most `M' + 1` share their record
before `M + M'` and differ at `M + M'`. The first marks every `(M + 1)`-th step, placed so that
the steps from `M'` to `M + M' - 1` are unmarked and step `M + M'` is marked; the second
follows it before step `M'` and stays unmarked from then on. With `M = 0` this is
`record_short`; with `M = M'` it is the case `N = N'` of `record_short_twice`. -/
theorem bounded_agree_exact {x y : O} (two : x ≠ y) (M M' : Nat) :
    ∃ o o' : Nat → O, StatesBelow o (M + 1) ∧ StatesBelow o' (M' + 1) ∧
      Learning.record o (M + M') = Learning.record o' (M + M') ∧ o (M + M') ≠ o' (M + M') := by
  let pos := Law.orbit (Learning.lassoNext 0 M) 0
  have early : ∀ j, j ≤ M → pos j = j := fun j le =>
    lassoPos_early (i := 0) (q := M) j
      (Eq.subst (motive := fun k => j ≤ k) (Nat.zero_add M).symm le)
  have period : ∀ u, pos (u + (M + 1)) = pos u := fun u =>
    Eq.subst (motive := fun k => pos (k + (M + 1)) = pos k) (Nat.zero_add u)
      (lassoPos_period (i := 0) (q := M) u)
  have placed : ∀ j, j ≤ M → pos (M' + j + M * M') = j := fun j le =>
    (congrArg pos ((congrArg (· + M * M') (Nat.add_comm M' j)).trans
      ((Nat.add_assoc j M' (M * M')).trans (congrArg (j + ·)
        ((Nat.add_comm M' (M * M')).trans (Nat.succ_mul M M').symm))))).trans
      ((periodic_whole (x := pos) period j M').trans (early j le))
  let o : Nat → O := fun n => mark 0 M M x y (n + M * M')
  let o' : Nat → O := Learning.holdFrom o M' x
  have lasso : Learning.Lasso o 0 M := fun u _ =>
    congrArg (fun k => if k = M then y else x)
      ((congrArg pos (Nat.add_right_comm u (M + 1) (M * M'))).trans (period (u + M * M')))
  have agree : ∀ n, n < M + M' → o n = o' n := fun n lt =>
    match Nat.lt_or_ge n M' with
    | .inl before => (Learning.holdFrom_before o x before).symm
    | .inr after =>
      match gap_of_le after with
      | ⟨j, at_n⟩ =>
        have short : j < M :=
          Nat.lt_of_add_lt_add_left
            (Eq.subst (motive := fun k => k < M' + M) at_n
              (Eq.subst (motive := fun k => n < k) (Nat.add_comm M M') lt))
        have unmarked : o n = x := if_neg fun marked =>
          Nat.ne_of_lt short ((placed j (Nat.le_of_lt short)).symm.trans
            ((congrArg (fun k => pos (k + M * M')) at_n).symm.trans marked))
        unmarked.trans (Learning.holdFrom_after o x after).symm
  have marked : o (M + M') = y :=
    if_pos ((congrArg (fun k => pos (k + M * M')) (Nat.add_comm M M')).trans
      (placed M (Nat.le_refl M)))
  have stays : o' (M + M') = x := Learning.holdFrom_after o x (Nat.le_add_left M' M)
  exact ⟨o, o',
    statesBelow_iff_lasso.mpr ⟨0, M, Nat.le_of_eq (congrArg (· + 1) (Nat.zero_add M)), lasso⟩,
    statesBelow_iff_lasso.mpr ⟨M', 0, Nat.le_refl (M' + 1), Learning.holdFrom_lasso o M' x⟩,
    record_eq_iff.mpr agree,
    fun same => two (stays.symm.trans (same.symm.trans marked))⟩

/-- A later stretch of a history with at most `N` states has at most `N` states. -/
theorem statesBelow_shift {o : Nat → O} {N : Nat} (bound : StatesBelow o N) (t : Nat) :
    StatesBelow (fun n => o (t + n)) N :=
  match statesBelow_iff_lasso.mp bound with
  | ⟨i, q, within, lasso⟩ =>
    statesBelow_iff_lasso.mpr ⟨i, q, within, fun u later =>
      (congrArg o (Nat.add_assoc t u (q + 1)).symm).trans
        (lasso (t + u) (Nat.le_trans later (Nat.le_add_left u t)))⟩

/-- **The states of a bounded history are read off a finite record.** Two moments of a history
with at most `N` states are one state exactly where what is registered from them agrees for
`N + N - 1` steps. -/
theorem sameAhead_iff_below {o : Nat → O} {N : Nat} (bound : StatesBelow o N) {t t' : Nat} :
    SameAhead o t t' ↔ ∀ n, n < N + N - 1 → o (t + n) = o (t' + n) :=
  ⟨fun same n _ => same n,
   fun agree => bounded_agree (statesBelow_shift bound t) (statesBelow_shift bound t') agree⟩

end Bounded

/-! ## Induction where the bound is given -/

section Induction

variable {O : Type u}

/-- **With the bound given, a hypothesis the record bears out is the law of the course.** On a
history with at most `N` states, a lasso `(i, q)` within `N` that holds on the record before
`N + N - 1` holds at every step. The lasso world reading the record is a second history within
`N` agreeing with the first before `N + N - 1`. -/
theorem lasso_of_fits {o : Nat → O} {N i q : Nat} (bound : StatesBelow o N)
    (within : i + q + 1 ≤ N)
    (fits : ∀ u, i ≤ u → u + (q + 1) < N + N - 1 → o (u + (q + 1)) = o u) :
    Learning.Lasso o i q := by
  let pos := Law.orbit (Learning.lassoNext i q) 0
  have lasso : Learning.Lasso (fun n => o (pos n)) i q := fun u le =>
    match gap_of_le le with
    | ⟨d, at_u⟩ =>
      congrArg o ((congrArg (fun n => pos (n + (q + 1))) at_u).trans
        ((lassoPos_period d).trans (congrArg pos at_u.symm)))
  have agree : ∀ n, n < N + N - 1 → o (pos n) = o n := below_all fun m before lt =>
    match Nat.lt_or_ge m (i + q + 1) with
    | .inl early => congrArg o (lassoPos_early m (Nat.le_of_lt_succ early))
    | .inr late =>
      match gap_of_le late with
      | ⟨d, at_m⟩ =>
        have at_m' : m = i + d + (q + 1) := at_m.trans (Nat.add_right_comm i (q + 1) d)
        have u_lt : i + d < m :=
          Eq.subst (motive := fun k => i + d < k) at_m'.symm
            (Nat.lt_succ_of_le (Nat.le_add_right (i + d) q))
        (congrArg (fun k => o (pos k)) at_m').trans
          ((lasso (i + d) (Nat.le_add_right i d)).trans
            ((before (i + d) u_lt (Nat.lt_trans u_lt lt)).trans
              ((fits (i + d) (Nat.le_add_right i d)
                (Eq.subst (motive := fun k => k < N + N - 1) at_m' lt)).symm.trans
                (congrArg o at_m'.symm))))
  have all : ∀ n, o (pos n) = o n :=
    bounded_agree (statesBelow_iff_lasso.mpr ⟨i, q, within, lasso⟩) bound agree
  exact fun u le => (all _).symm.trans ((lasso u le).trans (all u))

/-- A lasso hypothesis refuted at no step before `T` holds on the record before `T`. -/
theorem fits_of_unrefuted [DecidableEq O] {o : Nat → O} {i q T : Nat}
    (unrefuted : ∀ t, t < T → ¬ Learning.RefutedAt (Learning.lasso (i, q)) o t) :
    ∀ u, i ≤ u → u + (q + 1) < T → o (u + (q + 1)) = o u :=
  fun u le lt =>
    have claims : Learning.lasso (i, q) (Learning.record o (u + (q + 1))) = some (o u) :=
      (Learning.lasso_claims (o := o) (h := (i, q)) (Nat.add_le_add_right le (q + 1))).trans
        (Learning.back_record o u q)
    (Learning.eq_of_not_refuted
      (Eq.subst (motive := fun c => ¬ Learning.Refuted c (o (u + (q + 1)))) claims
        (unrefuted _ lt))).symm

/-- **In a bounded situation induction is deduction.** On a history with at most `N` states, a
lasso hypothesis within `N` refuted at no step before `N + N - 1` is refuted at no step. -/
theorem bounded_induction [DecidableEq O] {o : Nat → O} {N i q : Nat}
    (bound : StatesBelow o N) (within : i + q + 1 ≤ N)
    (unrefuted : ∀ t, t < N + N - 1 → ¬ Learning.RefutedAt (Learning.lasso (i, q)) o t) :
    Learning.Holds (Learning.lasso (i, q)) o :=
  Learning.lasso_holds (lasso_of_fits bound within (fits_of_unrefuted unrefuted))

/-- On a history with at most `N` states some lasso hypothesis within `N` holds. -/
theorem bounded_hypothesis {o : Nat → O} {N : Nat} (bound : StatesBelow o N) :
    ∃ i q, i + q + 1 ≤ N ∧ Learning.Holds (Learning.lasso (i, q)) o :=
  match statesBelow_iff_lasso.mp bound with
  | ⟨i, q, within, lasso⟩ => ⟨i, q, within, Learning.lasso_holds lasso⟩

end Induction

/-! ## The learner given the bound -/

section WithBound

variable {O : Type u}

/-- Every claim of `pred` on a record, each made from the record before it, is borne out. -/
def BorneOut (pred : List O → Option O) : List O → Prop
  | [] => True
  | v :: l => ¬ Learning.Refuted (pred l) v ∧ BorneOut pred l

instance decBorneOut [DecidableEq O] (pred : List O → Option O) :
    (l : List O) → Decidable (BorneOut pred l)
  | [] => isTrue trivial
  | v :: l =>
    match Learning.decRefuted (pred l) v, decBorneOut pred l with
    | isTrue refuted, _ => isFalse fun ⟨unrefuted, _⟩ => unrefuted refuted
    | isFalse unrefuted, isTrue borne => isTrue ⟨unrefuted, borne⟩
    | isFalse _, isFalse unborne => isFalse fun ⟨_, borne⟩ => unborne borne

/-- A record bears out `pred` exactly where `pred` is refuted at no step before its length. -/
theorem borneOut_record_iff {pred : List O → Option O} {o : Nat → O} : ∀ {T : Nat},
    BorneOut pred (Learning.record o T) ↔ ∀ t, t < T → ¬ Learning.RefutedAt pred o t
  | 0 => ⟨fun _ t lt => absurd lt (Nat.not_lt_zero t), fun _ => trivial⟩
  | T + 1 =>
    ⟨fun ⟨now, before⟩ t lt =>
      match Nat.lt_or_ge t T with
      | .inl lt' => borneOut_record_iff.mp before t lt'
      | .inr ge =>
        Eq.subst (motive := fun s => ¬ Learning.RefutedAt pred o s)
          (Nat.le_antisymm ge (Nat.le_of_lt_succ lt)) now,
     fun all => ⟨all T (Nat.lt_succ_self T),
       borneOut_record_iff.mpr fun t lt => all t (Nat.lt_succ_of_lt lt)⟩⟩

/-- The pairs `(i, q)` with `q < Q`, for one `i`. -/
def column (i : Nat) : Nat → List (Nat × Nat)
  | 0 => []
  | Q + 1 => (i, Q) :: column i Q

/-- The pairs `(i, q)` with `i < I` and `q < Q`. -/
def grid (Q : Nat) : Nat → List (Nat × Nat)
  | 0 => []
  | I + 1 => column I Q ++ grid Q I

theorem mem_column {i q : Nat} : ∀ {Q : Nat}, q < Q → (i, q) ∈ column i Q
  | 0, lt => absurd lt (Nat.not_lt_zero q)
  | Q + 1, lt =>
    match Nat.lt_or_ge q Q with
    | .inl lt' => List.Mem.tail _ (mem_column lt')
    | .inr ge =>
      Eq.subst (motive := fun k => (i, k) ∈ column i (Q + 1))
        (Nat.le_antisymm ge (Nat.le_of_lt_succ lt)) (List.Mem.head _)

theorem mem_grid {i q Q : Nat} (lt_q : q < Q) : ∀ {I : Nat}, i < I → (i, q) ∈ grid Q I
  | 0, lt => absurd lt (Nat.not_lt_zero i)
  | I + 1, lt =>
    match Nat.lt_or_ge i I with
    | .inl lt' => List.mem_append_right _ (mem_grid lt_q lt')
    | .inr ge =>
      List.mem_append_left _
        (Eq.subst (motive := fun k => (i, q) ∈ column k Q)
          (Nat.le_antisymm (Nat.le_of_lt_succ lt) ge) (mem_column lt_q))

/-- The first member of a list meeting a decided condition. -/
def firstFit {α : Type} (p : α → Prop) (dec : ∀ a, Decidable (p a)) : List α → Option α
  | [] => none
  | a :: l => if p a then some a else firstFit p dec l

theorem firstFit_sound {α : Type} {p : α → Prop} {dec : ∀ a, Decidable (p a)} :
    ∀ {l : List α} {a : α}, firstFit p dec l = some a → p a
  | [], _, found => nomatch found
  | b :: l, _, found =>
    match Decidable.em (p b) with
    | .inl pb => Eq.subst (motive := p) (Option.some.inj ((if_pos pb).symm.trans found)) pb
    | .inr npb => firstFit_sound (l := l) ((if_neg npb).symm.trans found)

theorem firstFit_found {α : Type} {p : α → Prop} {dec : ∀ a, Decidable (p a)} :
    ∀ {l : List α} {a : α}, a ∈ l → p a → ∃ b, firstFit p dec l = some b
  | [], _, mem, _ => nomatch mem
  | b :: _, a, mem, pa =>
    match Decidable.em (p b) with
    | .inl pb => ⟨b, if_pos pb⟩
    | .inr npb =>
      match a, mem, pa with
      | _, .head _, pa => absurd pa npb
      | _, .tail _ mem', pa =>
        match firstFit_found (dec := dec) mem' pa with
        | ⟨c, found⟩ => ⟨c, (if_neg npb).trans found⟩

/-- The condition the learner given `N` puts on a hypothesis: within `N`, and borne out by
the record. -/
def Fits (N : Nat) (l : List O) (h : Nat × Nat) : Prop :=
  h.1 + h.2 + 1 ≤ N ∧ BorneOut (Learning.lasso h) l

instance decFits [DecidableEq O] (N : Nat) (l : List O) (h : Nat × Nat) :
    Decidable (Fits N l h) :=
  instDecidableAnd

/-- The claim made by a hypothesis, if one is held. -/
def claimBy (l : List O) : Option (Nat × Nat) → Option O
  | some h => Learning.lasso h l
  | none => none

/-- **The learner given the bound `N`.** Silent before step `N + N - 1`; from then on it
claims by the first lasso hypothesis within `N` that the record bears out. -/
def withBound [DecidableEq O] (N : Nat) (l : List O) : Option O :=
  if N + N - 1 ≤ l.length then claimBy l (firstFit (Fits N l) (decFits N l) (grid N N))
  else none

/-- **The learner given the bound is right at every step from `N + N - 1` on** of every
history with at most `N` states. -/
theorem withBound_exact [DecidableEq O] {o : Nat → O} {N t : Nat} (bound : StatesBelow o N)
    (late : N + N - 1 ≤ t) : withBound N (Learning.record o t) = some (o t) :=
  have long : N + N - 1 ≤ (Learning.record o t).length :=
    Eq.subst (motive := fun n => N + N - 1 ≤ n) (Learning.record_length o t).symm late
  have N_le : N ≤ N + N - 1 := le_twice_less_one (statesBelow_pos bound)
  match bounded_hypothesis bound with
  | ⟨i, q, within, holds⟩ =>
    have true_fits : Fits N (Learning.record o t) (i, q) :=
      ⟨within, borneOut_record_iff.mpr fun t' _ => holds t'⟩
    have member : (i, q) ∈ grid N N :=
      mem_grid (Nat.lt_of_lt_of_le (Nat.lt_succ_of_le (Nat.le_add_left q i)) within)
        (Nat.lt_of_lt_of_le (Nat.lt_succ_of_le (Nat.le_add_right i q)) within)
    match firstFit_found (dec := decFits N (Learning.record o t)) member true_fits with
    | ⟨(i', q'), found⟩ =>
      have fits : Fits N (Learning.record o t) (i', q') := firstFit_sound found
      have speaks : i' + q' + 1 ≤ t := Nat.le_trans fits.1 (Nat.le_trans N_le late)
      have holds' : Learning.Holds (Learning.lasso (i', q')) o :=
        bounded_induction bound fits.1 fun t' lt =>
          borneOut_record_iff.mp fits.2 t' (Nat.lt_of_lt_of_le lt late)
      match Learning.back_made o
          (Nat.lt_of_lt_of_le (Nat.lt_succ_of_le (Nat.le_add_left q' i')) speaks) with
      | ⟨v, at_back⟩ =>
        have value : Learning.lasso (i', q') (Learning.record o t) = some v :=
          (Learning.lasso_claims (o := o) (h := (i', q')) speaks).trans at_back
        have right : v = o t :=
          Learning.eq_of_not_refuted
            (Eq.subst (motive := fun c => ¬ Learning.Refuted c (o t)) value (holds' t))
        (if_pos long).trans ((congrArg (claimBy (Learning.record o t)) found).trans
          (value.trans (congrArg some right)))

/-- **The learner given the bound is refuted at no step** of any history with at most `N`
states. -/
theorem withBound_holds [DecidableEq O] {o : Nat → O} {N : Nat} (bound : StatesBelow o N) :
    Learning.Holds (withBound N) o := fun t =>
  match Nat.lt_or_ge t (N + N - 1) with
  | .inl early =>
    fun ⟨_, made, _⟩ =>
      nomatch (show withBound N (Learning.record o t) = none from
        if_neg fun long => Nat.lt_irrefl t (Nat.lt_of_lt_of_le early
          (Eq.subst (motive := fun n => N + N - 1 ≤ n) (Learning.record_length o t) long))
        ).symm.trans made
  | .inr late =>
    Eq.subst (motive := fun c => ¬ Learning.Refuted c (o t)) (withBound_exact bound late).symm
      Learning.not_refuted_self

/-- **No learner can always speak sooner.** Given two values, no learner refuted at no step of
every history with at most `M + 2` states claims at step `M + M + 2` on each of them; the
learner given the bound speaks from step `M + M + 3` on. -/
theorem withBound_earliest {x y : O} (two : x ≠ y) (pred : List O → Option O) (M : Nat) :
    ¬ ∀ o : Nat → O, StatesBelow o (M + 2) →
      Learning.Holds pred o ∧ ∃ w, pred (Learning.record o (M + M + 2)) = some w :=
  fun all =>
    match record_short_twice two M with
    | ⟨o, o', bound, bound', same, differ⟩ =>
      match all o bound, all o' bound' with
      | ⟨holds, w, claims⟩, ⟨holds', _, _⟩ =>
        have claims' : pred (Learning.record o' (M + M + 2)) = some w :=
          (congrArg pred same).symm.trans claims
        holds _ ⟨w, claims, fun right => holds' _ ⟨w, claims', fun right' =>
          differ (right.symm.trans right')⟩⟩

/-- **The liar's truth is derived.** The learner given that there are two states is right about
the two-valued negation at every step from `3` on: what no fixed value answers
(`Diagonal.revision_never_rests`) is a rhythm read off the record. -/
theorem negation_derived : ∀ t, 3 ≤ t →
    withBound 2 (Learning.record Negation.register t) = some (Negation.register t) :=
  fun _ late => withBound_exact (statesBelow_of_same (Nat.zero_lt_succ 1) Negation.zero_two) late

/-- **A world answering its own learner exceeds the bound the learner is given.** Where `other`
moves every value, the course that answers every claim of the learner given `N` has more
than `N` states. -/
theorem answer_exceeds_bound [DecidableEq O] {other : O → O} (moves : ∀ v, other v ≠ v)
    (x : O) (N : Nat) : ¬ StatesBelow (Learning.diagonal (withBound N) other x) N :=
  fun bound => Learning.diagonal_unrested (withBound N) moves x
    ⟨N + N - 1, fun _ late => withBound_exact bound late⟩

end WithBound

/-! ## The learner not given the bound rests within it -/

section Resting

variable {O : Type u} [DecidableEq O] {o : Nat → O}

/-- **A lasso hypothesis unrefuted for `N + N - 1` steps is refuted at no later step.** On a
history with at most `N` states, a lasso `(a, b)` within `N` refuted at no step from `s ≥ a`
to before `s + (N + N - 1)` is refuted at no step from `s` on: the stretch from `s` repeats with
period `b + 1` on its record before `N + N - 1`, so at every step (`lasso_of_fits`). -/
theorem unrefuted_persists {N a b s : Nat} (bound : StatesBelow o N) (within : a + b + 1 ≤ N)
    (from_s : a ≤ s)
    (window : ∀ t, s ≤ t → t < s + (N + N - 1) →
      ¬ Learning.RefutedAt (Learning.lasso (a, b)) o t) :
    ∀ t, s ≤ t → ¬ Learning.RefutedAt (Learning.lasso (a, b)) o t := by
  have period_le : b + 1 ≤ N + N - 1 :=
    Nat.le_trans (Nat.le_trans (Nat.succ_le_succ (Nat.le_add_left b a)) within)
      (le_twice_less_one (statesBelow_pos bound))
  have fits : ∀ u, 0 ≤ u → u + (b + 1) < N + N - 1 →
      o (s + (u + (b + 1))) = o (s + u) := fun u _ lt =>
    have at_t : s + (u + (b + 1)) = s + u + b + 1 :=
      (Nat.add_assoc s u (b + 1)).symm
    have claims : Learning.lasso (a, b) (Learning.record o (s + (u + (b + 1)))) =
        some (o (s + u)) :=
      (Learning.lasso_claims (o := o) (h := (a, b))
        (Eq.subst (motive := fun n => a + b + 1 ≤ n) at_t.symm
          (Nat.succ_le_succ (Nat.add_le_add_right
            (Nat.le_trans from_s (Nat.le_add_right s u)) b)))).trans
        ((congrArg (fun n => Learning.back (Learning.record o n) b) at_t).trans
          (Learning.back_record o (s + u) b))
    (Learning.eq_of_not_refuted
      (Eq.subst (motive := fun c => ¬ Learning.Refuted c (o (s + (u + (b + 1))))) claims
        (window _ (Nat.le_add_right s _) (Nat.add_lt_add_left lt s)))).symm
  have shifted : Learning.Lasso (fun n => o (s + n)) 0 b :=
    lasso_of_fits (statesBelow_shift bound s)
      (Nat.le_trans (Nat.le_of_eq (congrArg (· + 1) (Nat.zero_add b)))
        (Nat.le_trans (Nat.succ_le_succ (Nat.le_add_left b a)) within))
      fits
  have from_here : Learning.Lasso o s b := fun u le =>
    match gap_of_le le with
    | ⟨d, at_u⟩ =>
      (congrArg (fun n => o (n + (b + 1))) at_u).trans
        ((congrArg o (Nat.add_assoc s d (b + 1))).trans
          ((shifted d (Nat.zero_le d)).trans (congrArg o at_u.symm)))
  intro t from_t refuted
  match Nat.lt_or_ge t (s + (N + N - 1)) with
  | .inl early => exact window t from_t early refuted
  | .inr late =>
    have far : s + b + 1 ≤ t := Nat.le_trans (Nat.add_le_add_left period_le s) late
    have same : Learning.lasso (a, b) (Learning.record o t) =
        Learning.lasso (s, b) (Learning.record o t) :=
      (Learning.lasso_claims (o := o) (h := (a, b))
        (Nat.le_trans (Nat.succ_le_succ (Nat.add_le_add_right from_s b)) far)).trans
        (Learning.lasso_claims (o := o) (h := (s, b)) far).symm
    exact Learning.lasso_holds from_here t
      (Eq.subst (motive := fun c => Learning.Refuted c (o t)) same refuted)

/-- **The learner not given the bound comes to rest within it.** On a history with at
most `N` states, the learner by refutation over the lasso hypotheses, given neither `N`
nor the course (`Becoming.Learning`'s `learner lassos`), claims at every step from
`N + (N + N - 1) * tri N` on and is right. Its hypotheses all lie within `N`; in each stretch of
`N + N - 1` steps from `N` on it is refuted, or the hypothesis it holds is never refuted again
(`unrefuted_persists`); it is refuted fewer than `tri N` times. Its record does not show the
step (`Becoming.Learning`'s `no_record_fixes_next_finite`); the bound does. -/
theorem learner_rests {N : Nat} (bound : StatesBelow o N) :
    ∀ t, N + (N + N - 1) * Learning.tri N ≤ t →
      Learning.learner Learning.lassos (Learning.record o t) = some (o t) := by
  match statesBelow_iff_lasso.mp bound with
  | ⟨i, q, within, repeats⟩ =>
    match Learning.lasso_learner_bounded repeats with
    | ⟨top, claims, _⟩ =>
      let W := N + N - 1
      let k := Learning.index Learning.lassos o
      let start := fun j => N + W * j
      have few : Learning.tri (i + q) + q + 1 ≤ Learning.tri N :=
        Nat.le_trans (Learning.place_lt i q)
          (match gap_of_le within with
           | ⟨d, at_N⟩ =>
             Eq.subst (motive := fun n => Learning.tri (i + q + 1) ≤ Learning.tri n) at_N.symm
               (Learning.tri_mono _ d))
      have held_within : ∀ t, (Learning.pairAt (k t)).1 + (Learning.pairAt (k t)).2 + 1 ≤ N :=
        fun t => Nat.le_trans (Nat.succ_le_succ (Nat.le_trans (Learning.diag_le (top t))
          (Nat.le_of_eq (congrArg Learning.diag (Learning.pairAt_place i q))))) within
      have stays : ∀ s, N ≤ s → k (s + W) = k s → ∀ t, s ≤ t →
          ¬ Learning.RefutedAt (Learning.learner Learning.lassos) o t := by
        intro s from_N steady
        let h := Learning.pairAt (k s)
        have h_first : h.1 ≤ s :=
          Nat.le_trans (Nat.le_trans (Nat.le_add_right h.1 h.2)
            (Nat.le_trans (Nat.le_succ _) (held_within s))) from_N
        have flat : ∀ t, s ≤ t → t < s + W → k t = k s ∧ k (t + 1) = k s := fun t from_s lt =>
          have up : k (t + 1) ≤ k s :=
            Nat.le_trans (Learning.index_mono_le (Nat.succ_le_of_lt lt)) (Nat.le_of_eq steady)
          have mid : k t = k s :=
            Nat.le_antisymm (Nat.le_trans (Learning.index_le_succ t) up)
              (Learning.index_mono_le from_s)
          ⟨mid, Nat.le_antisymm up (Nat.le_trans (Nat.le_of_eq mid.symm)
            (Learning.index_le_succ t))⟩
        have claim_is : ∀ t, k t = k s →
            Learning.learner Learning.lassos (Learning.record o t) =
              Learning.lasso h (Learning.record o t) := fun t at_t =>
          congrArg (fun n => Learning.lasso (Learning.pairAt n) (Learning.record o t)) at_t
        have window : ∀ t, s ≤ t → t < s + W →
            ¬ Learning.RefutedAt (Learning.lasso (h.1, h.2)) o t := fun t from_s lt refuted =>
          match flat t from_s lt with
          | ⟨mid, next⟩ =>
            Nat.succ_ne_self (k s) (((congrArg (· + 1) mid).symm.trans
              (Learning.index_refuted (H := Learning.lassos) (o := o) (t := t)
                (Eq.subst (motive := fun c => Learning.Refuted c (o t)) (claim_is t mid).symm
                  refuted)).symm).trans next)
        have never := unrefuted_persists bound (held_within s) h_first window
        have kept : ∀ d, k (s + d) = k s := fun d =>
          Nat.rec (motive := fun d => k (s + d) = k s) rfl
            (fun d ih => (Learning.index_kept (fun refuted =>
              never (s + d) (Nat.le_add_right s d)
                (Eq.subst (motive := fun c => Learning.Refuted c (o (s + d)))
                  (claim_is (s + d) ih) refuted))).trans ih) d
        intro t from_s refuted
        match gap_of_le from_s with
        | ⟨d, at_t⟩ =>
          have at_t_k : k t = k s := (congrArg k at_t).trans (kept d)
          exact never t from_s
            (Eq.subst (motive := fun c => Learning.Refuted c (o t)) (claim_is t at_t_k) refuted)
      have climb : ∀ j, j ≤ k (start j) ∨
          ∀ t, start j ≤ t → ¬ Learning.RefutedAt (Learning.learner Learning.lassos) o t := by
        intro j
        induction j with
        | zero => exact .inl (Nat.zero_le _)
        | succ j ih =>
          have step : start (j + 1) = start j + W := (Nat.add_assoc N (W * j) W).symm
          have later : start j ≤ start (j + 1) :=
            Eq.subst (motive := fun n => start j ≤ n) step.symm (Nat.le_add_right _ W)
          match ih with
          | .inr quiet => exact .inr fun t from_t => quiet t (Nat.le_trans later from_t)
          | .inl count =>
            have from_N : N ≤ start j := Nat.le_add_right N _
            match Nat.lt_or_ge (k (start j)) (k (start (j + 1))) with
            | .inl rose => exact .inl (Nat.le_trans (Nat.succ_le_succ count) (Nat.succ_le_of_lt rose))
            | .inr ge =>
              have steady : k (start j + W) = k (start j) :=
                Nat.le_antisymm (Eq.subst (motive := fun n => k n ≤ k (start j)) step ge)
                  (Learning.index_mono_le (Nat.le_add_right _ W))
              exact .inr fun t from_t =>
                stays (start j) from_N steady t (Nat.le_trans later from_t)
      have quiet : ∀ t, start (Learning.tri (i + q) + q + 1) ≤ t →
          ¬ Learning.RefutedAt (Learning.learner Learning.lassos) o t :=
        match climb (Learning.tri (i + q) + q + 1) with
        | .inl count => absurd (Nat.le_trans count (top _)) (Nat.not_succ_le_self _)
        | .inr quiet => quiet
      have soon : start (Learning.tri (i + q) + q + 1) ≤ N + W * Learning.tri N :=
        Nat.add_le_add_left (Nat.mul_le_mul (Nat.le_refl W) few) N
      intro t late
      have kept := quiet t (Nat.le_trans soon late)
      match claims t (Nat.le_trans within (Nat.le_trans (Nat.le_add_right N _) late)) with
      | ⟨_, made⟩ =>
        exact made.trans (congrArg some (Learning.eq_of_not_refuted fun refuted =>
          kept (Eq.subst (motive := fun c => Learning.Refuted c (o t)) made.symm refuted)))

/-- **On a lasso course the learner comes to rest at a step that is found.** Where the course
repeats from step `i` with period `q + 1`, the learner over the lasso hypotheses claims at every
step from a step bounded by `i` and `q` on and is right: the rest that `Becoming.Learning`'s
`rest_unrefuted` leaves unrefuted is found. -/
theorem rests_of_lasso {i q : Nat} (repeats : Learning.Lasso o i q) :
    ∃ T, ∀ t, T ≤ t → Learning.learner Learning.lassos (Learning.record o t) = some (o t) :=
  ⟨_, learner_rests (statesBelow_iff_lasso.mpr ⟨i, q, Nat.le_refl _, repeats⟩)⟩

/-- **Induction in a world held by a list: the learner rests within a bound on the list.** Under
a determined law whose configurations along an orbit are held by a list `l`, the learner by
refutation over the lasso hypotheses, given neither the configurations nor how many there
are, claims at every step from `N + (N + N - 1) * tri N` on and is right, `N` the length of
`l`. -/
theorem held_learner_rests {S : Type v} {next : S → S} {s : S} {l : List S}
    (held : ∀ n, Law.orbit next s n ∈ l) (reg : S → O) :
    ∀ t, l.length + (l.length + l.length - 1) * Learning.tri l.length ≤ t →
      Learning.learner Learning.lassos
          (Learning.record (fun n => reg (Law.orbit next s n)) t) =
        some (reg (Law.orbit next s t)) :=
  learner_rests (statesBelow_iff_lasso.mpr (Learning.lasso_of_held held reg))

end Resting

end Identification

/-! ## The split that makes sense, named with no quotient -/

namespace Law

variable {S : Type v} {R : Type w}

/-- An orbit from a member of a list closed under the law stays in it. -/
theorem orbit_held {next : S → S} {l : List S} (closed : ∀ s, s ∈ l → next s ∈ l) {s : S}
    (mem : s ∈ l) : ∀ n, Law.orbit next s n ∈ l
  | 0 => mem
  | n + 1 => closed _ (orbit_held closed mem n)

/-- The registered future of a member of a list closed under the law has at most as many
states as the list has members. -/
theorem statesBelow_held {next : S → S} {l : List S} (closed : ∀ s, s ∈ l → next s ∈ l)
    {s : S} (mem : s ∈ l) (o : S → R) :
    StatesBelow (fun n => o (Law.orbit next s n)) l.length :=
  match Learning.lasso_of_held (orbit_held closed mem) o with
  | ⟨i, q, within, lasso⟩ => Identification.statesBelow_iff_lasso.mpr ⟨i, q, within, lasso⟩

/-- **In a world a list closes, the same registered future is decided by a finite record.**
Two members have the same registered future exactly where their registered futures agree for
`N + N - 1` steps, `N` the length of the list. -/
theorem sameFuture_iff_below {next : S → S} {o : S → R} {l : List S}
    (closed : ∀ s, s ∈ l → next s ∈ l) {s s' : S} (mem : s ∈ l) (mem' : s' ∈ l) :
    Law.SameFuture next o s s' ↔
      ∀ n, n < l.length + l.length - 1 → o (Law.orbit next s n) = o (Law.orbit next s' n) :=
  ⟨fun same n _ => same n,
   fun agree => Identification.bounded_agree (statesBelow_held closed mem o)
     (statesBelow_held closed mem' o) agree⟩

/-- The name of a configuration: its registered future before step `T`, latest first. -/
def name (next : S → S) (o : S → R) (T : Nat) (s : S) : List R :=
  Learning.record (fun n => o (Law.orbit next s n)) T

/-- **The split that makes sense, named with no quotient.** In a world a list holds, naming each
configuration by its registered future before `N + N - 1` makes sense. -/
theorem name_identifiesAlike {next : S → S} {o : S → R} {l : List S} (world : ∀ s, s ∈ l) :
    IdentifiesAlike (Law.registered next o) (name next o (l.length + l.length - 1)) :=
  fun s s' =>
    (Identification.record_eq_iff.trans
      (sameFuture_iff_below (fun s _ => world (next s)) (world s) (world s')).symm).trans
      Law.alike_iff_sameFuture.symm

/-- **The names carry the law.** -/
theorem name_carries {next : S → S} {o : S → R} {l : List S} (world : ∀ s, s ∈ l) :
    ∃ Q : Process (List R) Unit,
      Determined Q ∧ FactorsThrough (Law.process next) (name next o (l.length + l.length - 1)) Q :=
  Law.IdentifiesAlike.carries (name_identifiesAlike world)

/-- **Likeness is decided by comparing names.** -/
def decideAlike [DecidableEq R] {next : S → S} {o : S → R} {l : List S} (world : ∀ s, s ∈ l)
    (s s' : S) : Decidable (Alike (Law.registered next o) (Law.registered next o) s s') :=
  decidable_of_iff _ (name_identifiesAlike world s s')

end Law

end Becoming
