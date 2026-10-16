import Becoming.Horizon
import Becoming.Population

/-!
# Dissipation: no finite part bears continued taking alone

`Becoming.Flow` shows that the renewers can be the takers themselves: in a closed cycle
each formation gives back what it takes, and generation is more without end (`Cycle`).
Whether continued taking must draw on more than any finite part of the unfolding turns
on dissipation. This module states that premise on flows and proves what it carries.

* A family of conditions is *closed* across a step when no formation taking part takes
  from or gives to a condition outside it (`ClosedAt`).
* A formation *dissipates* on a family across a step when it gives the family no more
  than it takes from it, and less when it takes (`DissipatesOn`). A flow is
  *dissipative* when, across every step, every family without repetition closed across
  it is dissipated on (`Dissipative`). Giving then always costs the conditions the
  renewer takes from more than it gives.
* In a balanced flow, a family dissipated on across a step falls across it by at least
  the number of formations taking from it (`Balances.runs_down`). Dissipated on from
  some step, the formations taking from it over all later steps number at most its stock
  there (`Balances.takers_within`), and taking from it does not recur
  (`Balances.taking_ceases`).
* Under dissipation, a finite family from which formations take at arbitrarily late
  steps is not closed from any step on, and neither is any finite family without
  repetition containing it: at arbitrarily late steps some formation taking part
  exchanges with a condition outside it (`Dissipative.opens`). More without end
  (`More.opens`) and the unceasing arising of formations that take
  (`opens_of_arising`) are such taking. If finitely many conditions are all there is,
  taking does not recur at all (`Dissipative.finite_ceases`).
* The premises are consistent with more without end: a sun burns a fresh fuel at every
  step and gives a pool less than it burns, while ever more growers take from the pool
  (`Frontier`). The conditions it draws on are not contained in any finite family.
* Without dissipation a finite family can stay closed: the cycle of `Becoming.Flow`
  gives back what it takes (`Cycle.closed_more`).

Dissipation is read on amounts with commensurable units, as of free energy; matter can
cycle within a finite family while what drives the cycling is dissipated. That a given
quantity dissipates is a physical premise, not a theorem. The unfolding that bears
unceasing taking under dissipation reaches beyond every finite family of conditions;
whether actual unfoldings meet these premises is an empirical question. No ethical
predicate, ranking or axiom occurs.
-/

namespace Becoming

/-! ## Totals over lists without repetition -/

section Totals

variable {α : Type}

theorem pos_of_sign : ∀ {n : Nat}, 0 < sign n → 0 < n
  | 0, positive => positive
  | n + 1, _ => Nat.succ_pos n

theorem sign_pos : ∀ {n : Nat}, 0 < n → 0 < sign n
  | 0, positive => positive
  | _ + 1, _ => Nat.succ_pos 0

theorem eq_zero_of_not_pos : ∀ {n : Nat}, ¬ 0 < n → n = 0
  | 0, _ => rfl
  | n + 1, not => absurd (Nat.succ_pos n) not

/-- A member's value is at most the total. -/
theorem le_total_of_mem {q : α → Nat} {a : α} : ∀ {as : List α}, a ∈ as → q a ≤ total as q
  | _ :: _, .head _ => Nat.le_add_right _ _
  | b :: _, .tail _ mem => Nat.le_trans (le_total_of_mem mem) (Nat.le_add_left _ (q b))

theorem total_eq_zero {q : α → Nat} : ∀ {as : List α}, (∀ a, a ∈ as → q a = 0) → total as q = 0
  | [], _ => rfl
  | a :: _, zero => (congrArg (· + _) (zero a (.head _))).trans
      ((Nat.zero_add _).trans (total_eq_zero fun b mem => zero b (.tail a mem)))

