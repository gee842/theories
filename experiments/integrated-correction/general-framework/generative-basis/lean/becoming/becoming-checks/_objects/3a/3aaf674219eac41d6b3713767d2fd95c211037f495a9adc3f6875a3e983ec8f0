import Becoming.Generation

/-!
# Flow: more generation needs more replenishment

`Becoming.Generation` reads whether generation ceases. Ren's words also say *more*: a
whole direction of unceasingly creating more 生. This module reads the conditions of an
unfolding as amounts that the formations taking part in each step take and give
(`Flow`), and states what unceasing and more generation need.

* A flow *balances* a web when every change of a condition's level is what the
  formations taking part take from it and give to it (`Balances`). Over a finite family
  of conditions, the family's total after a step, plus its uptake, equals its total
  before, plus its replenishment (`Balances.over`), and the same holds over any stretch
  of steps (`Balances.accumulates`). Adding amounts across conditions presupposes that
  their units are commensurable.
* Balance makes every rise the work of a formation: a balanced flow in which only active
  formations give makes the premise `RenewedBy` of `Becoming.Generation` a theorem
  (`Balances.renewedBy`).
* Unceasing generation of formations that take needs replenishment. When formations
  taking from the family at their first active step arise at arbitrarily late steps,
  the family is replenished at arbitrarily late steps (`replenishment_recurs`), by
  formations giving to it (`renewing_recurs`). Unlike the net rise of
  `Becoming.Generation`, this sees replenishment concurrent with drawing.
* Generation is *more without end* when, for every number, from some step on at least
  that many formations take from the family (`More`). Amounts are natural numbers, so
  a formation taking takes at least one unit: uptake has a positive minimum. Over any
  stretch of steps from which at least `K` formations take, the family is then
  replenished by at least `K` per step, less its stock at the start
  (`Balances.replenished_over`), and more without end needs replenishment without
  bound: no bound holding from some step on bounds it
  (`More.replenishment_unbounded`). When each formation gives at most a fixed amount
  (`Capacity`), the number of formations giving grows in the same averaged sense
  (`Balances.renewers_over`) and has no eventual bound (`More.renewers_unbounded`); it
  can still be zero at infinitely many steps (`Pulse`). If uptake could become
  arbitrarily small, more takers would not need more replenishment (argued, not
  formalized: the core has natural numbers only).
* The premises are consistent with more without end: renewers and growers arise
  together at every step (`Garden.more`). There the level never rises, so the net-rise
  premise of `Becoming.Generation` fails (`Garden.undepleted`), while the flow form
  applies. Unceasing generation does not imply more without end: the bloom arises again
  and again while at most one formation ever takes (`Bloom.not_more`).
* The renewers can be the takers themselves: in a closed cycle each formation gives
  back what it takes, the family's total never changes, and generation is more without
  end with as many renewers as takers (`Cycle`). That more must be carried beyond every
  finite part of the unfolding needs dissipation: every giving costing the giver's
  conditions more than it gives. `Becoming.Dissipation` states that premise and proves
  it.

So, read through balanced flows: renewal can recur with nothing arising
(`Tide.renewal_without_arising`), unceasing generation does not imply more without end,
and the replenishment each needs grows from recurring to unbounded. `More` counts the
formations taking part in the flow that take; `Becoming.Population` ties them to the
active formations of the web and states when more implies unceasing generation. A
flow's `present` lists each formation taking part at a step once; that it records what
is actually taken and given is an application duty. The family of conditions and the
formations taking part at each step are finite. No ethical predicate, ranking or axiom
occurs. Diversity and complexity are not stated here.
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

theorem total_append (q : α → Nat) (bs : List α) :
    ∀ as : List α, total (as ++ bs) q = total as q + total bs q
  | [] => (Nat.zero_add _).symm
  | a :: as => (congrArg (q a + ·) (total_append q bs as)).trans (Nat.add_assoc _ _ _).symm

