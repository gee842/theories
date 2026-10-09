import Becoming.Generation

/-!
# Flow: more generation needs more renewers

`Becoming.Generation` states that generation does not cease. Ren's words also say *more*:
a whole direction of unceasingly creating more 生. This module reads the conditions of
an unfolding as amounts that the formations taking part in each step take and give
(`Flow`), and states what "more" needs.

* A flow *balances* a web when every change of a condition's level is what the
  formations taking part take from it and give to it (`Balances`). Over a finite family
  of conditions, the family's total after a step, plus everything taken, equals its
  total before, plus everything given (`ledger`), and the same holds over any stretch
  of steps (`accumulates`).
* Balance makes every rise the work of a formation: a balanced flow in which only active
  formations give makes the premise `RenewedBy` of `Becoming.Generation` a theorem
  (`Balances.renewedBy`).
* Generation is *more without end* when, for every number, from some step on at least
  that many formations take from the family (`More`). It needs supply without bound:
  no bound holding from some step on bounds what the family is given
  (`More.supply_unbounded`). When each formation gives at most a fixed amount
  (`Capacity`), it needs renewers without bound: no bound holding from some step on
  bounds how many formations give (`More.renewers_unbounded`). More 生 needs ever more
  formations renewing its conditions; whether they arise is not stated here.
* The premises are consistent with more without end: renewers and growers arise
  together at every step (`Garden.more`). Unceasing generation does not imply it: the
  bloom of `Becoming.Generation` arises again and again while at most one formation ever
  takes (`Bloom.not_more`).

So, read through balanced flows: recurring renewal does not imply unceasing generation
(`Commons.renewal_without_generation`), unceasing generation does not imply more without
end, and each needs more renewal than the one before it. A flow's `present` lists each
formation taking part at a step once; that it records what is actually taken and given
is an application duty. The family of conditions and the formations taking part at
each step are finite. No ethical predicate, ranking or axiom occurs. Diversity and
complexity are not stated here.
-/

namespace Becoming

/-- One for a positive number, zero for zero. -/
def sign : Nat → Nat
  | 0 => 0
  | _ + 1 => 1

/-- How many members of a finite list a quantity is positive at. -/
def count {α : Type} (as : List α) (q : α → Nat) : Nat :=
  total as fun a => sign (q a)

/-- The steps `T`, `T + 1`, …, `T + N - 1`. -/
def steps : Nat → Nat → List Nat
  | _, 0 => []
  | T, N + 1 => T :: steps (T + 1) N

section Totals

variable {α β : Type}

theorem sign_le : ∀ n, sign n ≤ n
  | 0 => Nat.le_refl 0
  | n + 1 => Nat.succ_le_succ (Nat.zero_le n)

theorem sign_le_one : ∀ n, sign n ≤ 1
  | 0 => Nat.zero_le 1
  | _ + 1 => Nat.le_refl 1

theorem le_mul_sign {g : Nat} : ∀ n, n ≤ g → n ≤ g * sign n
  | 0, _ => Nat.zero_le 0
  | _ + 1, le => Nat.le_trans le (Nat.le_of_eq (Nat.mul_one g).symm)

theorem total_le {p q : α → Nat} :
    ∀ as : List α, (∀ a, a ∈ as → p a ≤ q a) → total as p ≤ total as q
  | [], _ => Nat.le_refl 0
  | a :: as, le => Nat.add_le_add (le a (.head as)) (total_le as fun b mem => le b (.tail a mem))

theorem total_add (p q : α → Nat) :
    ∀ as : List α, total as (fun a => p a + q a) = total as p + total as q
  | [] => rfl
  | a :: as => (congrArg (p a + q a + ·) (total_add p q as)).trans
      (Nat.add_add_add_comm (p a) (q a) (total as p) (total as q))

theorem total_zero : ∀ as : List α, total as (fun _ => 0) = 0
  | [] => rfl
  | _ :: as => (Nat.zero_add _).trans (total_zero as)

