import Becoming.ContinuingRevision
import Becoming.Support
import Becoming.Contacts

/-!
# The revision witnesses as instances of the general laws

SCRATCH DRAFT (planning, not landed). Each section reads one existing witness through the
general laws of `Becoming.Support` and `Becoming.Contacts`, so the witness becomes a corollary
or a control. On landing these would sit at the end of the witness modules themselves (or the
witnesses would import the general modules).
-/

namespace Becoming

open Generative

/-! ## P93: Revising is a registration process run jointly with its stock -/

namespace Revising

/-- The registration side: the link (first) and the response (second). -/
def R : Process (Bool × Bool) Act := ⟨fun s a t => match a with
  | .replenish => t = s
  | .rebuild b => t = (b, s.2)
  | .correct => s.1 = true ∧ t = (true, true)⟩

def draw : Act → Nat
  | .replenish => 0
  | .rebuild _ => 1
  | .correct => 1

def restore : Act → Nat
  | .replenish => 1
  | .rebuild _ => 0
  | .correct => 0

theorem step_iff {s t : State} {a : Act} :
    P.step s a t ↔ (productProcess (Support.process draw restore) R).step s a t := by
  obtain ⟨n, l, v⟩ := s
  obtain ⟨m, l', v'⟩ := t
  cases a with
  | replenish =>
    constructor
    · intro h
      cases h
      exact ⟨⟨Nat.zero_le _, rfl⟩, rfl⟩
    · intro ⟨⟨_, e₁⟩, e₂⟩
      cases e₂
      cases e₁
      rfl
  | rebuild b =>
    constructor
    · intro ⟨k, hn, ht⟩
      cases ht
      subst hn
      exact ⟨⟨Nat.succ_le_succ (Nat.zero_le _), rfl⟩, rfl⟩
    · intro ⟨⟨_, e₁⟩, e₂⟩
      cases e₂
      change m + 1 = n at e₁
      subst e₁
      exact ⟨m, rfl, rfl⟩
  | correct =>
    constructor
    · intro ⟨hl, k, hn, ht⟩
      cases ht
      subst hn
      exact ⟨⟨Nat.succ_le_succ (Nat.zero_le _), rfl⟩, hl, rfl⟩
    · intro ⟨⟨_, e₁⟩, hl, e₂⟩
      cases e₂
      change m + 1 = n at e₁
      subst e₁
      exact ⟨hl, m, rfl, rfl⟩

theorem trace_iff {s t : State} {w : List Act} :
    Trace P s w t ↔ Trace (productProcess (Support.process draw restore) R) s w t :=
  ⟨Support.trace_mono (fun _ _ _ h => step_iff.mp h),
   Support.trace_mono (fun _ _ _ h => step_iff.mpr h)⟩

/-- The stock is a supported observable of Revising. -/
theorem supported : Support.Balanced P (fun s => s.1) draw restore ∧
    Support.DrawsHeld P (fun s => s.1) draw :=
  ⟨fun _ _ _ h => (step_iff.mp h).1.2, fun _ _ _ h => (step_iff.mp h).1.1⟩

/-- **Instance of `Support.product_feasible_iff`.** A course of reconstruction and correction
is executable exactly where the registration side admits it and the stock covers it. -/
theorem feasible_iff {s : State} {w : List Act} :
    Feasible P s w ↔ Support.Covered draw restore s.1 w ∧ Feasible R s.2 w :=
  ⟨fun ⟨t, h⟩ => Support.product_feasible_iff.mp ⟨t, trace_iff.mp h⟩,
   fun both => match Support.product_feasible_iff.mpr both with
     | ⟨t, h⟩ => ⟨t, trace_iff.mpr h⟩⟩

/-- Converse counterexample to "support enacts": covered, yet the registration blocks. -/
theorem covered_not_enacted :
    Support.Covered draw restore 1 [.correct] ∧ ¬ Feasible P (1, false, false) [.correct] :=
  ⟨⟨Nat.le_refl 1, trivial⟩, fun ⟨_, h⟩ => match h with
    | .cons step _ => Bool.noConfusion step.1⟩