/-- A member at which a quantity is positive makes the total positive. -/
theorem total_pos_of_mem {q : α → Nat} {a : α} :
    ∀ {as : List α}, a ∈ as → 0 < q a → 0 < total as q
  | _ :: _, .head _, positive => Nat.lt_of_lt_of_le positive (Nat.le_add_right _ _)
  | b :: _, .tail _ mem, positive =>
    Nat.lt_of_lt_of_le (total_pos_of_mem mem positive) (Nat.le_add_left _ (q b))

/-- A positive total has a positive member. -/
theorem total_pos {q : α → Nat} : ∀ as : List α, 0 < total as q → ∃ a, a ∈ as ∧ 0 < q a
  | a :: as, pos => match h : q a with
    | 0 => match total_pos as (Nat.lt_of_lt_of_le pos (Nat.le_of_eq
        ((congrArg (· + total as q) h).trans (Nat.zero_add (total as q))))) with
      | ⟨b, mem, positive⟩ => ⟨b, .tail a mem, positive⟩
    | n + 1 => ⟨a, .head as, h ▸ Nat.succ_pos n⟩

theorem count_le (q : α → Nat) (as : List α) : count as q ≤ total as q :=
  total_le as fun a _ => sign_le (q a)

/-- A quantity positive at no member totals zero. -/
theorem total_zero_of_count {q : α → Nat} : ∀ as : List α, count as q = 0 → total as q = 0
  | [], _ => rfl
  | a :: as, zero => match h : q a with
    | 0 =>
      have rest : count as q = 0 :=
        (Nat.zero_add _).symm.trans ((congrArg (fun n => sign n + count as q) h).symm.trans zero)
      (congrArg (· + total as q) h).trans ((Nat.zero_add _).trans (total_zero_of_count as rest))
    | _ + 1 => Nat.noConfusion ((Nat.add_comm (count as q) 1).trans
        ((congrArg (fun n => sign n + count as q) h).symm.trans zero))

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

/-- Only active formations take, and only from conditions they draw on. -/
def Taking (W : Web F C) : Prop :=
  ∀ t f c, f ∈ L.present t → 0 < L.take t f c → W.active t f ∧ W.draws t f c

/-- The family's uptake: everything taken from a finite family of conditions across the
step from `t`. -/
def uptake (cs : List C) (t : Nat) : Nat :=
  total cs (L.taken t)

/-- The family's replenishment: everything given to a finite family of conditions across
the step from `t`. -/
def replenishment (cs : List C) (t : Nat) : Nat :=
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

/-- The formation arises across the step from `t` and takes from the family at its first
active step. -/
def ArisesTaking (W : Web F C) (cs : List C) (t : Nat) (f : F) : Prop :=
  W.Arises t f ∧ f ∈ L.present (t + 1) ∧ 0 < total cs (L.take (t + 1) f)

variable {L} {W : Web F C}

/-- The family's total after a step, plus its uptake, is its total before, plus its
replenishment. -/
theorem Balances.over (balances : L.Balances W) : ∀ (cs : List C) (t : Nat),
    W.stock cs (t + 1) + L.uptake cs t = W.stock cs t + L.replenishment cs t
  | [], _ => rfl
  | c :: cs, t =>
    (Nat.add_add_add_comm (W.level (t + 1) c) (W.stock cs (t + 1))
      (L.taken t c) (L.uptake cs t)).trans
    ((congrArg (· + (W.stock cs (t + 1) + L.uptake cs t)) (balances t c)).trans
    ((congrArg (W.level t c + L.given t c + ·) (balances.over cs t)).trans
      (Nat.add_add_add_comm (W.level t c) (L.given t c) (W.stock cs t) (L.replenishment cs t))))

