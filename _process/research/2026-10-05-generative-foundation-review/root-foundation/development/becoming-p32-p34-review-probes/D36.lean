import D35

namespace Becoming

/-! ## Counting in finite worlds -/

/-- The numbers of a list that are below `K`, as places among `K`. -/
def below (K : Nat) : List Nat → List (Fin K)
  | [] => []
  | k :: l => if h : k < K then ⟨k, h⟩ :: below K l else below K l

theorem fin_eq {K : Nat} : ∀ {i j : Fin K}, i.val = j.val → i = j
  | ⟨_, _⟩, ⟨_, _⟩, rfl => rfl

theorem mem_below {K : Nat} {i : Fin K} : ∀ {l : List Nat}, i ∈ below K l ↔ i.val ∈ l
  | [] => ⟨fun no => (nomatch no), fun no => (nomatch no)⟩
  | k :: l =>
    if h : k < K then
      have unfold : below K (k :: l) = ⟨k, h⟩ :: below K l := dif_pos h
      ⟨fun mem => match mem_cons_cases (Eq.mp (congrArg (i ∈ ·) unfold) mem) with
        | .inl same => Eq.subst (motive := fun v => v ∈ k :: l) (congrArg Fin.val same).symm
            (.head l)
        | .inr mem => .tail k (mem_below.mp mem),
       fun mem => Eq.mpr (congrArg (i ∈ ·) unfold) (match mem_cons_cases mem with
        | .inl same => Eq.subst (motive := fun j => j ∈ (⟨k, h⟩ : Fin K) :: below K l)
            (fin_eq (i := ⟨k, h⟩) (j := i) same.symm) (.head _)
        | .inr mem => .tail _ (mem_below.mpr mem))⟩
    else
      have unfold : below K (k :: l) = below K l := dif_neg h
      ⟨fun mem => .tail k (mem_below.mp (Eq.mp (congrArg (i ∈ ·) unfold) mem)),
       fun mem => Eq.mpr (congrArg (i ∈ ·) unfold) (match mem_cons_cases mem with
        | .inl same => absurd (Eq.subst (motive := fun v => v < K) same i.isLt) h
        | .inr mem => mem_below.mpr mem)⟩

theorem distinct_below {K : Nat} : ∀ {l : List Nat}, Distinct l → Distinct (below K l)
  | [], _ => trivial
  | k :: _, ⟨fresh, distinct⟩ =>
    if h : k < K then
      Eq.mpr (congrArg Distinct (dif_pos h))
        ⟨fun mem => fresh (mem_below.mp mem), distinct_below distinct⟩
    else Eq.mpr (congrArg Distinct (dif_neg h)) (distinct_below distinct)

/-- Over a list of numbers below `K`, a quantity on places totals what it totals on the
numbers. -/
theorem total_below {K : Nat} {q : Fin K → Nat} {g : Nat → Nat} (same : ∀ i, q i = g i.val) :
    ∀ {l : List Nat}, (∀ k, k ∈ l → k < K) → total (below K l) q = total l g
  | [], _ => rfl
  | k :: l, within =>
    (congrArg (fun m => total m q) (dif_pos (within k (.head l)))).trans
      ((congrArg (· + total (below K l) q) (same ⟨k, within k (.head l)⟩)).trans
        (congrArg (g k + ·) (total_below same fun j mem => within j (.tail k mem))))

/-- How far a queue has reached: those gone and those in it are those at the first step and
those joined since. -/
theorem Queue.reached {n c a : Nat → Nat} (tally : Tally n c a) :
    ∀ t, Queue.gone c t + n t = n 0 + total (steps 0 t) a
  | 0 => Nat.zero_add (n 0)
  | t + 1 => match tally t with
    | ⟨_, before, after⟩ => (congrArg (_ + ·) after).trans ((Nat.add_assoc _ _ _).symm.trans
        ((congrArg (· + a t) (Queue.kept_end before).symm).trans
          ((congrArg (· + a t) (Queue.reached tally t)).trans ((Nat.add_assoc _ _ _).trans
            (congrArg (n 0 + ·) ((steps_last a 0 t).trans
              (congrArg (_ + ·) (congrArg a (Nat.zero_add t)))).symm)))))