/-- A quantity positive only at `a` totals at most its value at `a` over a list without
repetition. -/
theorem total_le_at {q : α → Nat} {a : α} (only : ∀ b, 0 < q b → b = a) :
    ∀ {as : List α}, Distinct as → total as q ≤ q a
  | [], _ => Nat.zero_le _
  | b :: as, ⟨fresh, distinct⟩ => match h : q b with
    | 0 => Nat.le_trans (Nat.le_of_eq ((congrArg (· + total as q) h).trans (Nat.zero_add _)))
        (total_le_at only distinct)
    | n + 1 =>
      have same : b = a := only b (h ▸ Nat.succ_pos n)
      have rest : total as q = 0 := total_eq_zero fun e mem => eq_zero_of_not_pos fun pos =>
        fresh (Eq.subst (motive := fun x => x ∈ as) ((only e pos).trans same.symm) mem)
      Nat.le_of_eq ((congrArg (q b + ·) rest).trans ((Nat.add_zero _).trans (congrArg q same)))

end Totals

variable {F C : Type}

namespace Flow

variable (L : Flow F C)

/-- No formation taking part in the step from `t` takes from or gives to a condition
outside the family. -/
def ClosedAt (cs : List C) (t : Nat) : Prop :=
  ∀ f, f ∈ L.present t → ∀ c, ¬ c ∈ cs → L.take t f c = 0 ∧ L.give t f c = 0

/-- Across the step from `t`, every formation taking part gives the family no more than it
takes from it, and less when it takes. -/
def DissipatesOn (cs : List C) (t : Nat) : Prop :=
  ∀ f, f ∈ L.present t →
    total cs (L.give t f) + sign (total cs (L.take t f)) ≤ total cs (L.take t f)

/-- Dissipation: across every step, every family without repetition closed across it is
dissipated on. -/
def Dissipative : Prop :=
  ∀ cs t, Distinct cs → L.ClosedAt cs t → L.DissipatesOn cs t

variable {L} {W : Web F C}

/-- Dissipated on, the family's replenishment and its takers together are at most its
uptake. -/
theorem DissipatesOn.replenishment_takers {cs : List C} {t : Nat}
    (dissipates : L.DissipatesOn cs t) : L.replenishment cs t + L.takers cs t ≤ L.uptake cs t :=
  Nat.le_trans
    (Nat.le_of_eq ((congrArg (· + L.takers cs t)
      (total_swap (fun c f => L.give t f c) (L.present t) cs)).trans
      (total_add (fun f => total cs (L.give t f)) (fun f => sign (total cs (L.take t f)))
        (L.present t)).symm))
    (Nat.le_trans
      (total_le (p := fun f => total cs (L.give t f) + sign (total cs (L.take t f)))
        (q := fun f => total cs (L.take t f)) (L.present t) dissipates)
      (Nat.le_of_eq (total_swap (fun f c => L.take t f c) cs (L.present t))))

/-- Dissipated on, the family falls across a step by at least the number of formations
taking from it. -/
theorem Balances.runs_down (balances : L.Balances W) {cs : List C} {t : Nat}
    (dissipates : L.DissipatesOn cs t) : W.stock cs (t + 1) + L.takers cs t ≤ W.stock cs t :=
  le_of_add_le_add_right (L.replenishment cs t) (Nat.le_trans
    (Nat.le_of_eq ((Nat.add_assoc _ _ _).trans
      (congrArg (W.stock cs (t + 1) + ·) (Nat.add_comm _ (L.replenishment cs t)))))
    (Nat.le_trans (Nat.add_le_add_left dissipates.replenishment_takers _)
      (Nat.le_of_eq (balances.over cs t))))

/-- Dissipated on from step `S`, the formations taking from the family over any later
stretch of steps number at most its stock at `S`. -/
theorem Balances.takers_within (balances : L.Balances W) {cs : List C} :
    ∀ S N, (∀ t, S ≤ t → L.DissipatesOn cs t) →
      W.stock cs (S + N) + total (steps S N) (L.takers cs) ≤ W.stock cs S
  | _, 0, _ => Nat.le_refl _
  | S, N + 1, dissipates =>
    have later := balances.takers_within (S + 1) N fun t after =>
      dissipates t (Nat.le_of_succ_le after)
    have now := balances.runs_down (dissipates S (Nat.le_refl S))
    Nat.le_trans
      (Nat.le_of_eq
        ((congrArg (· + _) (congrArg (W.stock cs) (Nat.add_right_comm S 1 N).symm)).trans
          ((Nat.add_left_comm _ _ _).trans (Nat.add_comm _ _))))
      (Nat.le_trans (Nat.add_le_add_right later _) now)