/-- The balance over a stretch of steps. -/
theorem Balances.accumulates (balances : L.Balances W) (cs : List C) :
    ∀ T N, W.stock cs (T + N) + total (steps T N) (L.uptake cs) =
      W.stock cs T + total (steps T N) (L.replenishment cs)
  | _, 0 => rfl
  | T, N + 1 =>
    have later := balances.accumulates cs (T + 1) N
    have step := balances.over cs T
    calc W.stock cs (T + (N + 1)) + (L.uptake cs T + total (steps (T + 1) N) (L.uptake cs))
        = L.uptake cs T + (W.stock cs (T + 1 + N) + total (steps (T + 1) N) (L.uptake cs)) :=
          (congrArg (· + _) (congrArg (W.stock cs) (Nat.add_right_comm T 1 N).symm)).trans
            (Nat.add_left_comm _ _ _)
      _ = L.uptake cs T + (W.stock cs (T + 1) + total (steps (T + 1) N) (L.replenishment cs)) :=
          congrArg (L.uptake cs T + ·) later
      _ = W.stock cs (T + 1) + L.uptake cs T + total (steps (T + 1) N) (L.replenishment cs) :=
          (Nat.add_assoc _ _ _).symm.trans (congrArg (· + _) (Nat.add_comm _ _))
      _ = W.stock cs T + (L.replenishment cs T + total (steps (T + 1) N) (L.replenishment cs)) :=
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
theorem takers_le_uptake (cs : List C) (t : Nat) : L.takers cs t ≤ L.uptake cs t :=
  Nat.le_trans (count_le _ (L.present t))
    (Nat.le_of_eq (total_swap (fun f c => L.take t f c) cs (L.present t)))

/-- A formation taking part that takes from the family makes its uptake positive. -/
theorem uptake_pos {cs : List C} {t : Nat} {f : F} (present : f ∈ L.present t)
    (takes : 0 < total cs (L.take t f)) : 0 < L.uptake cs t :=
  Nat.lt_of_lt_of_le (total_pos_of_mem present takes)
    (Nat.le_of_eq (total_swap (fun f c => L.take t f c) cs (L.present t)))

/-- With no formation giving to the family, nothing replenishes it. -/
theorem replenishment_zero {cs : List C} {t : Nat} (nobody : L.renewers cs t = 0) :
    L.replenishment cs t = 0 :=
  (total_swap (fun c f => L.give t f c) (L.present t) cs).trans
    (total_zero_of_count (L.present t) nobody)

/-- With bounded capacity, the family's replenishment is bounded by the number of
renewers. -/
theorem replenishment_le {cs : List C} {g : Nat} (capacity : L.Capacity cs g) (t : Nat) :
    L.replenishment cs t ≤ g * L.renewers cs t :=
  Nat.le_trans (Nat.le_of_eq (total_swap (fun c f => L.give t f c) (L.present t) cs))
    (total_le_count (L.present t) (capacity t))

/-- Unceasing generation of formations that take needs replenishment: when formations
taking from the family at their first active step arise at arbitrarily late steps, the
family is replenished at arbitrarily late steps. -/
theorem replenishment_recurs {cs : List C} (balances : L.Balances W)
    (arising : ∀ N, ∃ t f, N ≤ t ∧ L.ArisesTaking W cs t f) (T : Nat) :
    ¬ ∀ t, T ≤ t → L.replenishment cs t = 0 :=
  fun none =>
    have step : ∀ t, T ≤ t → W.stock cs (t + 1) + L.uptake cs t = W.stock cs t :=
      fun t later => (balances.over cs t).trans
        ((congrArg (W.stock cs t + ·) (none t later)).trans (Nat.add_zero _))
    falls_finitely (W.stock cs) T
      (fun t later => Nat.le_trans (Nat.le_add_right _ _) (Nat.le_of_eq (step t later)))
      fun N => match arising (N + T) with
      | ⟨t, _, later, _, present, takes⟩ =>
        have after : T ≤ t + 1 := Nat.le_succ_of_le (Nat.le_trans (Nat.le_add_left T N) later)
        ⟨t + 1, Nat.le_succ_of_le (Nat.le_trans (Nat.le_add_right N T) later),
          Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right (uptake_pos present takes))
            (Nat.le_of_eq (step (t + 1) after))⟩

/-- Renewing activity recurs: under the same premises, formations give to the family at
arbitrarily late steps. When only active formations give, they are active. -/
theorem renewing_recurs {cs : List C} (balances : L.Balances W)
    (arising : ∀ N, ∃ t f, N ≤ t ∧ L.ArisesTaking W cs t f) (T : Nat) :
    ¬ ∀ t, T ≤ t → L.renewers cs t = 0 :=
  fun none => replenishment_recurs balances arising T fun t later =>
    replenishment_zero (none t later)

