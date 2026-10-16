import Becoming.Openness

namespace Becoming

/-! ## How much change enclosure allows -/

/-- How many steps from `T` before `t` a quantity is positive at. -/
def since (T : Nat) (q : Nat → Nat) : Nat → Nat
  | 0 => 0
  | t + 1 => since T q t + mark (T ≤ t ∧ 0 < q t)

theorem since_before {T : Nat} {q : Nat → Nat} : ∀ {t : Nat}, t ≤ T → since T q t = 0
  | 0, _ => rfl
  | _ + 1, early => (congrArg (since T q _ + ·) (mark_zero fun later =>
      Nat.lt_irrefl _ (Nat.lt_of_lt_of_le early later.1))).trans (since_before
        (Nat.le_of_lt early))

theorem since_succ {T t : Nat} (q : Nat → Nat) (later : T ≤ t) :
    since T q (t + 1) = since T q t + mark (0 < q t) :=
  congrArg (since T q t + ·) (mark_iff ⟨And.right, fun positive => ⟨later, positive⟩⟩)

theorem since_mono {T : Nat} (q : Nat → Nat) {t : Nat} :
    ∀ {s : Nat}, t ≤ s → since T q t ≤ since T q s
  | _, .refl => Nat.le_refl _
  | _ + 1, .step within => Nat.le_trans (since_mono q within) (Nat.le_add_right _ _)

/-- A quantity that never rises from step `T` on, and falls at each step at which `q` is
positive, has fallen from its value at `T` by at least the number of those steps. -/
theorem falls_within (r q : Nat → Nat) {T : Nat}
    (falls : ∀ t, T ≤ t → r (t + 1) + mark (0 < q t) ≤ r t) :
    ∀ {t}, T ≤ t → r t + since T q t ≤ r T
  | _, .refl => Nat.le_of_eq ((congrArg (r T + ·) (since_before (Nat.le_refl T))).trans
      (Nat.add_zero _))
  | m + 1, .step later => Nat.le_trans (Nat.le_of_eq ((congrArg (r (m + 1) + ·)
      (since_succ q later)).trans ((Nat.add_assoc _ _ _).symm.trans
        (Nat.add_right_comm _ _ _))))
      (Nat.le_trans (Nat.add_le_add_right (falls m later) _) (falls_within r q falls later))

/-- From step `T`, the number active and the steps at which something ceases or arises stay
within `B` together. -/
def Settles (T B : Nat) (n c a : Nat → Nat) : Prop :=
  ∀ t, T ≤ t → n t + since T (fun s => c s + a s) t ≤ B

/-- Settling, change does not recur. -/
theorem Settles.rests {T B : Nat} {n c a : Nat → Nat} (settles : Settles T B n c a) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ 0 < c t + a t :=
  fun recurs =>
    have more : ∀ m, ∃ t, T ≤ t ∧ m ≤ since T (fun s => c s + a s) t := fun m =>
      Nat.rec ⟨T, Nat.le_refl T, Nat.zero_le _⟩ (fun _ ⟨t, later, many⟩ =>
        match recurs t with
        | ⟨s, after, changes⟩ => ⟨s + 1, Nat.le_trans later (Nat.le_trans after
            (Nat.le_add_right s 1)), Nat.le_trans (Nat.add_le_add_right many 1)
            (Nat.le_trans (Nat.add_le_add_right (since_mono _ after) 1)
              (Nat.le_of_eq ((congrArg (since T _ s + ·) (mark_one changes)).symm.trans
                (since_succ _ (Nat.le_trans later after)).symm)))⟩) m
    match more (B + 1) with
    | ⟨t, later, many⟩ => Nat.lt_irrefl B (Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le
        (Nat.lt_succ_self B) many) (Nat.le_trans (Nat.le_add_left _ _) (settles t later)))

/-! ## Counting under enclosure -/

/-- What each has beyond the other, added to it, gives the same. -/
theorem add_sub_turn : ∀ x y : Nat, y + (x - y) = x + (y - x)
  | 0, y => (congrArg (y + ·) (Nat.zero_sub y)).trans (Nat.zero_add y).symm
  | x + 1, 0 => (Nat.zero_add (x + 1)).trans (congrArg (x + 1 + ·) (Nat.zero_sub (x + 1))).symm
  | x + 1, y + 1 => (congrArg (y + 1 + ·) (Nat.succ_sub_succ x y)).trans
      ((Nat.add_right_comm y 1 (x - y)).trans ((congrArg (· + 1) (add_sub_turn x y)).trans
        ((Nat.add_right_comm x (y - x) 1).trans
          (congrArg (x + 1 + ·) (Nat.succ_sub_succ y x).symm))))

