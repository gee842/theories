import Becoming.Recurrence

/-!
# A family of readings within what it reads

What a world reads of itself is read by parts of it. Here the readings are a family
`ψ : A → A → B`: the member `a` takes the value `ψ a x` at each `x`, and the members are among
what is read. `same` says when two values are alike: equality, or for claims `Iff`.
Nothing about the members or the values is assumed, and nothing is decided except where a law
names it.

* **The gap.** Moving each member's value at itself by a map `f` that leaves no value
  alike with its image gives a reading no member says (`gap_unsaid`). This is Lawvere's
  diagonal argument; `RootCoverageBoundary`, outside the core, proves it for functions and
  predicates. A family that says every reading gives every map a value alike with
  its image (`fixed_of_complete`).
* **For claims, never complete.** No family of claims indexed by what it reads realizes every
  pattern of claims (`claims_incomplete`), with no decision, since a claim is never alike with
  its negation (`moves_not`). A frame whose claims are its own configurations is the instance
  (`Frame.self_incomplete`).
* **Exactly where nothing differs.** For values compared by equality, a family within
  says every reading exactly when the values have nothing to tell apart
  (`complete_iff_alike`). One direction needs only that equality with one value be decided
  (`alike_of_complete`), and the other only a member and a value.
* **Completion is an unfolding.** A family that keeps what it said and next says what it missed
  (`Unfolds`) is incomplete at every step (`Unfolds.incomplete`).
  Each step's gap is said at no step up to its own (`Unfolds.gap_new`), no two gaps are
  alike (`Unfolds.gaps_differ`), and the family never returns: every later step
  says something no earlier step did (`Unfolds.never_returns`). No finite stock of
  readings holds what it misses (`Unfolds.unheld`, from `stock_unheld`: pairwise different
  readings are not all alike with members of a finite stock, with no decision on the values).
  Such an unfolding exists (`unfolding_unfolds`, `unfolding_open`). Like a kept history
  (`Law.withHistory_never_returns`, `Law.withHistory_unlisted`), it never returns and cannot be
  held by a finite stock.
* **No still value, a rhythm.** Revising a value by a map that moves every value never rests
  (`revision_never_rests`); for a claim that denies itself, revision never rests up to `Iff`
  (`negation_never_rests`); and the two-valued negation returns every two steps
  (`negation_returns`). The liar, read as a revision, is the simplest rhythm, not a
  contradiction; `Becoming.Description` reads the same rhythm off its course as two
  states, each defined through the other (`Negation.two_states`).

So, with no premise: a family of readings within what it reads is complete exactly where there
is nothing to tell apart. Where there is, what it misses is definite, and the next step can
say it, but that step misses something new; completing it is an unfolding that never
closes and never returns. Readings of this as a limit of a projection held within what it
projects, as Zhuangzi's 一与言为二，二与一为三, as the revision theory of truth, or as a limit on
self-prediction belong to the study, not to this module.

No ethical predicate, ranking or axiom occurs.

`Frame.self_incomplete` is in `Becoming.DiagonalRuns`, so this module does not import the frame
(board item W).
-/

namespace Becoming

universe u v w

namespace Diagonal

variable {A : Type u} {B : Type v}

/-! ## The gap -/

/-- Some member says `g`: its value is alike with `g`'s at every `x`. -/
def Says (same : B → B → Prop) (ψ : A → A → B) (g : A → B) : Prop :=
  ∃ a, ∀ x, same (ψ a x) (g x)

/-- Each member's value at itself, moved by `f`. -/
def gap (f : B → B) (ψ : A → A → B) (x : A) : B := f (ψ x x)

/-- `f` leaves no value alike with its image. -/
def Moves (same : B → B → Prop) (f : B → B) : Prop := ∀ b, ¬ same b (f b)

/-- No member says the gap. -/
theorem gap_unsaid {same : B → B → Prop} {f : B → B} (moves : Moves same f) (ψ : A → A → B) :
    ¬ Says same ψ (gap f ψ) :=
  fun ⟨a, h⟩ => moves (ψ a a) (h a)

/-- Lawvere's fixed point: where every reading is said, every map has a value alike with
its image. -/
theorem fixed_of_complete {same : B → B → Prop} (ψ : A → A → B) (all : ∀ g, Says same ψ g)
    (f : B → B) : ∃ b, same b (f b) :=
  match all (gap f ψ) with
  | ⟨a, h⟩ => ⟨ψ a a, h a⟩