/-- Over any stretch of steps from which at least `K` formations take, the family is
replenished by at least `K` per step, less its stock at the start. -/
theorem Balances.replenished_over {cs : List C} {K S : Nat} (balances : L.Balances W)
    (many : ∀ t, S ≤ t → K ≤ L.takers cs t) (N : Nat) :
    K * N ≤ W.stock cs S + total (steps S N) (L.replenishment cs) :=
  Nat.le_trans (steps_ge S N fun t later => Nat.le_trans (many t later) (takers_le_uptake cs t))
    (Nat.le_trans (Nat.le_add_left _ (W.stock cs (S + N)))
      (Nat.le_of_eq (balances.accumulates cs S N)))

/-- With bounded capacity, over any stretch of steps from which at least `K` formations
take, the formations giving to the family number at least `K` per step, less its stock
at the start, up to the capacity. -/
theorem Balances.renewers_over {cs : List C} {g K S : Nat} (balances : L.Balances W)
    (capacity : L.Capacity cs g) (many : ∀ t, S ≤ t → K ≤ L.takers cs t) (N : Nat) :
    K * N ≤ W.stock cs S + g * total (steps S N) (L.renewers cs) :=
  Nat.le_trans (balances.replenished_over many N)
    (Nat.add_le_add_left (Nat.le_trans (total_le _ fun t _ => replenishment_le capacity t)
      (Nat.le_of_eq (total_mul g (L.renewers cs) _))) _)

/-- More without end needs replenishment without bound: no bound holding from some step
on bounds the family's replenishment. -/
theorem More.replenishment_unbounded {cs : List C} (balances : L.Balances W)
    (more : L.More cs) (R T₀ : Nat) : ¬ ∀ t, T₀ ≤ t → L.replenishment cs t ≤ R :=
  fun bounded => match more (R + 1) with
  | ⟨T₁, many⟩ =>
    let S := T₁ + T₀
    let N := W.stock cs S + 1
    have over := balances.replenished_over
      (fun t later => many t (Nat.le_trans (Nat.le_add_right T₁ T₀) later)) N
    have given : total (steps S N) (L.replenishment cs) ≤ R * N :=
      steps_le S N fun t later => bounded t (Nat.le_trans (Nat.le_add_left T₀ T₁) later)
    have le : R * N + N ≤ W.stock cs S + R * N :=
      Nat.le_trans (Nat.le_of_eq (Nat.succ_mul R N).symm)
        (Nat.le_trans over (Nat.add_le_add_left given _))
    Nat.not_succ_le_self (W.stock cs S + R * N)
      (Nat.le_trans (Nat.le_of_eq (congrArg Nat.succ (Nat.add_comm _ _))) le)

/-- More without end needs renewers without bound: when each formation gives at most a
fixed amount, no bound holding from some step on bounds how many formations give. -/
theorem More.renewers_unbounded {cs : List C} {g : Nat} (balances : L.Balances W)
    (capacity : L.Capacity cs g) (more : L.More cs) (M T₀ : Nat) :
    ¬ ∀ t, T₀ ≤ t → L.renewers cs t ≤ M :=
  fun bounded => more.replenishment_unbounded balances (g * M) T₀ fun t later =>
    Nat.le_trans (replenishment_le capacity t) (Nat.mul_le_mul_left g (bounded t later))

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

/-- Only active growers take, each from the condition it draws on, and every grower
takes at its first active step: the flow form `replenishment_recurs` applies. -/
theorem growers_take : flow.Taking web ∧ ∀ t, flow.ArisesTaking web [()] t (.grower, t) :=
  ⟨fun t f _ mem takes => match f, mem, takes with
    | (.renewer, _), _, takes => absurd takes (Nat.lt_irrefl 0)
    | (.grower, _), mem, _ => ⟨present_active t _ mem, rfl, present_active t _ mem⟩,
   fun t => ⟨⟨Nat.lt_irrefl t, Nat.lt_succ_self t⟩, .tail _ (.head _), Nat.zero_lt_one⟩⟩