/-- Dissipated on from some step, taking from the family does not recur. -/
theorem Balances.taking_ceases (balances : L.Balances W) {cs : List C} {T : Nat}
    (dissipates : ∀ t, T ≤ t → L.DissipatesOn cs t) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t :=
  fun recurs => falls_finitely (W.stock cs) T
    (fun t later => Nat.le_trans (Nat.le_add_right _ _) (balances.runs_down (dissipates t later)))
    fun N => match recurs (N + T) with
    | ⟨t, later, takes⟩ => ⟨t, Nat.le_trans (Nat.le_add_right N T) later,
        Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right takes)
          (balances.runs_down (dissipates t (Nat.le_trans (Nat.le_add_left T N) later)))⟩

/-- A formation taking from a family takes from every family containing it. -/
theorem takers_pos_of_sub {cs ds : List C} (within : ∀ c, c ∈ cs → c ∈ ds) {t : Nat}
    (takes : 0 < L.takers cs t) : 0 < L.takers ds t :=
  match total_pos (q := fun f => sign (total cs (L.take t f))) (L.present t) takes with
  | ⟨_, mem, positive⟩ => match total_pos cs (pos_of_sign positive) with
    | ⟨c, inside, taken⟩ =>
      total_pos_of_mem (q := fun f => sign (total ds (L.take t f))) mem
        (sign_pos (total_pos_of_mem (within c inside) taken))

/-- Under dissipation, a finite family from which formations take at arbitrarily late
steps is not closed from any step on, and neither is any finite family without
repetition containing it. -/
theorem Dissipative.opens (balances : L.Balances W) (dissipative : L.Dissipative)
    {cs ds : List C} (distinct : Distinct ds) (within : ∀ c, c ∈ cs → c ∈ ds)
    (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t) (T : Nat) :
    ¬ ∀ t, T ≤ t → L.ClosedAt ds t :=
  fun closed => balances.taking_ceases (fun t later => dissipative ds t distinct (closed t later))
    fun N => match recurs N with
    | ⟨t, later, takes⟩ => ⟨t, later, takers_pos_of_sub within takes⟩

/-- If finitely many conditions are all there is, taking from any family does not recur
under dissipation. -/
theorem Dissipative.finite_ceases (balances : L.Balances W) (dissipative : L.Dissipative)
    {all : List C} (distinct : Distinct all) (every : ∀ c, c ∈ all) (cs : List C) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t :=
  fun recurs => dissipative.opens balances distinct (fun c _ => every c) recurs 0
    fun _ _ _ _ c outside => absurd (every c) outside

/-- More without end is taking at arbitrarily late steps. -/
theorem More.takers_recur {cs : List C} (more : L.More cs) :
    ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t :=
  fun N => match more 1 with
  | ⟨T, many⟩ => ⟨N + T, Nat.le_add_right N T, many (N + T) (Nat.le_add_left T N)⟩

/-- So is the unceasing arising of formations that take from the family at their first
active step. -/
theorem takers_recur_of_arising {cs : List C}
    (arising : ∀ N, ∃ t f, N ≤ t ∧ L.ArisesTaking W cs t f) :
    ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t :=
  fun N => match arising N with
  | ⟨t, _, later, _, present, takes⟩ =>
    ⟨t + 1, Nat.le_succ_of_le later,
      total_pos_of_mem (q := fun f => sign (total cs (L.take (t + 1) f))) present (sign_pos takes)⟩

/-- Under dissipation, more without end on a finite family needs exchange beyond it, and
beyond every finite family containing it, at arbitrarily late steps. -/
theorem More.opens (balances : L.Balances W) (dissipative : L.Dissipative) {cs ds : List C}
    (distinct : Distinct ds) (within : ∀ c, c ∈ cs → c ∈ ds) (more : L.More cs) (T : Nat) :
    ¬ ∀ t, T ≤ t → L.ClosedAt ds t :=
  dissipative.opens balances distinct within more.takers_recur T