/-- Saying carries over to a reading alike at every point. -/
theorem Says.congr {same : B → B → Prop} (trans : ∀ b b' b'', same b b' → same b' b'' → same b b'')
    {ψ : A → A → B} {g g' : A → B} (h : Says same ψ g) (e : ∀ x, same (g x) (g' x)) :
    Says same ψ g' :=
  match h with
  | ⟨a, ha⟩ => ⟨a, fun x => trans _ _ _ (ha x) (e x)⟩

/-! ## Claims -/

/-- A claim is never alike with its negation. -/
theorem moves_not : Moves Iff Not :=
  fun P h =>
    have np : ¬ P := fun p => h.mp p p
    np (h.mpr np)

/-- No family of claims indexed by what it reads realizes every pattern of claims. -/
theorem claims_incomplete (ψ : A → A → Prop) : ¬ ∀ g : A → Prop, Says Iff ψ g :=
  fun all => match fixed_of_complete ψ all Not with
    | ⟨P, h⟩ => moves_not P h

/-- In particular no member realizes exactly the members that do not realize themselves. -/
theorem claims_gap (ψ : A → A → Prop) : ¬ Says Iff ψ (fun x => ¬ ψ x x) :=
  gap_unsaid moves_not ψ

/-! ## Exactly where nothing differs -/