theorem sub_eq_zero_of_le : ∀ {m k : Nat}, m ≤ k → m - k = 0
  | 0, k, _ => Nat.zero_sub k
  | _ + 1, 0, le => absurd le (Nat.not_succ_le_zero _)
  | m + 1, k + 1, le =>
    (Nat.succ_sub_succ m k).trans (sub_eq_zero_of_le (Nat.le_of_succ_le_succ le))

theorem add_sub_of_le {m k : Nat} (le : m ≤ k) : m + (k - m) = k :=
  (add_sub_turn k m).trans (congrArg (k + ·) (sub_eq_zero_of_le le))

theorem le_sub_of_add_le {m u B : Nat} (le : m + u ≤ B) : m ≤ B - u :=
  le_of_add_le_add_right u (Nat.le_trans le (Nat.le_of_eq
    ((add_sub_of_le (Nat.le_trans (Nat.le_add_left u m) le)).symm.trans (Nat.add_comm _ _))))

instance Tended.decideEq : DecidableEq Tended.Relatum
  | .member a, .member b => if same : a = b then .isTrue (congrArg _ same)
      else .isFalse fun eq => same (Tended.member_inj a b eq)
  | .ground a, .ground b => if same : a = b then .isTrue (congrArg _ same)
      else .isFalse fun eq => same (Tended.Relatum.noConfusion eq id)
  | .member _, .ground _ => .isFalse fun eq => Tended.Relatum.noConfusion eq
  | .ground _, .member _ => .isFalse fun eq => Tended.Relatum.noConfusion eq

namespace Closing

variable (n c a : Nat → Nat) (T B : Nat)

/-- From step `T` on, what stands: `B`, less one for each step from `T` at which something
ceases or arises. -/
def store (t : Nat) : Nat :=
  B - since T (fun s => c s + a s) t

/-- What the store holds beyond one for each member, from step `T` on. -/
def spare (t : Nat) : Nat :=
  if T ≤ t then store c a T B t - n t else 0

/-- Standing in a queue whose front is `g` and which holds `m`: one, and `s` more at the
front. -/
def place (g m s k : Nat) : Nat :=
  if g ≤ k ∧ k < g + m then 1 + (if k = g then s else 0) else 0

/-- Members stand by their place in the queue, the front holding the spare; ground relata
stand at nothing. -/
def level (t : Nat) : Tended.Relatum → Nat
  | .member k => place (Queue.gone c t) (n t) (spare n c a T B t) k
  | .ground _ => 0

/-- Before step `T`, while the queue is not empty, the front exchanges one unit each way with
every ground relatum. -/
def exchange (t : Nat) : Tended.Relatum → Nat
  | .member _ => 0
  | .ground _ => mark (t < T ∧ 0 < n t)

/-- The queue's web, with these levels. -/
def web : Web Tended.Relatum Tended.Relatum :=
  { Tended.web n c with level := level n c a T B }

/-- The front takes part at every step. It takes from each relatum what it loses and gives
each what it gains, with the exchange with the ground. -/
def flow : Flow Tended.Relatum Tended.Relatum where
  present t := [.member (Queue.gone c t)]
  take t _ x := level n c a T B t x - level n c a T B (t + 1) x + exchange n T t x
  give t _ x := level n c a T B (t + 1) x - level n c a T B t x + exchange n T t x

/-- The members in the queue before or after the step from `t`. -/
def span (t : Nat) : List Tended.Relatum :=
  (steps (Queue.gone c t) (n t + a t)).map .member

variable {n c a : Nat → Nat} {T B : Nat}

theorem place_pos {g m s k : Nat} : (g ≤ k ∧ k < g + m) ↔ 0 < place g m s k :=
  if h : g ≤ k ∧ k < g + m then
    ⟨fun _ => Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_add_right 1 _))
      (Nat.le_of_eq (if_pos h).symm), fun _ => h⟩
  else
    ⟨fun holds => absurd holds h,
     fun pos => absurd (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (if_neg h))) (Nat.lt_irrefl 0)⟩

theorem place_zero {g m s k : Nat} (out : ¬ (g ≤ k ∧ k < g + m)) : place g m s k = 0 :=
  if_neg out