theorem total_mul (g : Nat) (q : α → Nat) :
    ∀ as : List α, total as (fun a => g * q a) = g * total as q
  | [] => rfl
  | a :: as => (congrArg (g * q a + ·) (total_mul g q as)).trans
      (Nat.left_distrib g (q a) (total as q)).symm

/-- Totals over two finite lists may be taken in either order. -/
theorem total_swap (q : α → β → Nat) (bs : List β) :
    ∀ as : List α, total as (fun a => total bs (q a)) = total bs (fun b => total as fun a => q a b)
  | [] => (total_zero bs).symm
  | a :: as => (congrArg (total bs (q a) + ·) (total_swap q bs as)).trans
      (total_add (q a) (fun b => total as fun a' => q a' b) bs).symm

/-- A positive total has a positive member. -/
theorem total_pos {q : α → Nat} : ∀ as : List α, 0 < total as q → ∃ a, a ∈ as ∧ 0 < q a
  | a :: as, pos => match h : q a with
    | 0 => match total_pos as (Nat.lt_of_lt_of_le pos (Nat.le_of_eq
        ((congrArg (· + total as q) h).trans (Nat.zero_add (total as q))))) with
      | ⟨b, mem, positive⟩ => ⟨b, .tail a mem, positive⟩
    | n + 1 => ⟨a, .head as, h ▸ Nat.succ_pos n⟩

theorem count_le (q : α → Nat) (as : List α) : count as q ≤ total as q :=
  total_le as fun a _ => sign_le (q a)

theorem total_le_count {q : α → Nat} {g : Nat} (as : List α) (le : ∀ a, a ∈ as → q a ≤ g) :
    total as q ≤ g * count as q :=
  Nat.le_trans (total_le as fun a mem => le_mul_sign (q a) (le a mem))
    (Nat.le_of_eq (total_mul g (fun a => sign (q a)) as))

theorem steps_ge {q : Nat → Nat} {K : Nat} :
    ∀ T N, (∀ t, T ≤ t → K ≤ q t) → K * N ≤ total (steps T N) q
  | _, 0, _ => Nat.zero_le _
  | T, N + 1, ge => Nat.le_trans (Nat.le_of_eq (Nat.add_comm (K * N) K))
      (Nat.add_le_add (ge T (Nat.le_refl T))
        (steps_ge (T + 1) N fun t later => ge t (Nat.le_of_succ_le later)))

theorem steps_le {q : Nat → Nat} {R : Nat} :
    ∀ T N, (∀ t, T ≤ t → q t ≤ R) → total (steps T N) q ≤ R * N
  | _, 0, _ => Nat.zero_le _
  | T, N + 1, le => Nat.le_trans
      (Nat.add_le_add (le T (Nat.le_refl T))
        (steps_le (T + 1) N fun t later => le t (Nat.le_of_succ_le later)))
      (Nat.le_of_eq (Nat.add_comm R (R * N)))

end Totals

variable {F C : Type}

/-- Amounts flowing between formations and conditions across each step: the formations
taking part in the step, and how much each takes from and gives to each condition. -/
structure Flow (F C : Type) where
  present : Nat → List F
  take : Nat → F → C → Nat
  give : Nat → F → C → Nat

namespace Flow

variable (L : Flow F C)

/-- What the formations taking part take from a condition across the step from `t`. -/
def taken (t : Nat) (c : C) : Nat :=
  total (L.present t) fun f => L.take t f c

/-- What the formations taking part give to a condition across the step from `t`. -/
def given (t : Nat) (c : C) : Nat :=
  total (L.present t) fun f => L.give t f c

/-- Every change of a condition's level is what the formations taking part take from it
and give to it. -/
def Balances (W : Web F C) : Prop :=
  ∀ t c, W.level (t + 1) c + L.taken t c = W.level t c + L.given t c

/-- Only active formations give. -/
def Acting (W : Web F C) : Prop :=
  ∀ t f c, f ∈ L.present t → 0 < L.give t f c → W.active t f