/-- Converse counterexample to "registration enacts": the link admits correction, nothing
covers it. -/
theorem linked_not_enacted :
    Feasible R (true, false) [.correct] ∧ ¬ Feasible P (0, true, false) [.correct] :=
  ⟨⟨(true, true), .cons ⟨rfl, rfl⟩ (.nil _)⟩, fun ⟨_, h⟩ => match h with
    | .cons step _ => match step.2 with
      | ⟨_, bad, _⟩ => Nat.noConfusion bad⟩

end Revising

/-! ## P99: ReferencePlan through the support and contact laws -/

namespace ReferencePlan

theorem balanced : Support.Balanced P State.fuel cost (fun _ => 0) :=
  fun _ _ _ h => (step_account h).1

theorem spent_balanced : Support.Balanced P State.spent (fun _ => 0) cost :=
  fun _ _ _ h => (step_account h).2

theorem draws_held : Support.DrawsHeld P State.fuel cost := by
  intro s a t h
  change execute s a = some t at h
  unfold execute at h
  split at h
  next enough => exact enough
  next => contradiction

/-- `trace_account` as a corollary of `Support.trace_balance`. -/
theorem trace_account_of_law {s t : State} {as : List Act} (h : Trace P s as t) :
    t.fuel + t.spent = s.fuel + s.spent :=
  have fuel : t.fuel + total as cost = s.fuel :=
    (Support.trace_balance balanced h).trans (congrArg (s.fuel + ·) (Support.total_zero as))
  have spent : t.spent = s.spent + total as cost :=
    (congrArg (t.spent + ·) (Support.total_zero as)).symm.trans (Support.trace_balance spent_balanced h)
  calc t.fuel + t.spent = t.fuel + (s.spent + total as cost) := congrArg (t.fuel + ·) spent
    _ = (t.fuel + total as cost) + s.spent :=
        (congrArg (t.fuel + ·) (Nat.add_comm _ _)).trans (Nat.add_assoc _ _ _).symm
    _ = s.fuel + s.spent := congrArg (· + s.spent) fuel

/-- **Instance of `Support.covered_of_trace`.** Every executed course is covered by the fuel it
starts from; `support_too_small_to_build` and `no_action_after_exhaustion` are cases. -/
theorem covered {s t : State} {as : List Act} (h : Trace P s as t) :
    Support.Covered cost (fun _ => 0) s.fuel as :=
  Support.covered_of_trace balanced draws_held h

/-- `added_keeps` as an instance of `Contacts.keeps_iff_retains`. -/
theorem added_keeps_of_law (m : List Nat) (i : Nat) : Registration.Keeps Alike m (i :: m) :=
  (Contacts.keeps_iff_retains (fun p : List Nat => p) m (i :: m)).mpr fun _ h => List.Mem.tail i h

/-- `new_contact_choice` as an instance of `Contacts.added_gains`. -/
theorem new_contact_choice_of_law (m : List Nat) (i : Nat) (absent : i ∉ m) :
    Learning.Training.Through (Alike (i :: m)) (fun x => x i = true) ∧
      ¬ Learning.Training.Through (Alike m) (fun x => x i = true) :=
  Contacts.added_gains (List.Mem.head m) absent

/-- The revision rule reads the receipt and answers every failure. -/
theorem propose_answers : Contacts.Answers propose := fun _ _ => List.Mem.head _

theorem revise_registers_failure (m : List Nat) (i : Nat) :
    Learning.Training.Through (Alike (propose m (some i))) (fun x => x i = true) :=
  (Contacts.answers_iff propose).mpr propose_answers m i

/-- The frozen operation re-runs the retained method whatever the receipt. -/
def frozenRule : List Nat → Option Nat → List Nat := fun m _ => m

theorem frozen_reads_method (s : State) :
    (operate s .frozen).map State.pending = some (frozenRule s.method s.receipt) := rfl

theorem frozen_blind : Contacts.Blind frozenRule := fun _ _ => rfl