/-- A queue of `m + 1` stands at `m + 1`, and `s` more at its front. -/
theorem total_place (g m s : Nat) : total (steps g (m + 1)) (place g (m + 1) s) = m + 1 + s :=
  have front : place g (m + 1) s g = 1 + s :=
    (if_pos ⟨Nat.le_refl g, Nat.lt_add_of_pos_right (Nat.succ_pos m)⟩).trans
      (congrArg (1 + ·) (if_pos rfl))
  have rest : total (steps (g + 1) m) (place g (m + 1) s) = m :=
    (total_congr_on (g := fun _ => 1) fun _ mem =>
      (if_pos ⟨Nat.le_of_succ_le (steps_mem mem), Nat.lt_of_lt_of_le (steps_within mem)
        (Nat.le_of_eq (Nat.add_right_comm g 1 m))⟩).trans
        (congrArg (1 + ·) (if_neg fun same => Nat.lt_irrefl g (Nat.lt_of_lt_of_le
          (Nat.lt_succ_self g) (Nat.le_trans (steps_mem mem) (Nat.le_of_eq same)))))).trans
      ((total_ones _).trans (steps_length _ _))
  (congrArg (· + _) front).trans ((congrArg (1 + s + ·) rest).trans
    ((Nat.add_right_comm 1 s m).trans ((congrArg (· + s) (Nat.add_comm 1 m)))))

/-- Where a relatum's standing does not change and nothing is exchanged with it, the front
neither takes from nor gives to it. -/
theorem still_flows {t : Nat} {x f : Tended.Relatum}
    (same : level n c a T B (t + 1) x = level n c a T B t x) (none : exchange n T t x = 0) :
    (flow n c a T B).take t f x = 0 ∧ (flow n c a T B).give t f x = 0 :=
  ⟨(congrArg (fun l => level n c a T B t x - l + exchange n T t x) same).trans
     ((congrArg (· + exchange n T t x) (Nat.sub_self _)).trans ((Nat.zero_add _).trans none)),
   (congrArg (fun l => l - level n c a T B t x + exchange n T t x) same).trans
     ((congrArg (· + exchange n T t x) (Nat.sub_self _)).trans ((Nat.zero_add _).trans none))⟩

theorem still {t : Nat} {x f : Tended.Relatum}
    (flows : (flow n c a T B).take t f x = 0 ∧ (flow n c a T B).give t f x = 0) :
    ¬ (0 < (flow n c a T B).take t f x ∨ 0 < (flow n c a T B).give t f x)
  | .inl takes => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le takes (Nat.le_of_eq flows.1))
  | .inr gives => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le gives (Nat.le_of_eq flows.2))

/-- An empty queue stays empty where nothing joins an empty queue. -/
theorem empty_stays (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) {t : Nat}
    (empty : n t = 0) : n (t + 1) = 0 :=
  match tally t with
  | ⟨k, before, after⟩ =>
    have kept : k = 0 := Nat.eq_zero_of_le_zero
      (Nat.le_trans (Nat.le_add_right k (c t)) (Nat.le_of_eq (before.symm.trans empty)))
    have none : a t = 0 := eq_zero_of_not_pos fun joins =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (company t joins) (Nat.le_of_eq empty))
    after.trans ((congrArg (· + a t) kept).trans ((Nat.zero_add _).trans none))

theorem outside_empty {k t : Nat} (empty : n t = 0) : ¬ Queue.holds n c k t :=
  fun holds => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (Tended.occupied holds) (Nat.le_of_eq empty))

/-- Across a step from an empty queue nothing is taken or given. -/
theorem idle (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) {t : Nat}
    (empty : n t = 0) (x f : Tended.Relatum) :
    (flow n c a T B).take t f x = 0 ∧ (flow n c a T B).give t f x = 0 :=
  have zero : ∀ s, n s = 0 → level n c a T B s x = 0 := fun _ none => match x with
    | .member _ => place_zero (outside_empty none)
    | .ground _ => rfl
  still_flows ((zero _ (empty_stays tally company empty)).trans (zero _ empty).symm)
    (match x with
      | .member _ => rfl
      | .ground _ => mark_zero fun early =>
          Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le early.2 (Nat.le_of_eq empty)))

