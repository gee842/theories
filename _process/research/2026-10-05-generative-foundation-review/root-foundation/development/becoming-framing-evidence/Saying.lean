/-!
# What a framing keeps and loses, and what makes a split make sense (scratch evidence, not landed)

Written by the AI (Claude Opus 5.5), 12 October 2026, to answer Ren's questions on the branch
"Current math core (fork)": that describing seems to separate the whole into a projection and lose
something (wave and particle, 道可道非常道), and what makes a split make sense, a pair a pair.

Prelude only; every axiom report empty. Builds on, and does not replace:
* `RelationalFormation.Rectangular` and `diagonal_not_rectangular` (`deeper/RelationalFormation.lean`,
  8 October): rectangular possibility, kept by factorized dynamics.
* `RootCoverageBoundary` (`mathematical-abstraction/constitution/global/formal/CoverageBoundary.lean`,
  7 October): Lawvere's diagonal theorem for functions, the external reading and the strict
  one-step extension (`diagonal_extension_strict`).
* `Becoming.Mechanism` (P66, landing package): a projection carries a law exactly where
  configurations alike under it go alike (`GoAlike`, `carries_law_iff`, `goAlike_const`).

Overlaps P69 (held by "Current math core" [1c3084]): `SameFuture`, `SameAhead` and `MakesSense`
bear on P69's item (3), configurations alike by relation (`Alike`, `Bisimulation` in the owner's
draft). Handed to the owner under the work board's rule 2.

Sections: 1 separation, and a relation held by the whole and by no pair; 2 a saying within; 3 the saying as a becoming; 4 the liar; 5 an odd cycle;
6 the split by the same registered future; 7 the pair; 8 states from moments; 9 making sense;
10 Specker's three boxes.
-/

namespace Saying

universe u v w

theorem cancel : ∀ k {a b : Nat}, a + k = b + k → a = b
  | 0, _, _, h => h
  | k + 1, _, _, h => cancel k (Nat.succ.inj h)

theorem flip_moves : ∀ b : Bool, (!b) ≠ b
  | true => fun h => nomatch h
  | false => fun h => nomatch h

/-! ## 1. Separating the parts loses exactly their relation -/

section Separation
variable {A : Type u} {B : Type v}