/-- Where equality with `b` is decided, a family that says everything leaves nothing to
tell apart from `b`. -/
theorem alike_of_complete (ψ : A → A → B) (all : ∀ g, Says Eq ψ g) (b b' : B)
    (decided : ∀ x : B, Decidable (x = b)) : b' = b :=
  match fixed_of_complete ψ all (fun x => match decided x with
      | isTrue _ => b'
      | isFalse _ => b) with
  | ⟨x, fixed⟩ => by
    revert fixed
    cases decided x with
    | isTrue same => exact fun fixed => fixed.symm.trans same
    | isFalse differ => exact fun fixed => absurd fixed differ

/-- Where values have nothing to tell apart, one member says every reading. -/
theorem complete_of_alike (a₀ : A) (b₀ : B) (alike : ∀ b b' : B, b = b') :
    ∃ ψ : A → A → B, ∀ g, Says Eq ψ g :=
  ⟨fun _ _ => b₀, fun g => ⟨a₀, fun x => alike b₀ (g x)⟩⟩

/-- A family within says every reading exactly when the values have nothing to tell
apart. -/
theorem complete_iff_alike [DecidableEq B] (a₀ : A) (b₀ : B) :
    (∃ ψ : A → A → B, ∀ g, Says Eq ψ g) ↔ ∀ b b' : B, b = b' :=
  ⟨fun ⟨ψ, all⟩ b b' => alike_of_complete ψ all b' b (fun x => decEq x b'),
   complete_of_alike a₀ b₀⟩

/-! ## Completion is an unfolding -/

/-- A family that keeps what it said and next says what it missed. -/
structure Unfolds (same : B → B → Prop) (f : B → B) (φ : Nat → A → A → B) : Prop where
  keeps : ∀ n g, Says same (φ n) g → Says same (φ (n + 1)) g
  chases : ∀ n, Says same (φ (n + 1)) (gap f (φ n))

section Unfolding

variable {same : B → B → Prop} {f : B → B} {φ : Nat → A → A → B}

theorem Unfolds.keeps_on (U : Unfolds same f φ) {g : A → B} :
    ∀ n k, Says same (φ n) g → Says same (φ (n + k)) g
  | _, 0, h => h
  | n, k + 1, h => U.keeps (n + k) g (U.keeps_on n k h)

/-- At every step something is missing: that step's own gap. This is `gap_unsaid` at step `n`, and
holds for every sequence of families, unfolding or not; the unfolding is taken so that
`U.incomplete` reads by dot notation. -/
theorem Unfolds.incomplete (_ : Unfolds same f φ) (moves : Moves same f) (n : Nat) :
    ¬ Says same (φ n) (gap f (φ n)) :=
  gap_unsaid moves (φ n)

/-- A gap is said at no step up to its own. -/
theorem Unfolds.gap_new (U : Unfolds same f φ) (moves : Moves same f) (m k : Nat) :
    ¬ Says same (φ m) (gap f (φ (m + k))) :=
  fun h => gap_unsaid moves (φ (m + k)) (U.keeps_on m k h)

/-- No two gaps are alike: what is missed is new each time. -/
theorem Unfolds.gaps_differ (U : Unfolds same f φ) (moves : Moves same f)
    (trans : ∀ b b' b'', same b b' → same b' b'' → same b b'') (m k : Nat) :
    ¬ ∀ x, same (gap f (φ m) x) (gap f (φ (m + 1 + k)) x) :=
  fun e => gap_unsaid moves (φ (m + 1 + k)) ((U.keeps_on (m + 1) k (U.chases m)).congr trans e)

/-- The family never returns: every later step says something no earlier step did. -/
theorem Unfolds.never_returns (U : Unfolds same f φ) (moves : Moves same f) (n k : Nat) :
    ¬ ∀ g, Says same (φ (n + 1 + k)) g → Says same (φ n) g :=
  fun back => gap_unsaid moves (φ n) (back _ (U.keeps_on (n + 1) k (U.chases n)))

end Unfolding

theorem two_ne_odd : ∀ a b : Nat, a + a ≠ b + b + 1
  | 0, _, h => nomatch h
  | a + 1, 0, h => nomatch Nat.succ.inj ((congrArg Nat.succ (Nat.succ_add a a)).symm.trans h)
  | a + 1, b + 1, h => two_ne_odd a b (Nat.succ.inj (Nat.succ.inj
      ((congrArg Nat.succ (Nat.succ_add a a)).symm.trans
        (h.trans (congrArg (· + 1) (congrArg Nat.succ (Nat.succ_add b b)))))))

/-- Pairwise different readings are not all alike with members of a finite stock: with no
decision, by halving the sequence into its even and odd places. -/
theorem stock_unheld {same : B → B → Prop} (symm : ∀ b b', same b b' → same b' b)
    (trans : ∀ b b' b'', same b b' → same b' b'' → same b b'') :
    ∀ (L : Nat) (r : Nat → A → B) (d : Nat → A → B),
      (∀ m n, m < n → ¬ ∀ x, same (d m x) (d n x)) → ¬ ∀ n, ∃ i, i < L ∧ ∀ x, same (r i x) (d n x)
  | 0, _, _, _, H => match H 0 with | ⟨i, hi, _⟩ => absurd hi (Nat.not_lt_zero i)
  | L + 1, r, d, differ, H =>
    have notBoth : ¬ ((∃ a, ∀ x, same (r L x) (d (a + a) x)) ∧
        (∃ b, ∀ x, same (r L x) (d (b + b + 1) x))) :=
      fun ⟨⟨a, ha⟩, ⟨b, hb⟩⟩ =>
        have alike : ∀ x, same (d (a + a) x) (d (b + b + 1) x) :=
          fun x => trans _ _ _ (symm _ _ (ha x)) (hb x)
        match Nat.lt_or_gt_of_ne (two_ne_odd a b) with
        | .inl lt => differ _ _ lt alike
        | .inr gt => differ _ _ gt (fun x => symm _ _ (alike x))
    have evens : ¬ (∃ a, ∀ x, same (r L x) (d (a + a) x)) → False := fun none =>
      stock_unheld symm trans L r (fun n => d (n + n))
        (fun _ _ lt => differ _ _ (Nat.add_lt_add lt lt))
        (fun n => match H (n + n) with
          | ⟨i, hi, hr⟩ =>
            match decEq i L with
            | isTrue e => False.elim (none ⟨n, e ▸ hr⟩)
            | isFalse ne => ⟨i, Nat.lt_of_le_of_ne (Nat.le_of_lt_succ hi) ne, hr⟩)
    have odds : ¬ (∃ b, ∀ x, same (r L x) (d (b + b + 1) x)) → False := fun none =>
      stock_unheld symm trans L r (fun n => d (n + n + 1))
        (fun _ _ lt => differ _ _ (Nat.succ_lt_succ (Nat.add_lt_add lt lt)))
        (fun n => match H (n + n + 1) with
          | ⟨i, hi, hr⟩ =>
            match decEq i L with
            | isTrue e => False.elim (none ⟨n, e ▸ hr⟩)
            | isFalse ne => ⟨i, Nat.lt_of_le_of_ne (Nat.le_of_lt_succ hi) ne, hr⟩)
    evens (fun e => odds (fun o => notBoth ⟨e, o⟩))

/-- No finite stock of readings holds what an unfolding family misses. -/
theorem Unfolds.unheld {same : B → B → Prop} {f : B → B} {φ : Nat → A → A → B}
    (U : Unfolds same f φ) (moves : Moves same f) (symm : ∀ b b', same b b' → same b' b)
    (trans : ∀ b b' b'', same b b' → same b' b'' → same b b'') (L : Nat) (r : Nat → A → B) :
    ¬ ∀ n, ∃ i, i < L ∧ ∀ x, same (r i x) (gap f (φ n) x) :=
  stock_unheld symm trans L r (fun n => gap f (φ n)) (fun m n lt =>
    match gap_of_lt lt with
    | ⟨k, e⟩ => by
      subst e
      exact (Nat.add_right_comm m k 1 ▸ U.gaps_differ moves trans m k :
        ¬ ∀ x, same (gap f (φ m) x) (gap f (φ (m + (k + 1))) x)))

/-! ## An unfolding exists -/

/-- At step `n + 1` the member `n + 1` takes up the gap of step `n`; members not yet reached
take `false`. -/
def unfolding : Nat → Nat → Nat → Bool
  | 0, _, _ => false
  | n + 1, a, x => if a = n + 1 then !(unfolding n x x) else unfolding n a x

theorem unfolding_fresh : ∀ n a, n < a → ∀ x, unfolding n a x = false
  | 0, _, _, _ => rfl
  | n + 1, a, h, x => by
    have ne : a ≠ n + 1 := fun e => Nat.lt_irrefl (n + 1) (e ▸ h)
    show (if a = n + 1 then !(unfolding n x x) else unfolding n a x) = false
    exact (if_neg ne).trans (unfolding_fresh n a (Nat.lt_of_succ_lt h) x)

theorem unfolding_zero : ∀ n x, unfolding n 0 x = false
  | 0, _ => rfl
  | n + 1, x => by
    show (if (0 : Nat) = n + 1 then !(unfolding n x x) else unfolding n 0 x) = false
    exact (if_neg (fun e : (0 : Nat) = n + 1 => nomatch e)).trans (unfolding_zero n x)

theorem flip_moves : Moves (@Eq Bool) (fun b => !b)
  | true => fun h => nomatch h
  | false => fun h => nomatch h

theorem unfolding_unfolds : Unfolds Eq (fun b => !b) unfolding where
  keeps n g := fun ⟨a, ha⟩ =>
    match decEq a (n + 1) with
    | isTrue e => ⟨0, fun x => (unfolding_zero (n + 1) x).trans
        ((unfolding_fresh n a (e ▸ Nat.lt_succ_self n) x).symm.trans (ha x))⟩
    | isFalse ne => ⟨a, fun x => by
        show (if a = n + 1 then !(unfolding n x x) else unfolding n a x) = g x
        exact (if_neg ne).trans (ha x)⟩
  chases n := ⟨n + 1, fun x => by
    show (if n + 1 = n + 1 then !(unfolding n x x) else unfolding n (n + 1) x) = !(unfolding n x x)
    exact if_pos rfl⟩

/-- It never closes and never returns, and no finite stock holds what it misses. -/
theorem unfolding_open (L : Nat) (r : Nat → Nat → Bool) :
    (∀ n, ¬ Says Eq (unfolding n) (gap (fun b => !b) (unfolding n))) ∧
      (∀ n k, ¬ ∀ g, Says Eq (unfolding (n + 1 + k)) g → Says Eq (unfolding n) g) ∧
      ¬ ∀ n, ∃ i, i < L ∧ ∀ x, r i x = gap (fun b => !b) (unfolding n) x :=
  ⟨unfolding_unfolds.incomplete flip_moves, unfolding_unfolds.never_returns flip_moves,
   unfolding_unfolds.unheld flip_moves (fun _ _ e => e.symm) (fun _ _ _ e e' => e.trans e') L r⟩

/-! ## No still value, a rhythm -/

/-- Revising a value by a map that moves every value never rests. -/
theorem revision_never_rests {f : B → B} (moves : Moves Eq f) (b : B) (n : Nat) :
    Law.orbit f b (n + 1) ≠ Law.orbit f b n :=
  fun e => moves (Law.orbit f b n) e.symm

/-- A claim that denies itself: revision never rests, up to `Iff`. -/
theorem negation_never_rests (P : Prop) (n : Nat) :
    ¬ (Law.orbit Not P (n + 1) ↔ Law.orbit Not P n) :=
  fun e => moves_not (Law.orbit Not P n) (Iff.symm e)

/-- The two-valued negation returns every two steps. -/
theorem negation_returns (b : Bool) : Law.Returns (fun b : Bool => !b) b :=
  ⟨2, Nat.zero_lt_succ 1, Bool.not_not b⟩

end Diagonal

end Becoming