/-- Everything taken from a finite family of conditions across the step from `t`. -/
def load (cs : List C) (t : Nat) : Nat :=
  total cs (L.taken t)

/-- Everything given to a finite family of conditions across the step from `t`. -/
def supply (cs : List C) (t : Nat) : Nat :=
  total cs (L.given t)

/-- How many formations take from the family across the step from `t`. -/
def takers (cs : List C) (t : Nat) : Nat :=
  count (L.present t) fun f => total cs (L.take t f)

/-- How many formations give to the family across the step from `t`. -/
def renewers (cs : List C) (t : Nat) : Nat :=
  count (L.present t) fun f => total cs (L.give t f)

/-- Generation is more without end: for every number, from some step on at least that
many formations take from the family. -/
def More (cs : List C) : Prop :=
  ∀ K, ∃ T, ∀ t, T ≤ t → K ≤ L.takers cs t

/-- Each formation gives the family at most `g` across a step. -/
def Capacity (cs : List C) (g : Nat) : Prop :=
  ∀ t f, f ∈ L.present t → total cs (L.give t f) ≤ g

variable {L} {W : Web F C}

/-- The family's total after a step, plus everything taken, is its total before, plus
everything given. -/
theorem ledger (balances : L.Balances W) :
    ∀ (cs : List C) (t : Nat), W.stock cs (t + 1) + L.load cs t = W.stock cs t + L.supply cs t
  | [], _ => rfl
  | c :: cs, t =>
    (Nat.add_add_add_comm (W.level (t + 1) c) (W.stock cs (t + 1))
      (L.taken t c) (L.load cs t)).trans
    ((congrArg (· + (W.stock cs (t + 1) + L.load cs t)) (balances t c)).trans
    ((congrArg (W.level t c + L.given t c + ·) (ledger balances cs t)).trans
      (Nat.add_add_add_comm (W.level t c) (L.given t c) (W.stock cs t) (L.supply cs t))))

/-- The ledger over a stretch of steps. -/
theorem accumulates (balances : L.Balances W) (cs : List C) :
    ∀ T N, W.stock cs (T + N) + total (steps T N) (L.load cs) =
      W.stock cs T + total (steps T N) (L.supply cs)
  | _, 0 => rfl
  | T, N + 1 =>
    have later := accumulates balances cs (T + 1) N
    have step := ledger balances cs T
    calc W.stock cs (T + (N + 1)) + (L.load cs T + total (steps (T + 1) N) (L.load cs))
        = L.load cs T + (W.stock cs (T + 1 + N) + total (steps (T + 1) N) (L.load cs)) :=
          (congrArg (· + _) (congrArg (W.stock cs) (Nat.add_right_comm T 1 N).symm)).trans
            (Nat.add_left_comm _ _ _)
      _ = L.load cs T + (W.stock cs (T + 1) + total (steps (T + 1) N) (L.supply cs)) :=
          congrArg (L.load cs T + ·) later
      _ = W.stock cs (T + 1) + L.load cs T + total (steps (T + 1) N) (L.supply cs) :=
          (Nat.add_assoc _ _ _).symm.trans (congrArg (· + _) (Nat.add_comm _ _))
      _ = W.stock cs T + (L.supply cs T + total (steps (T + 1) N) (L.supply cs)) :=
          (congrArg (· + _) step).trans (Nat.add_assoc _ _ _)

/-- Every rise is the work of a formation: in a balanced flow where only active
formations give, some active formation taking part gives to every condition that rises. -/
theorem Balances.renewedBy (balances : L.Balances W) (acting : L.Acting W) :
    W.RenewedBy fun t f c => f ∈ L.present t ∧ 0 < L.give t f c :=
  fun t c rises =>
    have given : 0 < L.given t c := Nat.pos_of_ne_zero fun none =>
      Nat.not_le_of_gt rises (Nat.le_trans (Nat.le_add_right _ (L.taken t c))
        (Nat.le_of_eq ((balances t c).trans (congrArg (W.level t c + ·) none))))
    match total_pos (L.present t) given with
    | ⟨f, mem, gives⟩ => ⟨f, acting t f c mem gives, mem, gives⟩