/-- As in `RelationalFormation`: whatever goes with one part goes with every other. -/
def Rectangular (whole : A × B → Prop) : Prop :=
  ∀ a a' b b', whole (a, b) → whole (a', b') → whole (a, b')

/-- Each part described by itself: what it can be, with nothing of what it goes with. -/
def Separated (whole : A × B → Prop) (p : A × B) : Prop :=
  (∃ b, whole (p.1, b)) ∧ (∃ a, whole (a, p.2))

/-- Separation keeps every combination that occurs. -/
theorem separated_of_whole {whole : A × B → Prop} {p : A × B} (h : whole p) : Separated whole p :=
  ⟨⟨p.2, h⟩, ⟨p.1, h⟩⟩

/-- Separation adds nothing exactly when the parts are unrelated. -/
theorem separation_faithful_iff {whole : A × B → Prop} :
    (∀ p, Separated whole p → whole p) ↔ Rectangular whole := by
  constructor
  · intro faithful a a' b b' hab ha'b'
    exact faithful (a, b') ⟨⟨b, hab⟩, ⟨a', ha'b'⟩⟩
  · intro rect p ⟨⟨b, hb⟩, ⟨a, ha⟩⟩
    exact rect p.1 a b p.2 hb ha

/-- Two parts that go the same way. -/
def same : Bool × Bool → Prop := fun p => p.1 = p.2

/-- Described separately, they could go different ways. -/
theorem same_separated : Separated same (true, false) ∧ ¬ same (true, false) :=
  ⟨⟨⟨true, rfl⟩, ⟨false, rfl⟩⟩, fun h => nomatch h⟩

end Separation

/-- `flipIf x b` turns `b` over exactly when `x` holds. -/
def flipIf : Bool → Bool → Bool
  | true, b => !b
  | false, b => b

/-- Three parts related as a whole: their parity is even. -/
def evenThree (p : Bool × Bool × Bool) : Prop := flipIf p.1 (flipIf p.2.1 p.2.2) = false

/-- Every two of the three may be anything, and the three may not: the relation is held by the
whole and shown by no pair, so describing every pair loses it. -/
theorem whole_not_in_pairs :
    (∀ x y : Bool, ∃ z, evenThree (x, y, z)) ∧ (∀ y z : Bool, ∃ x, evenThree (x, y, z)) ∧
      (∀ x z : Bool, ∃ y, evenThree (x, y, z)) ∧ ¬ evenThree (true, false, false) :=
  ⟨fun x y => match x, y with
    | true, true => ⟨false, rfl⟩
    | true, false => ⟨true, rfl⟩
    | false, true => ⟨true, rfl⟩
    | false, false => ⟨false, rfl⟩,
   fun y z => match y, z with
    | true, true => ⟨false, rfl⟩
    | true, false => ⟨true, rfl⟩
    | false, true => ⟨true, rfl⟩
    | false, false => ⟨false, rfl⟩,
   fun x z => match x, z with
    | true, true => ⟨false, rfl⟩
    | true, false => ⟨true, rfl⟩
    | false, true => ⟨true, rfl⟩
    | false, false => ⟨false, rfl⟩,
   fun h => nomatch h⟩

/-! ## 2. A saying within what it says -/

section Within
variable {A : Type u} {B : Type v}

/-- `ψ a` is what `a` says: a reading of every `x`. The sayers are among what is read. -/
def Says (ψ : A → A → B) (g : A → B) : Prop := ∃ a, ∀ x, ψ a x = g x

/-- What the saying says of each sayer, changed by `f`. -/
def gap (f : B → B) (ψ : A → A → B) (x : A) : B := f (ψ x x)

/-- Lawvere's diagonal, as `RootCoverageBoundary.no_complete_fixedpoint_free`: where `f` leaves
nothing in place, no saying within says its own gap. -/
theorem gap_unsaid {f : B → B} (moves : ∀ b, f b ≠ b) (ψ : A → A → B) : ¬ Says ψ (gap f ψ) :=
  fun ⟨a, h⟩ => moves (ψ a a) (h a).symm

theorem Says.congr {ψ : A → A → B} {g g' : A → B} (h : Says ψ g) (e : ∀ x, g x = g' x) :
    Says ψ g' :=
  match h with | ⟨a, ha⟩ => ⟨a, fun x => (ha x).trans (e x)⟩

/-- Everything can be said from within exactly where readings make no difference. -/
theorem complete_iff_no_difference [DecidableEq B] (a₀ : A) (b₀ : B) :
    (∃ ψ : A → A → B, ∀ g, Says ψ g) ↔ ∀ b b' : B, b = b' := by
  constructor
  · intro ⟨ψ, all⟩ b b'
    match decEq b b' with
    | isTrue same => exact same
    | isFalse differ =>
      have moves : ∀ x, (if x = b then b' else b) ≠ x := fun x e =>
        match decEq x b with
        | isTrue hx => differ ((((if_pos hx).symm.trans e).trans hx).symm)
        | isFalse hx => hx (((if_neg hx).symm.trans e).symm)
      exact absurd (all (gap (fun x => if x = b then b' else b) ψ)) (gap_unsaid moves ψ)
  · intro all
    exact ⟨fun _ _ => b₀, fun g => ⟨a₀, fun x => all b₀ (g x)⟩⟩

/-! ## 3. The saying as a becoming -/

variable {f : B → B}

/-- A saying that keeps what it said and says, next, what it missed. -/
structure Unfolds (f : B → B) (φ : Nat → A → A → B) : Prop where
  keeps : ∀ n g, Says (φ n) g → Says (φ (n + 1)) g
  chases : ∀ n, Says (φ (n + 1)) (gap f (φ n))

theorem Unfolds.keeps_on {φ : Nat → A → A → B} (U : Unfolds f φ) {g : A → B} :
    ∀ n k, Says (φ n) g → Says (φ (n + k)) g
  | _, 0, h => h
  | n, k + 1, h => U.keeps (n + k) g (U.keeps_on n k h)

/-- At every step something is missing: that step's own gap. -/
theorem Unfolds.incomplete (moves : ∀ b, f b ≠ b) (φ : Nat → A → A → B) (n : Nat) :
    ¬ Says (φ n) (gap f (φ n)) :=
  gap_unsaid moves (φ n)

/-- A gap is said at no step up to its own. -/
theorem Unfolds.gap_new {φ : Nat → A → A → B} (U : Unfolds f φ) (moves : ∀ b, f b ≠ b)
    (m k : Nat) : ¬ Says (φ m) (gap f (φ (m + k))) :=
  fun h => gap_unsaid moves (φ (m + k)) (U.keeps_on m k h)

/-- No two gaps are alike: what is missed is new each time. -/
theorem Unfolds.gaps_differ {φ : Nat → A → A → B} (U : Unfolds f φ) (moves : ∀ b, f b ≠ b)
    (m k : Nat) : ¬ ∀ x, gap f (φ m) x = gap f (φ (m + 1 + k)) x :=
  fun e => gap_unsaid moves (φ (m + 1 + k)) ((U.keeps_on (m + 1) k (U.chases m)).congr e)

/-- The saying never returns: every later step says something no earlier step said. -/
theorem Unfolds.never_returns {φ : Nat → A → A → B} (U : Unfolds f φ) (moves : ∀ b, f b ≠ b)
    (n k : Nat) : ¬ ∀ g, Says (φ (n + 1 + k)) g → Says (φ n) g :=
  fun back => gap_unsaid moves (φ n) (back _ (U.keeps_on (n + 1) k (U.chases n)))

theorem lt_split : ∀ {m n : Nat}, m < n → ∃ k, n = m + 1 + k
  | m, 0, h => absurd h (Nat.not_lt_zero m)
  | _, n + 1, h =>
    match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ h) with
    | .inl lt => match lt_split lt with | ⟨k, e⟩ => ⟨k + 1, congrArg (· + 1) e⟩
    | .inr eq => ⟨0, by subst eq; rfl⟩

theorem two_ne_odd : ∀ a b : Nat, a + a ≠ b + b + 1
  | 0, _, h => nomatch h
  | a + 1, 0, h => nomatch Nat.succ.inj ((congrArg Nat.succ (Nat.succ_add a a)).symm.trans h)
  | a + 1, b + 1, h => two_ne_odd a b (Nat.succ.inj (Nat.succ.inj
      ((congrArg Nat.succ (Nat.succ_add a a)).symm.trans
        (h.trans (congrArg (· + 1) (congrArg Nat.succ (Nat.succ_add b b)))))))

/-- Pairwise different readings cannot all be held among finitely many. -/
theorem finite_stock :
    ∀ (L : Nat) (r : Nat → A → B) (d : Nat → A → B),
      (∀ m n, m < n → ¬ ∀ x, d m x = d n x) → ¬ ∀ n, ∃ i, i < L ∧ ∀ x, r i x = d n x
  | 0, _, _, _, H => match H 0 with | ⟨i, hi, _⟩ => absurd hi (Nat.not_lt_zero i)
  | L + 1, r, d, differ, H =>
    have notBoth : ¬ ((∃ a, ∀ x, r L x = d (a + a) x) ∧ (∃ b, ∀ x, r L x = d (b + b + 1) x)) :=
      fun ⟨⟨a, ha⟩, ⟨b, hb⟩⟩ =>
        have alike : ∀ x, d (a + a) x = d (b + b + 1) x := fun x => (ha x).symm.trans (hb x)
        match Nat.lt_or_gt_of_ne (two_ne_odd a b) with
        | .inl lt => differ _ _ lt alike
        | .inr gt => differ _ _ gt (fun x => (alike x).symm)
    have evens : ¬ (∃ a, ∀ x, r L x = d (a + a) x) → False := fun none =>
      finite_stock L r (fun n => d (n + n))
        (fun _ _ lt => differ _ _ (Nat.add_lt_add lt lt))
        (fun n => match H (n + n) with
          | ⟨i, hi, hr⟩ =>
            match decEq i L with
            | isTrue e => False.elim (none ⟨n, e ▸ hr⟩)
            | isFalse ne => ⟨i, Nat.lt_of_le_of_ne (Nat.le_of_lt_succ hi) ne, hr⟩)
    have odds : ¬ (∃ b, ∀ x, r L x = d (b + b + 1) x) → False := fun none =>
      finite_stock L r (fun n => d (n + n + 1))
        (fun _ _ lt => differ _ _ (Nat.succ_lt_succ (Nat.add_lt_add lt lt)))
        (fun n => match H (n + n + 1) with
          | ⟨i, hi, hr⟩ =>
            match decEq i L with
            | isTrue e => False.elim (none ⟨n, e ▸ hr⟩)
            | isFalse ne => ⟨i, Nat.lt_of_le_of_ne (Nat.le_of_lt_succ hi) ne, hr⟩)
    evens (fun e => odds (fun o => notBoth ⟨e, o⟩))

/-- So no finite stock of readings holds what an unfolding saying misses. -/
theorem Unfolds.unheld {φ : Nat → A → A → B} (U : Unfolds f φ) (moves : ∀ b, f b ≠ b)
    (L : Nat) (r : Nat → A → B) : ¬ ∀ n, ∃ i, i < L ∧ ∀ x, r i x = gap f (φ n) x :=
  finite_stock L r (fun n => gap f (φ n)) (fun m n lt => by
    match lt_split lt with
    | ⟨k, e⟩ => subst e; exact U.gaps_differ moves m k)

end Within

/-- A saying that does unfold: sayer `n + 1` takes up, at step `n + 1`, the gap of step `n`. -/
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

theorem unfolds : Unfolds (fun b => !b) unfolding where
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
    (∀ n, ¬ Says (unfolding n) (gap (fun b => !b) (unfolding n))) ∧
      (∀ n k, ¬ ∀ g, Says (unfolding (n + 1 + k)) g → Says (unfolding n) g) ∧
      ¬ ∀ n, ∃ i, i < L ∧ ∀ x, r i x = gap (fun b => !b) (unfolding n) x :=
  ⟨Unfolds.incomplete flip_moves unfolding, unfolds.never_returns flip_moves,
   unfolds.unheld flip_moves L r⟩

/-! ## 4. The liar: no still value, a regular movement -/

def liar : Nat → Bool
  | 0 => true
  | n + 1 => !(liar n)

theorem not_not' : ∀ b : Bool, (!!b) = b
  | true => rfl
  | false => rfl

theorem liar_moves (n : Nat) : liar (n + 1) ≠ liar n := flip_moves (liar n)

theorem liar_returns (n : Nat) : liar (n + 2) = liar n := not_not' (liar n)

/-! ## 5. Views that hold two at a time and not all at once -/

theorem any_two_hold :
    (∃ x y z : Bool, x ≠ y ∧ y ≠ z) ∧ (∃ x y z : Bool, y ≠ z ∧ z ≠ x) ∧
      (∃ x y z : Bool, z ≠ x ∧ x ≠ y) :=
  ⟨⟨true, false, true, (fun h => nomatch h), (fun h => nomatch h)⟩,
   ⟨true, true, false, (fun h => nomatch h), (fun h => nomatch h)⟩,
   ⟨true, false, false, (fun h => nomatch h), (fun h => nomatch h)⟩⟩

theorem three_do_not : ∀ x y z : Bool, ¬ (x ≠ y ∧ y ≠ z ∧ z ≠ x)
  | true, true, _, h => h.1 rfl
  | false, false, _, h => h.1 rfl
  | true, false, true, h => h.2.2 rfl
  | true, false, false, h => h.2.1 rfl
  | false, true, true, h => h.2.1 rfl
  | false, true, false, h => h.2.2 rfl

/-! ## 6. A split that makes sense, relative to what is registered

For one determined law this is the construction of the minimal automaton (Myhill–Nerode) and of
causal states in computational mechanics (Crutchfield and Young 1989; Shalizi and Crutchfield 2001):
configurations are one state when everything registered from them on is alike. -/

section Sense
variable {S : Type u} {O : Type v}

def orbit (next : S → S) (s : S) : Nat → S
  | 0 => s
  | n + 1 => orbit next (next s) n

/-- Alike in all that will be registered. -/
def SameFuture (next : S → S) (o : S → O) (s s' : S) : Prop :=
  ∀ n, o (orbit next s n) = o (orbit next s' n)

/-- A reading keeps every difference that will make a difference to what is registered. -/
def Sufficient (next : S → S) (o : S → O) {K : Type w} (π : S → K) : Prop :=
  ∀ s s', π s = π s' → SameFuture next o s s'

/-- A reading carries a law: what it lumps goes on lumped (P66's `GoAlike`, determined law). -/
def CarriesLaw (next : S → S) {K : Type w} (π : S → K) : Prop :=
  ∀ s s', π s = π s' → π (next s) = π (next s')

theorem SameFuture.refl (next : S → S) (o : S → O) (s : S) : SameFuture next o s s :=
  fun _ => rfl

theorem SameFuture.symm {next : S → S} {o : S → O} {s s' : S} (h : SameFuture next o s s') :
    SameFuture next o s' s := fun n => (h n).symm

theorem SameFuture.trans {next : S → S} {o : S → O} {s s' s'' : S} (h : SameFuture next o s s')
    (h' : SameFuture next o s' s'') : SameFuture next o s s'' := fun n => (h n).trans (h' n)

theorem SameFuture.registered {next : S → S} {o : S → O} {s s' : S}
    (h : SameFuture next o s s') : o s = o s' := h 0

theorem SameFuture.goes {next : S → S} {o : S → O} {s s' : S}
    (h : SameFuture next o s s') : SameFuture next o (next s) (next s') := fun n => h (n + 1)

/-- The split by the same registered future is the greatest relation that keeps what is
registered and goes on as itself: every such relation lies within it. -/
theorem SameFuture.greatest {next : S → S} {o : S → O} (R : S → S → Prop)
    (keeps : ∀ s s', R s s' → o s = o s') (goes : ∀ s s', R s s' → R (next s) (next s')) :
    ∀ s s', R s s' → SameFuture next o s s' := by
  intro s s' h n
  induction n generalizing s s' with
  | zero => exact keeps s s' h
  | succ n ih => exact ih (next s) (next s') (goes s s' h)

/-- The reading that distinguishes nothing always carries a law (P66's `goAlike_const`), and is
sufficient only where nothing registered can ever differ. -/
theorem const_carries (next : S → S) : CarriesLaw next (fun _ : S => ()) := fun _ _ _ => rfl

theorem const_sufficient_iff {next : S → S} {o : S → O} :
    Sufficient next o (fun _ : S => ()) ↔ ∀ s s', SameFuture next o s s' :=
  ⟨fun h s s' => h s s' rfl, fun h s s' _ => h s s'⟩

end Sense

/-! ## 7. The pair: where it stands, and how it passes -/

/-- The standing changes by the passing. -/
def move (s : Nat × Nat) : Nat × Nat := (s.1 + s.2, s.2)

/-- Registering only where it stands, the canonical split keeps both. -/
theorem pair_canonical (x v x' v' : Nat) :
    SameFuture move Prod.fst (x, v) (x', v') ↔ x = x' ∧ v = v' := by
  constructor
  · intro h
    have hx : x = x' := h 0
    have h1 : x + v = x' + v' := h 1
    subst hx
    exact ⟨rfl, cancel x ((Nat.add_comm v x).trans (h1.trans (Nat.add_comm x v')))⟩
  · intro ⟨hx, hv⟩
    subst hx
    subst hv
    exact fun _ => rfl

/-- Standing alone carries no law and is not enough. -/
theorem standing_alone :
    ¬ CarriesLaw move Prod.fst ∧ ¬ Sufficient move Prod.fst Prod.fst :=
  ⟨fun h => absurd (h (0, 0) (0, 1) rfl) (by decide),
   fun h => absurd ((h (0, 0) (0, 1) rfl) 1) (by decide)⟩

/-- Passing alone is not enough either. -/
theorem passing_alone : ¬ Sufficient move Prod.fst Prod.snd :=
  fun h => absurd ((h (0, 0) (1, 0) rfl) 0) (by decide)

/-- Where nothing passes, standing alone is the canonical split: the pair is one. -/
def still (s : Nat × Nat) : Nat × Nat := s

theorem orbit_still : ∀ (s : Nat × Nat) n, orbit still s n = s
  | _, 0 => rfl
  | s, n + 1 => orbit_still s n

theorem still_canonical (s s' : Nat × Nat) :
    SameFuture still Prod.fst s s' ↔ s.1 = s'.1 :=
  ⟨fun h => h 0, fun h n =>
    (congrArg Prod.fst (orbit_still s n)).trans (h.trans (congrArg Prod.fst (orbit_still s' n)).symm)⟩

/-! ## 8. States from one registered unfolding -/

section Moments
variable {O : Type v}

/-- Two moments are one state when all that follows each is registered alike. -/
def SameAhead (o : Nat → O) (t t' : Nat) : Prop := ∀ n, o (t + n) = o (t' + n)

theorem SameAhead.symm {o : Nat → O} {t t' : Nat} (h : SameAhead o t t') : SameAhead o t' t :=
  fun n => (h n).symm

theorem SameAhead.trans {o : Nat → O} {t t' t'' : Nat} (h : SameAhead o t t')
    (h' : SameAhead o t' t'') : SameAhead o t t'' := fun n => (h n).trans (h' n)

theorem SameAhead.next {o : Nat → O} {t t' : Nat} (h : SameAhead o t t') :
    SameAhead o (t + 1) (t' + 1) := fun n =>
  (congrArg o (Nat.succ_add t n)).trans ((h (n + 1)).trans (congrArg o (Nat.succ_add t' n)).symm)

/-- An unfolding that never registers the same twice has no recurring state. -/
theorem new_each_moment {t t' : Nat} (h : SameAhead (fun t : Nat => t) t t') : t = t' := h 0

theorem liar_zero_two : SameAhead liar 0 2 := fun n =>
  (congrArg liar (Nat.zero_add n)).trans ((liar_returns n).symm.trans (congrArg liar (Nat.add_comm n 2)))

/-- The simplest rhythm has exactly two states, each the other's next. -/
theorem liar_two_states :
    (¬ SameAhead liar 0 1) ∧ SameAhead liar 0 2 ∧ ∀ t, SameAhead liar t 0 ∨ SameAhead liar t 1 := by
  refine ⟨(fun h => nomatch (h 0)), liar_zero_two, ?_⟩
  intro t
  induction t with
  | zero => exact .inl (fun _ => rfl)
  | succ t ih =>
    match ih with
    | .inl h0 => exact .inr h0.next
    | .inr h1 => exact .inl (h1.next.trans liar_zero_two.symm)

/-- Each of the two is defined through the other: one registers `true` and goes into the other,
which registers `false` and goes into the first. -/
theorem liar_each_through_other (t : Nat) :
    (SameAhead liar t 0 → liar t = true ∧ SameAhead liar (t + 1) 1) ∧
      (SameAhead liar t 1 → liar t = false ∧ SameAhead liar (t + 1) 0) :=
  ⟨fun h => ⟨h 0, h.next⟩, fun h => ⟨h 0, h.next.trans liar_zero_two.symm⟩⟩

end Moments

/-! ## 9. What makes a split make sense -/

section MakingSense
variable {S : Type u} {O : Type v} {K : Type w}

/-- A split makes sense, relative to what is registered, when it keeps every difference that will
make a difference there and adds none that never will. -/
def MakesSense (next : S → S) (o : S → O) (π : S → K) : Prop :=
  ∀ s s', π s = π s' ↔ SameFuture next o s s'

/-- It loses nothing that is registered, now or later. -/
theorem MakesSense.sufficient {next : S → S} {o : S → O} {π : S → K}
    (h : MakesSense next o π) : Sufficient next o π := fun s s' e => (h s s').mp e

/-- The law comes out of it: what it lumps goes on lumped. -/
theorem MakesSense.carries {next : S → S} {o : S → O} {π : S → K}
    (h : MakesSense next o π) : CarriesLaw next π :=
  fun s s' e => (h (next s) (next s')).mpr ((h s s').mp e).goes

/-- Any two splits that make sense lump exactly the same configurations. -/
theorem MakesSense.unique {next : S → S} {o : S → O} {π : S → K} {π' : S → K}
    (h : MakesSense next o π) (h' : MakesSense next o π') : ∀ s s', π s = π s' ↔ π' s = π' s' :=
  fun s s' => (h s s').trans (h' s s').symm

/-- A split that keeps what is registered now, carries a law, and lumps configurations whose
registered futures are alike, makes sense. -/
theorem MakesSense.of_law {next : S → S} {o : S → O} {π : S → K}
    (keeps : ∀ s s', π s = π s' → o s = o s') (law : CarriesLaw next π)
    (idle : ∀ s s', SameFuture next o s s' → π s = π s') : MakesSense next o π :=
  fun s s' => ⟨SameFuture.greatest (fun s s' => π s = π s') keeps law s s', idle s s'⟩

/-- What is registered now makes sense alone exactly where configurations registered alike now
are registered alike from then on: where now fixes its own registered future. -/
theorem MakesSense.now_alone_iff {next : S → S} {o : S → O} :
    MakesSense next o o ↔ ∀ s s', o s = o s' → SameFuture next o s s' :=
  ⟨fun h s s' e => (h s s').mp e, fun h s s' => ⟨h s s', SameFuture.registered⟩⟩

end MakingSense

/-- Where the standing changes by the passing, the pair makes sense and neither alone does; where
nothing passes, standing alone makes sense. -/
theorem pair_makes_sense :
    MakesSense move Prod.fst (fun s : Nat × Nat => s) ∧ ¬ MakesSense move Prod.fst Prod.fst ∧
      ¬ MakesSense move Prod.fst Prod.snd ∧ MakesSense still Prod.fst Prod.fst :=
  ⟨fun ⟨x, v⟩ ⟨x', v'⟩ =>
      ⟨fun e => match e with | rfl => SameFuture.refl move Prod.fst (x, v),
       fun h => match (pair_canonical x v x' v').mp h with | ⟨rfl, rfl⟩ => rfl⟩,
   fun h => standing_alone.2 h.sufficient,
   fun h => passing_alone h.sufficient,
   fun s s' => (still_canonical s s').symm⟩

/-! ## 10. Three boxes: views that agree where they meet and are not one view

Specker's parable (1960): of three boxes any two may be opened together, and exactly one of the two
opened holds the gem. -/

/-- The three ways to open two of the boxes `a`, `b`, `c`. -/
inductive Opening where
  | ab
  | bc
  | ca

/-- A reading of what each opening shows: the first and the second box opened. Each opening shows
exactly one gem. -/
def Shows (seen : Opening → Bool × Bool) : Prop := ∀ p, (seen p).1 ≠ (seen p).2

/-- The views agree where they meet: in every opening either box may show either way. -/
theorem views_agree (v : Bool) : (∃ w : Bool, v ≠ w) ∧ (∃ w : Bool, w ≠ v) :=
  match v with
  | true => ⟨⟨false, fun h => nomatch h⟩, ⟨false, fun h => nomatch h⟩⟩
  | false => ⟨⟨true, fun h => nomatch h⟩, ⟨true, fun h => nomatch h⟩⟩

/-- Read with its opening, every box has a definite showing in every view. -/
theorem shown_in_context : ∃ seen : Opening → Bool × Bool, Shows seen :=
  ⟨fun _ => (true, false), fun _ h => nomatch h⟩

/-- Read as one view, no reading fits: some box shows differently in two openings. -/
theorem not_one_view (seen : Opening → Bool × Bool) (h : Shows seen) :
    ¬ ((seen .ab).1 = (seen .ca).2 ∧ (seen .ab).2 = (seen .bc).1 ∧ (seen .bc).2 = (seen .ca).1) :=
  fun ⟨ea, eb, ec⟩ => three_do_not (seen .ab).1 (seen .ab).2 (seen .bc).2
    ⟨h .ab, fun e => h .bc (eb.symm.trans e), fun e => h .ca (ec.symm.trans (e.trans ea))⟩

end Saying

#print axioms Saying.cancel
#print axioms Saying.flip_moves
#print axioms Saying.separated_of_whole
#print axioms Saying.separation_faithful_iff
#print axioms Saying.same_separated
#print axioms Saying.whole_not_in_pairs
#print axioms Saying.gap_unsaid
#print axioms Saying.Says.congr
#print axioms Saying.complete_iff_no_difference
#print axioms Saying.Unfolds.keeps_on
#print axioms Saying.Unfolds.incomplete
#print axioms Saying.Unfolds.gap_new
#print axioms Saying.Unfolds.gaps_differ
#print axioms Saying.Unfolds.never_returns
#print axioms Saying.lt_split
#print axioms Saying.two_ne_odd
#print axioms Saying.finite_stock
#print axioms Saying.Unfolds.unheld
#print axioms Saying.unfolding_fresh
#print axioms Saying.unfolding_zero
#print axioms Saying.unfolds
#print axioms Saying.unfolding_open
#print axioms Saying.not_not'
#print axioms Saying.liar_moves
#print axioms Saying.liar_returns
#print axioms Saying.any_two_hold
#print axioms Saying.three_do_not
#print axioms Saying.SameFuture.refl
#print axioms Saying.SameFuture.symm
#print axioms Saying.SameFuture.trans
#print axioms Saying.SameFuture.registered
#print axioms Saying.SameFuture.goes
#print axioms Saying.SameFuture.greatest
#print axioms Saying.const_carries
#print axioms Saying.const_sufficient_iff
#print axioms Saying.pair_canonical
#print axioms Saying.standing_alone
#print axioms Saying.passing_alone
#print axioms Saying.orbit_still
#print axioms Saying.still_canonical
#print axioms Saying.SameAhead.symm
#print axioms Saying.SameAhead.trans
#print axioms Saying.SameAhead.next
#print axioms Saying.new_each_moment
#print axioms Saying.liar_zero_two
#print axioms Saying.liar_two_states
#print axioms Saying.liar_each_through_other
#print axioms Saying.MakesSense.sufficient
#print axioms Saying.MakesSense.carries
#print axioms Saying.MakesSense.unique
#print axioms Saying.MakesSense.of_law
#print axioms Saying.MakesSense.now_alone_iff
#print axioms Saying.pair_makes_sense
#print axioms Saying.views_agree
#print axioms Saying.shown_in_context
#print axioms Saying.not_one_view