/-- From step `T` on, across a step at which nothing ceases or arises nothing changes. -/
theorem quiet_same (tally : Tally n c a) {t : Nat} (later : T ≤ t) (quiet : c t + a t = 0)
    (x : Tended.Relatum) : level n c a T B (t + 1) x = level n c a T B t x :=
  have ceased : c t = 0 :=
    Nat.eq_zero_of_le_zero (Nat.le_trans (Nat.le_add_right _ _) (Nat.le_of_eq quiet))
  have joined : a t = 0 :=
    Nat.eq_zero_of_le_zero (Nat.le_trans (Nat.le_add_left _ _) (Nat.le_of_eq quiet))
  have front : Queue.gone c (t + 1) = Queue.gone c t :=
    (Queue.gone_succ t).trans (congrArg (_ + ·) ceased)
  have size : n (t + 1) = n t := match tally t with
    | ⟨_, before, after⟩ => after.trans ((congrArg (_ + ·) joined).trans
        ((congrArg (_ + ·) ceased).symm.trans before.symm))
  have spared : spare n c a T B (t + 1) = spare n c a T B t :=
    (if_pos (Nat.le_succ_of_le later)).trans
      ((congrArg (fun m => store c a T B (t + 1) - m) size).trans
        ((congrArg (fun u => B - u - n t) ((since_succ _ later).trans (congrArg (_ + ·)
          (mark_zero fun changes => Nat.lt_irrefl 0
            (Nat.lt_of_lt_of_le changes (Nat.le_of_eq quiet)))))).trans (if_pos later).symm))
  match x with
  | .member k =>
    (congrArg (fun g => place g (n (t + 1)) (spare n c a T B (t + 1)) k) front).trans
      ((congrArg (fun m => place (Queue.gone c t) m (spare n c a T B (t + 1)) k) size).trans
        (congrArg (fun s => place (Queue.gone c t) (n t) s k) spared))
  | .ground _ => rfl

/-- What is in the queue before or after a step lies in its span. -/
theorem within_span (tally : Tally n c a) {t k : Nat}
    (holds : Queue.holds n c k t ∨ Queue.holds n c k (t + 1)) :
    Tended.Relatum.member k ∈ span n c a t :=
  mem_map_of (match tally t, holds with
    | _, .inl now => steps_of_within now.1
        (Nat.lt_of_lt_of_le now.2 (Nat.add_le_add_left (Nat.le_add_right _ _) _))
    | ⟨_, before, after⟩, .inr next => steps_of_within
        (Nat.le_trans (Nat.le_trans (Nat.le_add_right _ (c t))
          (Nat.le_of_eq (Queue.gone_succ t).symm)) next.1)
        (Nat.lt_of_lt_of_le next.2 (Nat.le_of_eq ((congrArg (_ + ·) after).trans
          ((Nat.add_assoc _ _ _).symm.trans ((congrArg (· + a t) (Queue.kept_end before).symm).trans
            (Nat.add_assoc _ _ _)))))))

/-- From step `T` on, whatever the front takes from or gives to lies in the span. -/
theorem moving_within (tally : Tally n c a) {t : Nat} (later : T ≤ t) {f x : Tended.Relatum}
    (moves : 0 < (flow n c a T B).take t f x ∨ 0 < (flow n c a T B).give t f x) :
    x ∈ span n c a t :=
  match x, moves with
  | .member k, moves =>
    if now : Queue.holds n c k t then within_span tally (.inl now)
    else if next : Queue.holds n c k (t + 1) then within_span tally (.inr next)
    else absurd moves (still (still_flows ((place_zero next).trans (place_zero now).symm) rfl))
  | .ground _, moves => absurd moves (still (still_flows rfl
      (mark_zero fun early => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le early.1 later))))

/-- From step `T` on, each step is enclosed by its span. -/
theorem closed (tally : Tally n c a) {t : Nat} (later : T ≤ t) :
    (flow n c a T B).ClosedAt (span n c a t) t :=
  fun _ _ _ out => ⟨eq_zero_of_not_pos fun takes => out (moving_within tally later (.inl takes)),
    eq_zero_of_not_pos fun gives => out (moving_within tally later (.inr gives))⟩

theorem span_distinct (t : Nat) : Distinct (span n c a t) :=
  distinct_map Tended.member_inj (steps_distinct _ _)