/-- The level never rises: generation is unceasing, yet arising does not deplete the
family in the net sense of `Becoming.Generation`. Replenishment concurrent with drawing
is invisible to a net rise. -/
theorem undepleted :
    web.Unceasing ∧ (∀ t, ¬ web.Rises t ()) ∧
    ¬ web.Depletes [()] (fun t => ∃ f, web.Arises t f) :=
  ⟨more.2.2.2.2.2.1, fun _ rises => Nat.lt_irrefl 1 rises,
   fun depletes => match depletes 0 ⟨(.renewer, 0), Nat.lt_irrefl 0, Nat.zero_lt_one⟩
      (fun _ _ rises => Nat.lt_irrefl 1 rises) with
    | ⟨_, _, falls⟩ => Nat.lt_irrefl 1 falls⟩

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

theorem takes_when_active : ∀ t, 2 ≤ glow t → 0 < 2 * (glow t - 1)
  | 0, _ => Nat.zero_lt_succ 1
  | 1, two => absurd two (Nat.not_succ_le_self 1)
  | t + 2, two => takes_when_active t two

theorem active_when_taking : ∀ t, 0 < 2 * (glow t - 1) → 2 ≤ glow t
  | 0, _ => Nat.le_refl 2
  | 1, takes => absurd takes (Nat.lt_irrefl 0)
  | t + 2, takes => active_when_taking t takes

/-- Only the active bloom takes, from the condition it draws on, and it takes at its
first active step. -/
theorem takes : flow.Taking web ∧ ∀ t f, web.Arises t f → flow.ArisesTaking web [()] t f :=
  ⟨fun t f _ _ takes => match f, takes with
    | .sun, takes => absurd takes (Nat.lt_irrefl 0)
    | .bloom, takes => ⟨active_when_taking t takes, active_when_taking t takes⟩,
   fun t f arises => match f, arises with
    | .sun, ⟨inactive, _⟩ => absurd trivial inactive
    | .bloom, arises => ⟨arises, .tail _ (.head _), takes_when_active (t + 1) arises.2⟩⟩

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

/-! ## The renewers can be the takers -/

namespace Cycle

/-- Formations `0`, …, `t - 1` take part in the step from `t`. -/
def present : Nat → List Nat
  | 0 => []
  | n + 1 => n :: present n

/-- Each formation taking part takes one unit and gives one back. -/
def flow : Flow Nat Unit := ⟨present, fun _ _ _ => 1, fun _ _ _ => 1⟩

/-- Formation `n` arises across step `n`, depends on the condition at need one, and draws
on it while active. -/
def web : Web Nat Unit where
  level _ _ := 1
  active t n := n < t
  requires t n _ := n < t
  need _ _ _ := 1
  draws t n _ := n < t

/-- `t` formations take part in the step from `t`. -/
theorem ones : ∀ t, total (present t) (fun _ => 1) = t
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (ones n)).trans (Nat.add_comm 1 n)

theorem present_lt : ∀ t n, n ∈ present t → n < t
  | m + 1, _, .head _ => Nat.lt_succ_self m
  | m + 1, n, .tail _ mem => Nat.lt_succ_of_lt (present_lt m n mem)

/-- Each formation renews what it takes: the flow balances, only active formations take
and give, generation is unceasing and more without end, the family's total never
changes, and as many formations give as take. -/
theorem closed_more :
    flow.Balances web ∧ flow.Acting web ∧ flow.Taking web ∧ flow.Capacity [()] 1 ∧
    web.Dependent ∧ web.Unceasing ∧ flow.More [()] ∧
    (∀ t, web.stock [()] (t + 1) = web.stock [()] t) ∧
    ∀ t, flow.renewers [()] t = flow.takers [()] t :=
  ⟨fun t _ => congrArg (1 + ·) ((ones t).trans (ones t).symm),
   fun t n _ mem _ => present_lt t n mem,
   fun t n _ mem _ => ⟨present_lt t n mem, present_lt t n mem⟩,
   fun _ _ _ => Nat.le_refl 1,
   fun _ _ _ _ _ => Nat.le_refl 1,
   fun N => ⟨N, N, Nat.le_refl N, Nat.lt_irrefl N, Nat.lt_succ_self N⟩,
   fun K => ⟨K, fun t later => Nat.le_trans later (Nat.le_of_eq (ones t).symm)⟩,
   fun _ => rfl,
   fun _ => rfl⟩

