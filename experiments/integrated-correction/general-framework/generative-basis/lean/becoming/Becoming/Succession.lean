import Becoming.Continuation

/-!
# Succession: fed at every step, by no particular source

The record `continuing-self-fed-from-beyond` proved that a continuing family is fed from beyond
and that no source condition need recur (`Lone.fed_not_recurring`); in `Lone` one source
formation does all the conveying, so it left open, in the chapter's section 8, a witness in
which no particular source formation recurs. This module gives it, under Ren's "move towards
100%" (12 October 2026).

* **Sources in succession.** One source for each step, active at its own step only, burns that
  step's fuel and gives the pool one unit; one eater takes one unit from the pool at every
  step (`Successive.flow`, `Successive.web`).
* **Fed at every step, by no particular source.** The flow balances, is dissipative and gives
  only from active formations; the eater takes from the pool at every step and the pool is fed
  from beyond at every step; yet no source formation takes part at two steps, and none is
  active at two (`Successive.relay`, from `Successive.takes_part_once`). With `Lone`, neither a
  particular source condition nor a particular source formation need recur: what continuing
  needs is being fed, not any one feeder.

Read (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D12): the
dependence of a continuing family on what lies beyond is on
the conveying, which can pass from formation to formation. Not shown: that the sources
themselves arise from the flow (here each is given at its step); a world-level form. No ethical
predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace Successive

open Frontier (Condition unburnt burning)

/-- Sources, one for each step, and one eater. -/
inductive Formation where
  | source (n : Nat)
  | eater

/-- At each step its own source burns the step's fuel, two units, and gives the pool one; the
eater takes one unit from the pool. -/
def flow : Flow Formation Condition where
  present t := [.source t, .eater]
  take t f c := match f, c with
    | .source _, .pool => 0
    | .source _, .fuel n => 2 * burning n t
    | .eater, .pool => 1
    | .eater, .fuel _ => 0
  give _ f c := match f, c with
    | .source _, .pool => 1
    | .source _, .fuel _ => 0
    | .eater, _ => 0

/-- The pool holds nothing between steps; the `n`th fuel holds two units until it burns. A
source is active at its own step only; the eater always. -/
def web : Web Formation Condition where
  level t c := match c with
    | .pool => 0
    | .fuel n => 2 * unburnt n t
  active t f := match f with
    | .source n => n = t
    | .eater => True
  requires _ _ _ := False
  need _ _ _ := 0
  draws t f c := match f, c with
    | .source _, .pool => False
    | .source _, .fuel n => n = t
    | .eater, .pool => True
    | .eater, .fuel _ => False

theorem balances : flow.Balances web
  | _, .pool => rfl
  | t, .fuel n => show 2 * unburnt n (t + 1) + (2 * burning n t + 0) = 2 * unburnt n t + 0 from
      (Nat.left_distrib 2 _ _).symm.trans (congrArg (2 * ·) (Frontier.burns n t))

/-- Every family without repetition closed across a step is dissipated on: the step's source
gives the pool one unit and burns two. -/
theorem dissipative : flow.Dissipative
  | ds, t, distinct, closed, f, mem => match f, mem with
    | .eater, _ => Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (total_zero ds)).trans
        (Nat.zero_add _))) (sign_le _)
    | .source m, mem =>
      have gives : total ds (flow.give t (.source m)) ≤ 1 :=
        total_le_at (q := flow.give t (.source m)) (a := .pool) (fun c given => match c, given with
          | .pool, _ => rfl
          | .fuel _, given => absurd given (Nat.lt_irrefl 0)) distinct
      have burnt : flow.take t (.source m) (.fuel t) = 2 :=
        (congrArg (2 * ·) (Frontier.burning_self t)).trans (Nat.mul_one _)
      match Nat.decLe (total ds (flow.give t (.source m)) + sign (total ds (flow.take t (.source m))))
          (total ds (flow.take t (.source m))) with
      | isTrue le => le
      | isFalse not => absurd (fun inside : Condition.fuel t ∈ ds => not
          (Nat.le_trans (Nat.add_le_add gives (sign_le_one _))
            (Nat.le_trans (Nat.le_of_eq burnt.symm) (le_total_of_mem inside))))
          fun outside => Nat.noConfusion (burnt.symm.trans (closed (.source m) mem (.fuel t) outside).1)

/-- Only active formations give: a source gives at its own step only, where it is active. -/
theorem acting : flow.Acting web
  | _, f, _, mem, _ => match f, mem with
    | .eater, _ => trivial
    | .source _, .head _ => rfl
    | .source _, .tail _ (.tail _ no) => nomatch no

/-- The pool is fed from beyond at every step: the step's source conveys from the step's
fuel. -/
theorem fed (t : Nat) : flow.FedFromBeyond [.pool] t :=
  ⟨.fuel t, .pool, (fun mem => match mem with | .tail _ no => nomatch no),
   .head _, .source t, .head _,
   show 0 < 2 * burning t t from
     Eq.subst (motive := fun b => 0 < 2 * b) (Frontier.burning_self t).symm (Nat.succ_pos 1),
   Nat.zero_lt_one⟩

/-- A source takes part at its own step only. -/
theorem takes_part_once {m t : Nat} (mem : Formation.source m ∈ flow.present t) : m = t :=
  match mem with
  | .head _ => rfl
  | .tail _ (.tail _ no) => nomatch no

/-- **Fed at every step, by no particular source.** The flow balances, is dissipative and
gives only from active formations; the eater takes from the pool at every step and the pool
is fed from beyond at every step; yet no source formation takes part at two steps, and none is
active at two. -/
theorem relay :
    flow.Balances web ∧ flow.Dissipative ∧ flow.Acting web ∧ (∀ t, flow.takers [.pool] t = 1) ∧
      (∀ t, flow.FedFromBeyond [.pool] t) ∧
      (∀ m t t', Formation.source m ∈ flow.present t → Formation.source m ∈ flow.present t' →
        t = t') ∧
      ∀ m t t', web.active t (.source m) → web.active t' (.source m) → t = t' :=
  ⟨balances, dissipative, acting, fun _ => rfl, fed,
   fun _ _ _ here there => (takes_part_once here).symm.trans (takes_part_once there),
   fun _ _ _ here there => (here : _ = _).symm.trans there⟩

end Successive

end Becoming