/-- Something taken or given means the queue is not empty. -/
theorem busy (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) {t : Nat}
    {f x : Tended.Relatum}
    (moves : 0 < (flow n c a T B).take t f x ∨ 0 < (flow n c a T B).give t f x) : 0 < n t :=
  match Nat.eq_zero_or_pos (n t) with
  | .inl empty => absurd moves (still (idle tally company empty x f))
  | .inr occupied => occupied

end Closing

namespace World

variable {w : World}

theorem length_le_stock {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (embodied : w.Embodied) (t : Nat) : (alive t).length ≤ w.web.stock (alive t) t :=
  Nat.le_trans (Nat.le_of_eq (total_ones (alive t)).symm) (total_le (alive t) fun x mem =>
    (embodied x t).mp (((census t).2 x).mpr mem))

/-- Enclosure bounds change. In a world with a census whose relata are embodied, with a
balanced, dissipative flow, in which every step from `T` on is enclosed, the relata active
at any later step, with the steps from `T` at which something arises or ceases, number at
most the total standing at `T`. -/
theorem change_within [∀ t x, Decidable (w.web.active t x)] {alive : Nat → List w.Relatum}
    (census : w.web.Census alive) (embodied : w.Embodied) (balanced : w.Balanced)
    (dissipative : w.Dissipative) {T : Nat} (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) :
    Settles T (w.web.stock (alive T) T) (fun t => (alive t).length)
      (fun t => ceasings (alive t) (fun x s => w.web.active s x) t)
      (fun t => comings (alive (t + 1)) (fun x s => w.web.active s x) t) :=
  have standing := standingCensus census embodied
  fun _ later => Nat.le_trans (Nat.add_le_add_right (length_le_stock census embodied _) _)
    (falls_within (fun t => w.web.stock (alive t) t) _ (fun t later =>
      Decidable.of_not_not fun no => (enclosed t later).aroundStanding_not_not alive
        fun around => no (match Nat.eq_zero_or_pos (ceasings (alive t)
            (fun x s => w.web.active s x) t + comings (alive (t + 1))
            (fun x s => w.web.active s x) t) with
          | .inl quiet => Nat.le_trans (Nat.le_of_eq (congrArg (_ + ·) (mark_zero
              fun positive => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le positive
                (Nat.le_of_eq quiet)))))
              (Flow.standing_never_rises balanced dissipative standing around)
          | .inr changes =>
            have lowers : ∃ x, w.web.Rises t x ∨ w.web.Falls t x :=
              match Nat.eq_zero_or_pos (ceasings (alive t) (fun x s => w.web.active s x) t) with
              | .inr ceasing => match total_pos _ ceasing with
                | ⟨x, _, ceases⟩ => ⟨x, .inr (falls_of_ceases embodied (mark_pos.mp ceases))⟩
              | .inl still => match total_pos _ (Nat.lt_of_lt_of_le changes (Nat.le_of_eq
                  ((congrArg (· + _) still).trans (Nat.zero_add _)))) with
                | ⟨x, _, comes⟩ => ⟨x, .inl (rises_of_arises embodied (mark_pos.mp comes))⟩
            match lowers with
            | ⟨_, change⟩ => Nat.le_trans (Nat.le_of_eq (congrArg (_ + ·) (mark_one changes)))
                (Flow.change_lowers balanced dissipative standing around change)))
      later)

/-- A queue tended by its front and closed from step `T`. Before `T` the front exchanges with
the ground while the queue is not empty; from `T` on it exchanges only within the queue, whose
store falls by one at each step at which a member joins or leaves. -/
def closingQueue (n c a : Nat → Nat) (T B : Nat) : World :=
  ⟨Tended.Relatum, Closing.flow n c a T B, Closing.web n c a T B⟩

instance closingQueue_decided (n c a : Nat → Nat) (T B : Nat) :
    ∀ t x, Decidable ((closingQueue n c a T B).web.active t x) :=
  tendedQueue_decided n c

theorem closingQueue_census (n c a : Nat → Nat) (T B : Nat) :
    (closingQueue n c a T B).web.Census fun t => (Queue.line n c t).map .member :=
  tendedQueue_census n c

theorem closingQueue_embodied (n c a : Nat → Nat) (T B : Nat) :
    (closingQueue n c a T B).Embodied
  | .member _ => fun _ => Closing.place_pos
  | .ground _ => fun _ => ⟨False.elim, fun pos => absurd pos (Nat.lt_irrefl 0)⟩