/-- **Instance of `Contacts.blind_misses`.** At every retained method, some failure is left
unregistered by the frozen rule; `frozen_method_still_fails` is one control of this law. -/
theorem frozen_misses (m : List Nat) :
    ∃ i, ¬ Learning.Training.Through (Alike (frozenRule m (some i))) (fun x => x i = true) :=
  Contacts.blind_misses frozen_blind Contacts.nat_unlisted m

theorem flip_is_pick (c : Bool → Bool) (b : Bool) :
    flip (c false) b = References.pick c false true b := by
  show flip (c false) b = (if c false = b then false else true)
  cases c false <;> cases b <;> rfl

/-- **Instance of `References.drives_iff`:** `checked_pair_correct` and its converse. -/
theorem checked_pair_iff (c : Bool → Bool) :
    (∀ target, c (flip (c false) target) = target) ↔ c false ≠ c true :=
  ⟨fun h => (References.drives_iff c false true).mp fun b =>
      (congrArg c (flip_is_pick c b)).symm.trans (h b),
   fun apart b => (congrArg c (flip_is_pick c b)).trans
      ((References.drives_iff c false true).mpr apart b)⟩

/-- **Instance of `References.inverted_fails`:** after drift a checked key fails at every
target; `drift_after_check_can_fail` is one control of this law. -/
theorem drift_fails (c : Bool → Bool) (apart : c false ≠ c true) (b : Bool) :
    (fun x => !(c x)) (flip (c false) b) ≠ b :=
  References.inverted_fails (e := fun b => flip (c false) b) ((checked_pair_iff c).mpr apart) b

end ReferencePlan

/-! ## P103: ContinuingRevision through the support laws -/

namespace ContinuingRevision

theorem balanced (yield : Nat) :
    Support.Balanced (P yield) (fun s => s.work.fuel) cost (returned yield) :=
  fun _ _ _ h => (step_account h).1

theorem cost_pos : ∀ a, 0 < cost a
  | .native (.perform _ _) => Nat.succ_pos 0
  | .native .revise => Nat.succ_pos 0
  | .native .probe => Nat.succ_pos 1
  | .native .install => Nat.succ_pos 0
  | .native .frozen => Nat.succ_pos 0
  | .native .erase => Nat.succ_pos 0
  | .native .drift => Nat.succ_pos 0
  | .renew => Nat.succ_pos 0

theorem renew_of_returned {yield : Nat} : ∀ {a : Act}, 0 < returned yield a → a = .renew
  | .native _, h => absurd h (Nat.lt_irrefl 0)
  | .renew, _ => rfl

theorem no_return : ∀ (s : State) (a : Act), s.work.fuel + returned 0 a = s.work.fuel
  | _, .native _ => rfl
  | _, .renew => rfl

/-- **Instance of `Run.not_of_depletion`.** With the return cut, no unending run exists at all,
whatever the controller; `cut_stops_next` is one finite control of this law. -/
theorem no_run_without_return (r : Run (P 0)) : False :=
  Run.not_of_depletion (fun s => s.work.fuel)
    (fun s a _ h => Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right (cost_pos a))
      (Nat.le_of_eq ((step_account h).1.trans (no_return s a)))) r

/-- **Instance of `Run.replenishes_of_draws`.** Along every run of every yield, renewal recurs. -/
theorem renew_recurs {yield : Nat} (r : Run (P yield)) : ∀ N, ∃ n, N ≤ n ∧ r.act n = .renew :=
  fun N => match Run.replenishes_of_draws (balanced yield) r
      (fun M => ⟨M, Nat.le_refl M, cost_pos _⟩) N with
  | ⟨n, le, pos⟩ => ⟨n, le, renew_of_returned pos⟩

theorem renew_needs_credit {yield : Nat} {s t : State} (h : (P yield).step s .renew t) :
    s.credit = true := by
  change execute yield s .renew = some t at h
  dsimp only [execute] at h
  split at h
  next cond =>
    cases hc : s.credit with
    | true => rfl
    | false =>
      rw [hc] at cond
      exact Bool.noConfusion cond
  next => contradiction