/-- So does the unceasing arising of formations that take from it. -/
theorem opens_of_arising (balances : L.Balances W) (dissipative : L.Dissipative)
    {cs ds : List C} (distinct : Distinct ds) (within : ∀ c, c ∈ cs → c ∈ ds)
    (arising : ∀ N, ∃ t f, N ≤ t ∧ L.ArisesTaking W cs t f) (T : Nat) :
    ¬ ∀ t, T ≤ t → L.ClosedAt ds t :=
  dissipative.opens balances distinct within (takers_recur_of_arising arising) T

end Flow

/-! ## A frontier of fuels -/

namespace Frontier

/-- A pool, and fuels, one for each step. -/
inductive Condition where
  | pool
  | fuel (n : Nat)

/-- A sun, and growers, one arising at each step. -/
inductive Formation where
  | sun
  | grower (i : Nat)

/-- One while the `n`th fuel is unburnt: up to step `n`. -/
def unburnt : Nat → Nat → Nat
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, t + 1 => unburnt n t
termination_by structural _ t => t

/-- One at the step at which the `n`th fuel burns. -/
def burning : Nat → Nat → Nat
  | 0, 0 => 1
  | 0, _ + 1 => 0
  | _ + 1, 0 => 0
  | n + 1, t + 1 => burning n t
termination_by structural _ t => t

theorem burns : ∀ n t, unburnt n (t + 1) + burning n t = unburnt n t
  | 0, 0 => rfl
  | 0, _ + 1 => rfl
  | _ + 1, 0 => rfl
  | n + 1, t + 1 => burns n t

theorem burning_self : ∀ n, burning n n = 1
  | 0 => rfl
  | n + 1 => burning_self n

theorem burning_at : ∀ n t, 0 < burning n t → n = t
  | 0, 0, _ => rfl
  | 0, _ + 1, burnt => absurd burnt (Nat.lt_irrefl 0)
  | _ + 1, 0, burnt => absurd burnt (Nat.lt_irrefl 0)
  | n + 1, t + 1, burnt => congrArg (· + 1) (burning_at n t burnt)

/-- The growers arisen before step `t`. -/
def growers : Nat → List Formation
  | 0 => []
  | n + 1 => .grower n :: growers n

/-- Across the step from `t`, the sun burns the `t`th fuel, `t + 1` units, and gives the
pool `t`; each of the `t` growers takes one unit from the pool. -/
def flow : Flow Formation Condition where
  present t := .sun :: growers t
  take t f c := match f, c with
    | .sun, .pool => 0
    | .sun, .fuel n => (n + 1) * burning n t
    | .grower _, .pool => 1
    | .grower _, .fuel _ => 0
  give t f c := match f, c with
    | .sun, .pool => t
    | .sun, .fuel _ => 0
    | .grower _, _ => 0

/-- The pool holds nothing between steps; the `n`th fuel holds `n + 1` units until it
burns. The sun is always active and draws on the fuel it burns; the `i`th grower is
active from step `i + 1` and draws on the pool. -/
def web : Web Formation Condition where
  level t c := match c with
    | .pool => 0
    | .fuel n => (n + 1) * unburnt n t
  active t f := match f with
    | .sun => True
    | .grower i => i < t
  requires _ _ _ := False
  need _ _ _ := 0
  draws t f c := match f, c with
    | .sun, .pool => False
    | .sun, .fuel n => n = t
    | .grower i, .pool => i < t
    | .grower _, .fuel _ => False

theorem growers_take (t : Nat) :
    ∀ n, total (growers n) (fun f => flow.take t f .pool) = n
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (growers_take t n)).trans (Nat.add_comm 1 n)

theorem growers_give (t : Nat) (c : Condition) :
    ∀ n, total (growers n) (fun f => flow.give t f c) = 0
  | 0 => rfl
  | n + 1 => (Nat.zero_add _).trans (growers_give t c n)