theorem closingQueue_balanced (n c a : Nat → Nat) (T B : Nat) :
    (closingQueue n c a T B).Balanced :=
  fun t x =>
    (Nat.add_assoc (Closing.level n c a T B (t + 1) x) _ (Closing.exchange n T t x)).symm.trans
      ((congrArg (· + Closing.exchange n T t x) (add_sub_turn (Closing.level n c a T B t x)
        (Closing.level n c a T B (t + 1) x))).trans (Nat.add_assoc _ _ _))

variable {n c a : Nat → Nat} {T B : Nat}

theorem closingQueue_acting (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) :
    (closingQueue n c a T B).Acting :=
  fun _ f _ present gives => match f, present, gives with
    | _, .head _, gives => Tended.front.mpr (Closing.busy tally company (.inr gives))
    | _, .tail _ no, _ => (nomatch no)

theorem closingQueue_taking (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) :
    (closingQueue n c a T B).Taking :=
  fun _ f _ present takes => match f, present, takes with
    | _, .head _, takes => ⟨Tended.front.mpr (Closing.busy tally company (.inl takes)), trivial⟩
    | _, .tail _ no, _ => (nomatch no)

/-- From step `T` on, a settling queue's store holds what stands. -/
theorem closingQueue_stock {t : Nat} (later : T ≤ t) (fits : n t ≤ Closing.store c a T B t) :
    (closingQueue n c a T B).web.stock ((Queue.line n c t).map .member) t ≤
        Closing.store c a T B t ∧
      (0 < n t → (closingQueue n c a T B).web.stock ((Queue.line n c t).map .member) t =
        Closing.store c a T B t) :=
  have whole : ∀ m, n t = m + 1 →
      (closingQueue n c a T B).web.stock ((Queue.line n c t).map .member) t =
        Closing.store c a T B t := fun m size =>
    (total_map _ _ _).trans ((congrArg (fun k => total (steps (Queue.gone c t) k)
      (Closing.place (Queue.gone c t) k (Closing.spare n c a T B t))) size).trans
      ((Closing.total_place _ m _).trans ((congrArg (· + _) size.symm).trans
        ((congrArg (n t + ·) (if_pos later)).trans (add_sub_of_le fits)))))
  match Nat.eq_zero_or_pos (n t) with
  | .inl empty => ⟨Nat.le_trans (Nat.le_of_eq ((total_map _ _ _).trans
      (congrArg (fun k => total (steps (Queue.gone c t) k)
        (Closing.place (Queue.gone c t) k (Closing.spare n c a T B t))) empty)))
      (Nat.zero_le _), fun occupied => absurd (empty ▸ occupied) (Nat.lt_irrefl 0)⟩
  | .inr occupied => ⟨Nat.le_of_eq (whole _ (Nat.succ_pred_eq_of_pos occupied).symm),
      fun _ => whole _ (Nat.succ_pred_eq_of_pos occupied).symm⟩