/-- Settling from the first step, at most `B` join at each of at most `B` steps. -/
theorem Settles.joins {n c a : Nat → Nat} {B : Nat} (tally : Tally n c a)
    (settles : Settles 0 B n c a) :
    ∀ t, total (steps 0 t) a ≤ B * since 0 (fun s => c s + a s) t
  | 0 => Nat.zero_le _
  | t + 1 =>
    have joined : a t ≤ B * mark (0 < c t + a t) := match Nat.eq_zero_or_pos (a t) with
      | .inl zero => Nat.le_trans (Nat.le_of_eq zero) (Nat.zero_le _)
      | .inr joins => match tally t with
        | ⟨_, _, after⟩ => Nat.le_trans (Nat.le_trans (Nat.le_add_left _ _)
            (Nat.le_of_eq after.symm)) (Nat.le_trans (Nat.le_trans (Nat.le_add_right _ _)
              (settles (t + 1) (Nat.zero_le _))) (Nat.le_of_eq ((congrArg (B * ·)
                (mark_one (Nat.lt_of_lt_of_le joins (Nat.le_add_left _ _)))).trans
                  (Nat.mul_one B)).symm))
    Nat.le_trans (Nat.le_of_eq ((steps_last a 0 t).trans
        (congrArg (_ + ·) (congrArg a (Nat.zero_add t)))))
      (Nat.le_trans (Nat.add_le_add (Settles.joins tally settles t) joined)
        (Nat.le_of_eq ((Nat.left_distrib _ _ _).symm.trans
          (congrArg (B * ·) (since_succ _ (Nat.zero_le t)).symm))))

/-- So every member a queue settling from the first step ever holds is below `B + B * B + 1`. -/
theorem Settles.reach {n c a : Nat → Nat} {B : Nat} (tally : Tally n c a)
    (settles : Settles 0 B n c a) (t : Nat) : Queue.gone c t + n t < B + B * B + 1 :=
  Nat.lt_succ_of_le (Nat.le_trans (Nat.le_of_eq (Queue.reached tally t))
    (Nat.add_le_add (settles 0 (Nat.le_refl 0)) (Nat.le_trans (Settles.joins tally settles t)
      (Nat.mul_le_mul_left B (Nat.le_trans (Nat.le_add_left _ _)
        (settles t (Nat.zero_le t)))))))

namespace Closed

variable (n c a : Nat → Nat) (B : Nat)

/-- Room for every member a queue settling from the first step within `B` ever holds
(`Settles.reach`). -/
def size : Nat := B + B * B + 1

/-- The front of the queue where it lies within the room, the first place otherwise. -/
def front (t : Nat) : Fin (size B) :=
  if h : Queue.gone c t < size B then ⟨_, h⟩ else ⟨0, Nat.succ_pos _⟩

/-- The closing queue's web, closed from the first step, on the places of the room. -/
def web : Web (Fin (size B)) (Fin (size B)) where
  level t i := Closing.level n c a 0 B t (.member i.val)
  active t i := Queue.holds n c i.val t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- The closing queue's flow, on the places of the room. -/
def flow : Flow (Fin (size B)) (Fin (size B)) where
  present t := [front c B t]
  take t _ i := (Closing.flow n c a 0 B).take t (.member (Queue.gone c t)) (.member i.val)
  give t _ i := (Closing.flow n c a 0 B).give t (.member (Queue.gone c t)) (.member i.val)

/-- The members in the queue at each step, as places. -/
def alive (t : Nat) : List (Fin (size B)) :=
  below (size B) (Queue.line n c t)

variable {n c a : Nat → Nat} {B : Nat}

theorem front_val (tally : Tally n c a) (settles : Settles 0 B n c a) (t : Nat) :
    (front c B t).val = Queue.gone c t :=
  congrArg Fin.val (dif_pos (Nat.lt_of_le_of_lt (Nat.le_add_right _ (n t))
    (Settles.reach tally settles t)))

/-- Every member the queue holds has a place. -/
theorem placed (tally : Tally n c a) (settles : Settles 0 B n c a) {k t : Nat}
    (holds : Queue.holds n c k t) : k < size B :=
  Nat.lt_trans holds.2 (Settles.reach tally settles t)

end Closed

namespace World

/-- A queue closed from the first step, on the finitely many places its members ever
take. -/
def closedQueue (n c a : Nat → Nat) (B : Nat) : World :=
  ⟨Fin (Closed.size B), Closed.flow n c a B, Closed.web n c a B⟩

instance closedQueue_decided (n c a : Nat → Nat) (B : Nat) :
    ∀ t x, Decidable ((closedQueue n c a B).web.active t x) :=
  fun t i => inferInstanceAs (Decidable (Queue.holds n c i.val t))

theorem closedQueue_finite (n c a : Nat → Nat) (B : Nat) : (closedQueue n c a B).Finite :=
  ⟨below _ (steps 0 (Closed.size B)), distinct_below (steps_distinct _ _), fun i =>
    mem_below.mpr (steps_of_within (Nat.zero_le _)
      (Nat.lt_of_lt_of_le i.isLt (Nat.le_of_eq (Nat.zero_add _).symm)))⟩

variable {n c a : Nat → Nat} {B : Nat}

theorem closedQueue_census (n c a : Nat → Nat) (B : Nat) :
    (closedQueue n c a B).web.Census (Closed.alive n c B) :=
  fun _ => ⟨distinct_below (steps_distinct _ _), fun _ =>
    ⟨fun holds => mem_below.mpr (steps_of_within holds.1 holds.2),
     fun mem => ⟨steps_mem (mem_below.mp mem), steps_within (mem_below.mp mem)⟩⟩⟩