/-- Formations taking from the family take at least one unit each. -/
theorem takers_le_load (cs : List C) (t : Nat) : L.takers cs t ≤ L.load cs t :=
  Nat.le_trans (count_le _ (L.present t))
    (Nat.le_of_eq (total_swap (fun f c => L.take t f c) cs (L.present t)))

/-- With bounded capacity, what the family is given is bounded by the number of renewers. -/
theorem supply_le {cs : List C} {g : Nat} (capacity : L.Capacity cs g) (t : Nat) :
    L.supply cs t ≤ g * L.renewers cs t :=
  Nat.le_trans (Nat.le_of_eq (total_swap (fun c f => L.give t f c) (L.present t) cs))
    (total_le_count (L.present t) (capacity t))

/-- More without end needs supply without bound: no bound holding from some step on
bounds what the family is given. -/
theorem More.supply_unbounded {cs : List C} (balances : L.Balances W) (more : L.More cs)
    (R T₀ : Nat) : ¬ ∀ t, T₀ ≤ t → L.supply cs t ≤ R :=
  fun bounded => match more (R + 1) with
  | ⟨T₁, many⟩ =>
    let S := T₁ + T₀
    let N := W.stock cs S + 1
    have taken : (R + 1) * N ≤ total (steps S N) (L.load cs) :=
      steps_ge S N fun t later => Nat.le_trans
        (many t (Nat.le_trans (Nat.le_add_right T₁ T₀) later)) (takers_le_load cs t)
    have given : total (steps S N) (L.supply cs) ≤ R * N :=
      steps_le S N fun t later => bounded t (Nat.le_trans (Nat.le_add_left T₀ T₁) later)
    have le : R * N + N ≤ W.stock cs S + R * N :=
      Nat.le_trans (Nat.le_of_eq (Nat.succ_mul R N).symm)
        (Nat.le_trans taken (Nat.le_trans (Nat.le_add_left _ (W.stock cs (S + N)))
          (Nat.le_trans (Nat.le_of_eq (accumulates balances cs S N))
            (Nat.add_le_add_left given _))))
    Nat.not_succ_le_self (W.stock cs S + R * N)
      (Nat.le_trans (Nat.le_of_eq (congrArg Nat.succ (Nat.add_comm _ _))) le)

/-- More without end needs renewers without bound: when each formation gives at most a
fixed amount, no bound holding from some step on bounds how many formations give. -/
theorem More.renewers_unbounded {cs : List C} {g : Nat} (balances : L.Balances W)
    (capacity : L.Capacity cs g) (more : L.More cs) (M T₀ : Nat) :
    ¬ ∀ t, T₀ ≤ t → L.renewers cs t ≤ M :=
  fun bounded => more.supply_unbounded balances (g * M) T₀ fun t later =>
    Nat.le_trans (supply_le capacity t) (Nat.mul_le_mul_left g (bounded t later))

end Flow

/-! ## More without end on renewers that arise -/

namespace Garden

inductive Kind where
  | renewer
  | grower

/-- The formations taking part in the step from `t`: the `i`th renewer and the `i`th
grower for each `i < t`. -/
def present : Nat → List (Kind × Nat)
  | 0 => []
  | n + 1 => (.renewer, n) :: (.grower, n) :: present n

/-- Each grower takes one unit and each renewer gives one. -/
def flow : Flow (Kind × Nat) Unit where
  present := present
  take _ f _ := match f.1 with
    | .renewer => 0
    | .grower => 1
  give _ f _ := match f.1 with
    | .renewer => 1
    | .grower => 0

/-- The `i`th renewer and grower arise across step `i`; growers depend on the condition
and draw on it. -/
def web : Web (Kind × Nat) Unit where
  level _ _ := 1
  active t f := f.2 < t
  requires t f _ := f.1 = .grower ∧ f.2 < t
  need _ _ _ := 1
  draws t f _ := f.1 = .grower ∧ f.2 < t