end Cycle

/-! ## Renewers without eventual bound can be absent infinitely often -/

namespace Pulse

open Garden (Kind)

/-- `n` formations of one kind. -/
def kind (k : Kind) : Nat → List (Kind × Nat)
  | 0 => []
  | n + 1 => (k, n) :: kind k n

theorem total_kind {q : Kind × Nat → Nat} {k : Kind} {v : Nat} (same : ∀ i, q (k, i) = v) :
    ∀ n, total (kind k n) q = n * v
  | 0 => (Nat.zero_mul v).symm
  | n + 1 => (congrArg (· + total (kind k n) q) (same n)).trans
      ((congrArg (v + ·) (total_kind same n)).trans
        ((Nat.add_comm v (n * v)).trans (Nat.succ_mul n v).symm))

def half : Nat → Nat
  | 0 => 0
  | 1 => 0
  | n + 2 => half n + 1

def even : Nat → Bool
  | 0 => true
  | 1 => false
  | n + 2 => even n

/-- A number at even steps, zero at odd steps. -/
def onEven : Bool → Nat → Nat
  | true, n => n
  | false, _ => 0

/-- `t` renewers at an even step `t`, none at odd steps. -/
def pulse (t : Nat) : Nat := onEven (even t) t

/-- Nothing stored at even steps; half the step at odd steps. -/
def stored (t : Nat) : Nat := onEven (even (t + 1)) (half t)

/-- At step `t`, `half t` growers each take one unit and `pulse t` renewers each give
one. -/
def flow : Flow (Kind × Nat) Unit where
  present t := kind .renewer (pulse t) ++ kind .grower (half t)
  take _ f _ := match f.1 with
    | .renewer => 0
    | .grower => 1
  give _ f _ := match f.1 with
    | .renewer => 1
    | .grower => 0

/-- Every formation is active; growers draw on the condition. -/
def web : Web (Kind × Nat) Unit where
  level t _ := stored t
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ f _ := f.1 = .grower

theorem half_even : ∀ m, half (2 * m) = m
  | 0 => rfl
  | m + 1 => congrArg (· + 1) (half_even m)

theorem half_odd : ∀ m, half (2 * m + 1) = m
  | 0 => rfl
  | m + 1 => congrArg (· + 1) (half_odd m)

theorem even_even : ∀ m, even (2 * m) = true
  | 0 => rfl
  | m + 1 => even_even m

theorem even_odd : ∀ m, even (2 * m + 1) = false
  | 0 => rfl
  | m + 1 => even_odd m

theorem half_ge : ∀ K t, 2 * K ≤ t → K ≤ half t
  | 0, _, _ => Nat.zero_le _
  | _ + 1, 0, le => absurd le (Nat.not_succ_le_zero _)
  | _ + 1, 1, le => absurd (Nat.le_of_succ_le_succ le) (Nat.not_succ_le_zero _)
  | K + 1, t + 2, le =>
    Nat.succ_le_succ (half_ge K t (Nat.le_of_succ_le_succ (Nat.le_of_succ_le_succ le)))

theorem parity : ∀ t, (∃ m, t = 2 * m) ∨ ∃ m, t = 2 * m + 1
  | 0 => .inl ⟨0, rfl⟩
  | t + 1 => match parity t with
    | .inl ⟨m, h⟩ => .inr ⟨m, congrArg (· + 1) h⟩
    | .inr ⟨m, h⟩ => .inl ⟨m + 1, congrArg (· + 1) h⟩