/-- Its census counts what the queue counts. -/
theorem closedQueue_counts (tally : Tally n c a) (settles : Settles 0 B n c a) (t : Nat) :
    (Closed.alive n c B t).length = n t ∧
      ceasings (Closed.alive n c B t) (fun x s => (closedQueue n c a B).web.active s x) t =
        c t ∧
      comings (Closed.alive n c B (t + 1)) (fun x s => (closedQueue n c a B).web.active s x)
        t = a t :=
  have within : ∀ s k, k ∈ Queue.line n c s → k < Closed.size B := fun _ _ mem =>
    Closed.placed tally settles ⟨steps_mem mem, steps_within mem⟩
  ⟨(total_ones _).symm.trans ((total_below (g := fun _ => 1) (fun _ => rfl) (within t)).trans
      ((total_ones _).trans (steps_length _ _))),
   (total_below (fun _ => rfl) (within t)).trans (Queue.ceasings_eq tally t),
   (total_below (fun _ => rfl) (within (t + 1))).trans (Queue.comings_eq tally t)⟩

theorem closedQueue_premised (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (settles : Settles 0 B n c a) : (closedQueue n c a B).Premised :=
  have active : ∀ {t : Nat}, 0 < n t → (closedQueue n c a B).web.active t (Closed.front c B t) :=
    fun occupied => Eq.subst (motive := fun v => Queue.holds n c v _)
      (Closed.front_val tally settles _).symm (Tended.front.mpr occupied)
  .of (fun _ _ _ _ no => (nomatch no))
    (fun t i => closingQueue_balanced n c a 0 B t (.member i.val))
    (fun _ f _ present gives => match f, present, gives with
      | _, .head _, gives => active (Closing.busy (f := .member 0) tally company (.inr gives))
      | _, .tail _ no, _ => (nomatch no))
    (fun _ f _ present takes => match f, present, takes with
      | _, .head _, takes =>
        ⟨active (Closing.busy (f := .member 0) tally company (.inl takes)), trivial⟩
      | _, .tail _ no, _ => (nomatch no))
    (fun cs t distinct closed f present =>
      have dissipates := closingQueue_dissipative (T := 0) tally company settles
        (cs.map fun i : Fin (Closed.size B) => .member i.val) t
        (distinct_map (g := fun i : Fin (Closed.size B) => Tended.Relatum.member i.val)
          (fun _ _ same => fin_eq (Tended.member_inj _ _ same)) distinct)
        (fun _ _ x out => match x with
          | .member k =>
            if h : k < Closed.size B then closed f present ⟨k, h⟩ fun mem => out (mem_map_of mem)
            else Closing.still_flows
              ((Closing.place_zero fun holds => h (Closed.placed tally settles holds)).trans
                (Closing.place_zero fun holds => h (Closed.placed tally settles holds)).symm) rfl
          | .ground _ => Closing.still_flows rfl
              (mark_zero (p := t < 0 ∧ 0 < n t) fun early => Nat.not_lt_zero _ early.1))
        (.member (Queue.gone c t)) (.head _)
      have gives : total (cs.map fun i => Tended.Relatum.member i.val)
          ((Closing.flow n c a 0 B).give t (.member (Queue.gone c t))) =
            total cs ((Closed.flow n c a B).give t f) := total_map _ _ cs
      have takes : total (cs.map fun i => Tended.Relatum.member i.val)
          ((Closing.flow n c a 0 B).take t (.member (Queue.gone c t))) =
            total cs ((Closed.flow n c a B).take t f) := total_map _ _ cs
      Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) gives.symm).trans
          (congrArg (fun k => _ + sign k) takes.symm)))
        (Nat.le_trans dissipates (Nat.le_of_eq takes)))
    (fun _ _ => Closing.place_pos)
    ⟨_, closedQueue_census _ _ _ _⟩
    ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩

/-- Under all eight premises, in a finite world, the laws of counting are the balance, that
nothing arises across a step at which nothing is active, and that the counts settle from
the first step: a finite world counts as a world enclosed from the first step does. -/
theorem finite_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, Settles 0 B n c a) →
      Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
        w.CountsObey Q :=
  ⟨fun law w _ premised finite alive census =>
    law _ _ _ census.tally
      (counting_binds_jointly.1 w (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.head _))))
        (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
          (.head _))))))))
        alive census)
      ⟨_, change_within census
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))))
        (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))))
        fun t _ => finite.enclosed t⟩,
   fun law _ _ _ tally company ⟨_, settles⟩ => pointwise (closedQueue_counts tally settles)
      (law (closedQueue _ _ _ _) (closedQueue_premised tally company settles)
        (closedQueue_finite _ _ _ _) _ (closedQueue_census _ _ _ _))⟩

end World

end Becoming