theorem credit_earned {yield : Nat} {s t : State} {a : Act} (h : (P yield).step s a t)
    (credit : t.credit = true) :
    ∃ i, a = .native (.perform i true) ∧ t.work.response = true := by
  cases a with
  | renew =>
    change execute yield s .renew = some t at h
    dsimp only [execute] at h
    split at h
    next =>
      split at h
      next =>
        cases Option.some.inj h
        exact Bool.noConfusion credit
      next => contradiction
    next => contradiction
  | native a =>
    change execute yield s (.native a) = some t at h
    dsimp only [execute] at h
    cases eq : ReferencePlan.execute s.work a with
    | none => rw [eq] at h; contradiction
    | some u =>
      rw [eq] at h
      cases Option.some.inj h
      cases a with
      | perform i b =>
        cases b with
        | false => exact Bool.noConfusion credit
        | true =>
          refine ⟨i, rfl, ?_⟩
          revert credit
          show (if i = s.carrier + 1 then u.response else false) = true → u.response = true
          split
          next => exact id
          next => exact fun c => Bool.noConfusion c
      | revise => exact Bool.noConfusion credit
      | probe => exact Bool.noConfusion credit
      | install => exact Bool.noConfusion credit
      | frozen => exact Bool.noConfusion credit
      | erase => exact Bool.noConfusion credit
      | drift => exact Bool.noConfusion credit

/-- **Successful activity recurs along every run of every yield.** Renewal recurs (the support
law), renewal needs credit, and credit is earned only by a successful undertaking. -/
theorem success_recurs {yield : Nat} (r : Run (P yield)) :
    ∀ N, ∃ n i, N ≤ n ∧ r.act n = .native (.perform i true) ∧
      (r.state (n + 1)).work.response = true :=
  fun N => match renew_recurs r (N + 1) with
  | ⟨0, le, _⟩ => absurd le (Nat.not_succ_le_zero N)
  | ⟨n + 1, le, renew⟩ =>
    have step : (P yield).step (r.state (n + 1)) .renew (r.state (n + 1 + 1)) :=
      Eq.mp (congrArg (fun a => (P yield).step (r.state (n + 1)) a (r.state (n + 1 + 1))) renew)
        (r.step (n + 1))
    match credit_earned (r.step n) (renew_needs_credit step) with
    | ⟨i, act, response⟩ => ⟨n, i, Nat.le_of_succ_le_succ le, act, response⟩

theorem history_cycles : ∀ k, history k = Support.cycles word k
  | 0 => rfl
  | k + 1 => congrArg (· ++ word k) (history_cycles k)

theorem word_cost (n : Nat) : total (word n) cost = 9 := rfl

theorem word_return (yield n : Nat) : total (word n) (returned yield) = yield := by
  show 0 + (0 + (0 + (0 + (0 + (0 + yield))))) = yield
  rw [Nat.zero_add, Nat.zero_add, Nat.zero_add, Nat.zero_add, Nat.zero_add, Nat.zero_add]

/-- **Instance of `Support.cycles_need`.** The revision cycle can be repeated for every number
of cycles, from any configuration, only where the yield covers its draw of nine. -/
theorem cycles_need_yield {yield : Nat} {s : State}
    (each : ∀ k, Feasible (P yield) s (history k)) : 9 ≤ yield :=
  Support.cycles_need (balanced yield) (w := word) word_cost (word_return yield)
    (fun k => history_cycles k ▸ each k)

theorem cycles_at_nine : ∀ k, Feasible (P 9) (ready 0) (history k) :=
  fun k => ⟨ready k, forget_policy (all_cycles k)⟩

/-- Up to nine, the cycle repeats without bound exactly at nine: the witness is tight. -/
theorem repeats_iff {yield : Nat} (le : yield ≤ 9) :
    (∃ s, ∀ k, Feasible (P yield) s (history k)) ↔ yield = 9 :=
  ⟨fun ⟨_, each⟩ => Nat.le_antisymm le (cycles_need_yield each),
   fun e => e ▸ ⟨ready 0, cycles_at_nine⟩⟩

end ContinuingRevision

end Becoming