theorem taken_eq : ∀ t, flow.taken t () = t
  | 0 => rfl
  | n + 1 => (Nat.zero_add _).trans ((Nat.add_comm 1 _).trans (congrArg (· + 1) (taken_eq n)))

theorem given_eq : ∀ t, flow.given t () = t
  | 0 => rfl
  | n + 1 => (Nat.add_comm 1 _).trans (congrArg (· + 1)
      ((Nat.zero_add _).trans (given_eq n)))

theorem takers_eq : ∀ t, flow.takers [()] t = t
  | 0 => rfl
  | n + 1 => (Nat.zero_add _).trans ((Nat.add_comm 1 _).trans (congrArg (· + 1) (takers_eq n)))

theorem present_active : ∀ t f, f ∈ present t → f.2 < t
  | n + 1, _, .head _ => Nat.lt_succ_self n
  | n + 1, _, .tail _ (.head _) => Nat.lt_succ_self n
  | n + 1, f, .tail _ (.tail _ mem) => Nat.lt_succ_of_lt (present_active n f mem)

/-- Renewers and growers arise together at every step: the flow balances, only active
formations give, each gives at most one unit, generation is unceasing, and more without
end. -/
theorem more :
    flow.Balances web ∧ flow.Acting web ∧ flow.Capacity [()] 1 ∧ web.Dependent ∧
    (∀ t, web.Arises t (.renewer, t)) ∧ web.Unceasing ∧ flow.More [()] :=
  ⟨fun t _ => (congrArg (1 + ·) (taken_eq t)).trans (congrArg (1 + ·) (given_eq t).symm),
   fun t f _ mem _ => present_active t f mem,
   fun _ f _ => match f with
    | (.renewer, _) => Nat.le_refl 1
    | (.grower, _) => Nat.zero_le 1,
   fun _ _ _ _ _ => Nat.le_refl 1,
   fun t => ⟨Nat.lt_irrefl t, Nat.lt_succ_self t⟩,
   fun N => ⟨N, (.renewer, N), Nat.le_refl N, Nat.lt_irrefl N, Nat.lt_succ_self N⟩,
   fun K => ⟨K, fun t later => Nat.le_trans later (Nat.le_of_eq (takers_eq t).symm)⟩⟩

end Garden

/-! ## Unceasing generation is not yet more -/

namespace Bloom

/-- The bloom takes two when it is active, and the sun gives one at every step. -/
def flow : Flow Formation Unit where
  present _ := [.sun, .bloom]
  take t f _ := match f with
    | .sun => 0
    | .bloom => 2 * (glow t - 1)
  give _ f _ := match f with
    | .sun => 1
    | .bloom => 0

theorem balances : ∀ t, web.level (t + 1) () + flow.taken t () = web.level t () + flow.given t ()
  | 0 => rfl
  | 1 => rfl
  | t + 2 => balances t

theorem takers_le (t : Nat) : flow.takers [()] t ≤ 1 :=
  Nat.add_le_add (Nat.zero_le 0) (Nat.add_le_add (sign_le_one _) (Nat.zero_le 0))

/-- The bloom arises again and again (`Bloom.unceasing`), yet the flow balances, only
active formations give, and at most one formation ever takes: unceasing generation is
not more without end. -/
theorem not_more :
    flow.Balances web ∧ flow.Acting web ∧ flow.Capacity [()] 1 ∧ web.Unceasing ∧
    ¬ flow.More [()] :=
  ⟨fun t _ => balances t,
   fun _ f _ _ gives => match f, gives with
    | .sun, _ => trivial,
   fun _ f _ => match f with
    | .sun => Nat.le_refl 1
    | .bloom => Nat.zero_le 1,
   unceasing.2.2.2.1,
   fun more => match more 2 with
    | ⟨T, many⟩ => Nat.not_succ_le_self 1 (Nat.le_trans (many T (Nat.le_refl T)) (takers_le T))⟩

end Bloom

end Becoming