theorem closingQueue_dissipative (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (settles : Settles T B n c a) : (closingQueue n c a T B).Dissipative :=
  fun cs t distinct closed f present =>
    have still : (∀ x, (Closing.flow n c a T B).take t f x = 0 ∧
        (Closing.flow n c a T B).give t f x = 0) →
        total cs ((Closing.flow n c a T B).give t f) +
          sign (total cs ((Closing.flow n c a T B).take t f)) ≤
            total cs ((Closing.flow n c a T B).take t f) := fun flows =>
      Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (total_eq_zero fun x _ => (flows x).2)).trans
        ((Nat.zero_add _).trans (congrArg sign (total_eq_zero fun x _ => (flows x).1)))))
        (Nat.zero_le _)
    match Nat.eq_zero_or_pos (n t), Nat.lt_or_ge t T with
    | .inl empty, _ => still fun x => Closing.idle tally company empty x f
    | .inr occupied, .inl early => absurd ((mark_one ⟨early, occupied⟩).symm.trans
        ((Nat.zero_add _).symm.trans (closed f present _ (Tended.outside cs)).1))
        (fun no => Nat.noConfusion no)
    | .inr occupied, .inr later => match Nat.eq_zero_or_pos (c t + a t) with
      | .inl quiet => still fun x => Closing.still_flows (Closing.quiet_same tally later quiet x)
          (match x with
            | .member _ => rfl
            | .ground _ => mark_zero fun early =>
                Nat.lt_irrefl _ (Nat.lt_of_lt_of_le early.1 later))
      | .inr changes =>
        have census := closingQueue_census n c a T B
        have standing := standingCensus census (closingQueue_embodied n c a T B)
        have fits : ∀ s, T ≤ s → n s ≤ Closing.store c a T B s := fun s after =>
          le_sub_of_add_le (settles s after)
        have before := standing.stock_eq (Closing.span_distinct t) fun x mem =>
          match x, ((census t).2 x).mpr mem with
          | .member _, holds => Closing.within_span tally (.inl holds)
        have after := standing.stock_eq (t := t + 1) (Closing.span_distinct t) fun x mem =>
          match x, ((census (t + 1)).2 x).mpr mem with
          | .member _, holds => Closing.within_span tally (.inr holds)
        have spent : Closing.store c a T B (t + 1) + 1 ≤ Closing.store c a T B t :=
          Nat.le_of_eq ((congrArg (fun u => B - u + 1) ((since_succ _ later).trans
            (congrArg (_ + ·) (mark_one changes)))).trans (Nat.succ_pred_eq_of_pos
              (Nat.lt_of_lt_of_le occupied (fits t later))))
        have lowered := Nat.le_trans (Nat.add_le_add_right (Nat.le_trans (Nat.le_of_eq after.symm)
            (closingQueue_stock (Nat.le_succ_of_le later)
              (fits _ (Nat.le_succ_of_le later))).1) 1)
          (Nat.le_trans spent (Nat.le_of_eq (((closingQueue_stock later (fits t later)).2
            occupied).symm.trans before)))
        have over := (closingQueue_balanced n c a T B).over (Closing.span n c a t) t
        have exceeds : total (Closing.span n c a t) ((Closing.flow n c a T B).give t f) + 1 ≤
            total (Closing.span n c a t) ((Closing.flow n c a T B).take t f) :=
          le_of_add_le_add_right _ (Nat.le_trans (Nat.le_of_eq ((Nat.add_assoc _ _ _).trans
            (congrArg (_ + ·) (Nat.add_comm _ _)))) (Nat.le_trans (Nat.add_le_add_left lowered _)
              (Nat.le_of_eq ((Nat.add_comm _ _).trans (over.symm.trans (Nat.add_comm _ _))))))
        Nat.le_trans (Nat.add_le_add (total_le_of_support distinct fun _ _ gives =>
            Closing.moving_within tally later (.inr gives)) (sign_le_one _))
          (Nat.le_trans exceeds (total_le_of_support (Closing.span_distinct t) fun x _ takes =>
            match decideMem x cs with
            | .isTrue mem => mem
            | .isFalse out => absurd (Nat.lt_of_lt_of_le takes
                (Nat.le_of_eq (closed f present x out).1)) (Nat.lt_irrefl 0)))

theorem closingQueue_premised (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (settles : Settles T B n c a) : (closingQueue n c a T B).Premised :=
  .of (fun _ _ _ _ no => (nomatch no)) (closingQueue_balanced n c a T B)
    (closingQueue_acting tally company) (closingQueue_taking tally company)
    (closingQueue_dissipative tally company settles) (closingQueue_embodied n c a T B)
    ⟨_, closingQueue_census n c a T B⟩ ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩

/-- From step `T` on, each step of a closing queue is enclosed. -/
theorem closingQueue_enclosed (tally : Tally n c a) :
    ∀ t, T ≤ t → (closingQueue n c a T B).flow.Enclosed t :=
  fun t later => ⟨Closing.span n c a t, Closing.span_distinct t, Closing.closed tally later⟩

/-- Under all eight premises, with every step from some step on enclosed, the laws of
counting are the balance, that nothing arises across a step at which nothing is active, and
that the counts settle: from some step on, the number active and the steps at which
something ceases or arises stay within a bound together. -/
theorem enclosed_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ T B, Settles T B n c a) →
      Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
        (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q :=
  ⟨fun law w _ premised ⟨_, enclosed⟩ alive census =>
    law _ _ _ census.tally
      (counting_binds_jointly.1 w (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.head _))))
        (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
          (.head _))))))))
        alive census)
      ⟨_, _, change_within census
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))))
        (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))) enclosed⟩,
   fun law _ _ _ tally company ⟨_, _, settles⟩ => pointwise (tendedQueue_counts tally)
      (law (closingQueue _ _ _ _ _) (closingQueue_premised tally company settles)
        ⟨_, closingQueue_enclosed tally⟩ _ (closingQueue_census _ _ _ _ _))⟩

end World

end Becoming