theorem growers_take_fuel (t m : Nat) :
    ∀ n, total (growers n) (fun f => flow.take t f (.fuel m)) = 0
  | 0 => rfl
  | n + 1 => (Nat.zero_add _).trans (growers_take_fuel t m n)

theorem balances : flow.Balances web
  | t, .pool => show 0 + (0 + total (growers t) _) = 0 + (t + total (growers t) _) from
      (congrArg (fun x => 0 + (0 + x)) (growers_take t t)).trans
        ((congrArg (0 + ·) ((Nat.zero_add t).trans (Nat.add_zero t).symm)).trans
          (congrArg (fun x => 0 + (t + x)) (growers_give t .pool t)).symm)
  | t, .fuel n => show (n + 1) * unburnt n (t + 1) + ((n + 1) * burning n t + total (growers t) _)
        = (n + 1) * unburnt n t + (0 + total (growers t) _) from
      (congrArg (fun x => (n + 1) * unburnt n (t + 1) + ((n + 1) * burning n t + x))
        (growers_take_fuel t n t)).trans
      ((Nat.left_distrib (n + 1) _ _).symm.trans
      ((congrArg ((n + 1) * ·) (burns n t)).trans
      ((Nat.add_zero _).symm.trans
        (congrArg ((n + 1) * unburnt n t + ·) ((growers_give t (.fuel n) t).symm.trans
          (Nat.zero_add _).symm)))))

/-- Every family without repetition closed across a step is dissipated on: the sun gives
the pool `t` and burns `t + 1`; the growers give nothing. -/
theorem dissipative : flow.Dissipative
  | ds, t, distinct, closed, f, mem => match f, mem with
    | .grower _, _ => Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (total_zero ds)).trans
        (Nat.zero_add _))) (sign_le _)
    | .sun, mem =>
      have gives : total ds (flow.give t .sun) ≤ t :=
        total_le_at (q := flow.give t .sun) (a := .pool) (fun c given => match c, given with
          | .pool, _ => rfl
          | .fuel _, given => absurd given (Nat.lt_irrefl 0)) distinct
      have burnt : flow.take t .sun (.fuel t) = t + 1 :=
        (congrArg ((t + 1) * ·) (burning_self t)).trans (Nat.mul_one _)
      match Nat.decLe (total ds (flow.give t .sun) + sign (total ds (flow.take t .sun)))
          (total ds (flow.take t .sun)) with
      | isTrue le => le
      | isFalse not => absurd (fun inside : Condition.fuel t ∈ ds => not
          (Nat.le_trans (Nat.add_le_add gives (sign_le_one _))
            (Nat.le_trans (Nat.le_of_eq burnt.symm) (le_total_of_mem inside))))
          fun outside => Nat.noConfusion (burnt.symm.trans (closed .sun mem (.fuel t) outside).1)

theorem takers_pool (t : Nat) : flow.takers [.pool] t = t :=
  (Nat.zero_add _).trans (go t)
where
  go : ∀ n, count (growers n) (fun f => total [.pool] (flow.take t f)) = n
    | 0 => rfl
    | n + 1 => (congrArg (1 + ·) (go n)).trans (Nat.add_comm 1 n)

/-- Ever more growers take from the pool. -/
theorem more : flow.More [.pool] :=
  fun K => ⟨K, fun t later => Nat.le_trans later (Nat.le_of_eq (takers_pool t).symm)⟩

/-- Balanced, dissipative and more without end: every finite family without repetition
containing the pool is open at arbitrarily late steps, so the fuels the sun burns are
not contained in any finite family. -/
theorem frontier {ds : List Condition} (distinct : Distinct ds) (pool : Condition.pool ∈ ds)
    (T : Nat) : ¬ ∀ t, T ≤ t → flow.ClosedAt ds t :=
  Flow.More.opens balances dissipative distinct
    (fun c inside => match c, inside with | .pool, _ => pool) more T

end Frontier

end Becoming