theorem taken_eq (t : Nat) : flow.taken t () = half t :=
  (total_append _ _ _).trans
    ((congr (congrArg (· + ·) (total_kind (v := 0) (fun _ => rfl) (pulse t)))
      (total_kind (v := 1) (fun _ => rfl) (half t))).trans
      ((Nat.zero_add _).trans (Nat.mul_one (half t))))

theorem given_eq (t : Nat) : flow.given t () = pulse t :=
  (total_append _ _ _).trans
    ((congr (congrArg (· + ·) (total_kind (v := 1) (fun _ => rfl) (pulse t)))
      (total_kind (v := 0) (fun _ => rfl) (half t))).trans (Nat.mul_one (pulse t)))

theorem takers_eq (t : Nat) : flow.takers [()] t = half t :=
  (total_append _ _ _).trans
    ((congr (congrArg (· + ·) (total_kind (v := 0) (fun _ => rfl) (pulse t)))
      (total_kind (v := 1) (fun _ => rfl) (half t))).trans
      ((Nat.zero_add _).trans (Nat.mul_one (half t))))

theorem renewers_eq (t : Nat) : flow.renewers [()] t = pulse t :=
  (total_append _ _ _).trans
    ((congr (congrArg (· + ·) (total_kind (v := 1) (fun _ => rfl) (pulse t)))
      (total_kind (v := 0) (fun _ => rfl) (half t))).trans (Nat.mul_one (pulse t)))

theorem balances (t : Nat) :
    web.level (t + 1) () + flow.taken t () = web.level t () + flow.given t () :=
  (congrArg (stored (t + 1) + ·) (taken_eq t)).trans
    (Eq.trans (match parity t with
      | .inl ⟨m, h⟩ => h ▸
        (show stored (2 * m + 1) + half (2 * m) = stored (2 * m) + pulse (2 * m) from
          (congr (congrArg (· + ·) ((congrArg (onEven · _) (even_even m)).trans (half_odd m)))
            (half_even m)).trans ((Nat.two_mul m).symm.trans ((Nat.zero_add _).symm.trans
              (congr (congrArg (· + ·) (congrArg (onEven · _) (even_odd m)))
                (congrArg (onEven · _) (even_even m))).symm)))
      | .inr ⟨m, h⟩ => h ▸
        (show stored (2 * m + 1 + 1) + half (2 * m + 1) =
            stored (2 * m + 1) + pulse (2 * m + 1) from
          (congr (congrArg (· + ·) (congrArg (onEven · _) (even_odd (m + 1))))
            (half_odd m)).trans ((Nat.zero_add m).trans ((Nat.add_zero m).symm.trans
              (congr (congrArg (· + ·) ((congrArg (onEven · _) (even_even (m + 1))).trans
                (half_odd m))) (congrArg (onEven · _) (even_odd m))).symm))))
      (congrArg (stored t + ·) (given_eq t).symm))

/-- The flow balances, every formation is active, each gives at most one unit, and
generation is more without end; yet at every odd step no formation gives and nothing
replenishes the family. Renewers without eventual bound are not ever more renewers at
every step. -/
theorem pulsed :
    flow.Balances web ∧ flow.Acting web ∧ flow.Capacity [()] 1 ∧ flow.More [()] ∧
    ∀ T, ∃ t, T ≤ t ∧ flow.renewers [()] t = 0 ∧ flow.replenishment [()] t = 0 :=
  ⟨fun t _ => balances t,
   fun _ _ _ _ _ => trivial,
   fun _ f _ => match f with
    | (.renewer, _) => Nat.le_refl 1
    | (.grower, _) => Nat.zero_le 1,
   fun K => ⟨2 * K, fun t later => Nat.le_trans (half_ge K t later)
     (Nat.le_of_eq (takers_eq t).symm)⟩,
   fun T =>
    have none : flow.renewers [()] (2 * T + 1) = 0 :=
      (renewers_eq _).trans (congrArg (onEven · _) (even_odd T))
    ⟨2 * T + 1, Nat.le_succ_of_le (Nat.le_mul_of_pos_left T Nat.zero_lt_two), none,
      Flow.replenishment_zero none⟩⟩

end Pulse

end Becoming
