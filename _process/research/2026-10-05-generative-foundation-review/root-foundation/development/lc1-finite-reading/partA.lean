
/-! ## Rest from a finite reading: no least loss -/

namespace Amounts

variable {A : Type} {M : Amounts A} {S : Type}

/-- Steps rising one after another, `f i < f (i + 1)` below `K`, lie at least as far apart as
their indices. -/
theorem rising_apart {f : Nat → Nat} {K : Nat} (rising : ∀ i, i < K → f i < f (i + 1)) (i : Nat) :
    ∀ d, i + d ≤ K → f i + d ≤ f (i + d)
  | 0, _ => Nat.le_refl _
  | d + 1, within => Nat.le_trans (Nat.succ_le_succ (rising_apart rising i d
      (Nat.le_of_succ_le within))) (rising (i + d) within)

/-- **A finite reading counts the falls.** Read an amount `q` off configurations `g t` that a
list `l` holds, and let it not rise across any step from `T` on. Then of any `l.length + 1`
steps `f 0 < f 1 < ⋯` from `T` on, not every one is a step across which the amount falls
strictly (is not, after the step, back within its value before): at most `l.length` steps fall
strictly. No least loss is asked, no Archimedean property, no totality and no decision: a strict
fall leaves a configuration the amount never reads again, and the list has room for only so many. -/
theorem falls_within_reading {g : Nat → S} {q : S → A} {l : List S} {T : Nat}
    (held : ∀ t, g t ∈ l) (still : ∀ t, T ≤ t → M.le (q (g (t + 1))) (q (g t)))
    {f : Nat → Nat} (start : T ≤ f 0) (rising : ∀ i, i < l.length → f i < f (i + 1)) :
    ¬ ∀ i, i ≤ l.length → ¬ M.le (q (g (f i))) (q (g (f i + 1))) := fun falls =>
  match revisits_within l (fun i => g (f i)) (fun n _ => held (f n)) with
  | ⟨i, j, lt, le, same⟩ =>
    match gap_of_lt lt with
    | ⟨d, at_j⟩ =>
      have from_i : T ≤ f i := Nat.le_trans start
        (Nat.le_trans (Nat.le_add_left (f 0) i)
          (Nat.le_trans (Nat.le_of_eq (Nat.add_comm i (f 0)))
            (Nat.le_trans (rising_apart rising 0 i
              (Nat.le_trans (Nat.le_of_eq (Nat.zero_add i)) (Nat.le_trans (Nat.le_of_lt lt) le)))
              (Nat.le_of_eq (congrArg f (Nat.zero_add i))))))
      have apart : f i + 1 ≤ f j :=
        Nat.le_trans (Nat.succ_le_succ (Nat.le_add_right (f i) d))
          (Nat.le_trans (rising_apart rising i (d + 1) (Nat.le_trans (Nat.le_of_eq at_j.symm) le))
            (Nat.le_of_eq (congrArg f at_j.symm)))
      match le_dest apart with
      | ⟨e, at_fj⟩ =>
        have down : M.le (q (g (f j))) (q (g (f i + 1))) :=
          Eq.subst (motive := fun x => M.le (q (g x)) (q (g (f i + 1)))) at_fj.symm
            (still_within (s := fun t => q (g t)) still e (f i + 1) (Nat.le_succ_of_le from_i))
        falls i (Nat.le_trans (Nat.le_of_lt lt) le)
          (Eq.subst (motive := fun x => M.le (q x) (q (g (f i + 1)))) same.symm down)

/-- **Rest from a finite reading.** Where a list holds the configurations an amount is read off
and the amount does not rise across any step from `T` on, steps across which it falls strictly
do not recur. Over any amounts: no least loss, no Archimedean property, no totality of the order
and no decision is asked. The least loss on which `Amounts.rests` turns is needed only where the
amount reads configurations no list holds: falls that recur need an unbounded reading
(`Halving.stock_unlisted`). -/
theorem rests_of_finite_reading {g : Nat → S} {q : S → A} {l : List S} {T : Nat}
    (held : ∀ t, g t ∈ l) (still : ∀ t, T ≤ t → M.le (q (g (t + 1))) (q (g t))) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ ¬ M.le (q (g t)) (q (g (t + 1))) := fun recurs =>
  have chain : ∀ m, ∃ f : Nat → Nat, T ≤ f 0 ∧ (∀ i, i < m → f i < f (i + 1)) ∧
      ∀ i, i ≤ m → ¬ M.le (q (g (f i))) (q (g (f i + 1))) := fun m => by
    induction m with
    | zero =>
      match recurs T with
      | ⟨t, after, fall⟩ =>
        exact ⟨fun _ => t, after, fun i below => absurd below (Nat.not_lt_zero i), fun _ _ => fall⟩
    | succ m ih =>
      match ih with
      | ⟨f, start, rising, falls⟩ =>
        match recurs (f m + 1) with
        | ⟨t, after, fall⟩ =>
          refine ⟨fun i => if i ≤ m then f i else t, ?_, ?_, ?_⟩
          · exact Eq.subst (motive := fun x => T ≤ x) (if_pos (Nat.zero_le m)).symm start
          · intro i below
            have at_i : (if i ≤ m then f i else t) = f i := if_pos (Nat.le_of_lt_succ below)
            show (if i ≤ m then f i else t) < (if i + 1 ≤ m then f (i + 1) else t)
            rw [at_i]
            match Nat.decLe (i + 1) m with
            | isTrue next =>
              rw [if_pos next]
              exact rising i next
            | isFalse past =>
              rw [if_neg past]
              have same : i = m := Nat.le_antisymm (Nat.le_of_lt_succ below)
                (Nat.le_of_lt_succ (Nat.gt_of_not_le past))
              rw [same]
              exact after
          · intro i within
            match Nat.decLe i m with
            | isTrue earlier =>
              show ¬ M.le (q (g (if i ≤ m then f i else t)))
                (q (g ((if i ≤ m then f i else t) + 1)))
              rw [if_pos earlier]
              exact falls i earlier
            | isFalse later =>
              show ¬ M.le (q (g (if i ≤ m then f i else t)))
                (q (g ((if i ≤ m then f i else t) + 1)))
              rw [if_neg later]
              exact fall
  match chain l.length with
  | ⟨f, start, rising, falls⟩ => falls_within_reading held still start rising falls

end Amounts

namespace Halving

/-- **Falls that recur need an unbounded reading.** The halving stock falls strictly at every
step, so no list holds its values: by `Amounts.rests_of_finite_reading`, a list holding them would
bring its falls to rest. Halving's lack of a least loss and the unbounded count of its values are
one fact read twice. -/
theorem stock_unlisted : ¬ ∃ l : List Dyadic, ∀ t, stock t ∈ l := fun ⟨_, held⟩ =>
  Amounts.rests_of_finite_reading (M := Dyadic.amounts) (q := fun x => x) (T := 0) held
    (fun t _ => never_rests.2.1 t) (fun N => ⟨N, Nat.le_refl N, falls_strictly N⟩)

end Halving
