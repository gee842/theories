import Becoming.Learning
import Becoming.Stock

/-!
# Selection when the registration itself changes

One Process supplies actual changes of configuration. A registration at each configuration
reads distinctions within that unfolding; its index is not an outside selector. Reuse
Learning.Training.Through (and hence Web.SelectsThrough), rather than another notion of selection.
Every old selection survives a change exactly when new indistinguishability implies old
indistinguishability. Along actual traces this composes. It says nothing by itself about
whether a selected corrective action remains enabled.

A history of the registrations actually made is different from applying the latest apparatus
retroactively. Keeping that history preserves distinctions; a physical memory doing so is
an additional correspondence condition. A finite Process instance changes its registration
and the availability of correction through reconstruction that draws on a stock. Both opening
and closing are executable; neither is selected inevitably. Its stock, replenishment and
construction recipe are local supplied relations, not universal primitives.

That instance is a registration process run jointly with its stock, step for step
(`Revising.step_iff`), so the general laws of `Becoming.Stock` apply to it: a course of
reconstruction and correction is executable exactly where the registration admits it and the
stock covers it (`Revising.feasible_iff`). Discrimination, stock and enactment stay distinct: a
covered correction can be blocked by the registration (`Revising.covered_not_enacted`), and a
correction the link admits can lack stock (`Revising.linked_not_enacted`).
-/

namespace Becoming

open Generative

namespace Learning.Training

variable {X : Type u}

/-- Every selection through the old relation remains through the new one exactly where
the new relation identifies no previously distinguishable pair. Only the old relation's
equivalence properties are needed for the converse. -/
theorem keeps_through_iff {old new : X → X → Prop}
    (refl : ∀ x, old x x) (symm : ∀ x y, old x y → old y x)
    (trans : ∀ x y z, old x y → old y z → old x z) :
    (∀ select, Through old select → Through new select) ↔
      (∀ x y, new x y → old x y) := by
  constructor
  · intro keeps x y same
    have cell : Through old (old x) := fun a b ab =>
      ⟨fun xa => trans x a b xa ab, fun xb => trans x b a xb (symm a b ab)⟩
    exact (keeps (old x) cell x y same).mp (refl x)
  · intro refines select through x y same
    exact through x y (refines x y same)

/-- Losing a distinction loses an old selection, constructively, without deciding all
selections or all histories. -/
theorem lost_choice {old new : X → X → Prop}
    (refl : ∀ x, old x x) (symm : ∀ x y, old x y → old y x)
    (trans : ∀ x y z, old x y → old y z → old x z)
    {x y : X} (merged : new x y) (apart : ¬ old x y) :
    ∃ select, Through old select ∧ ¬ Through new select :=
  ⟨old x,
   fun a b ab => ⟨fun xa => trans x a b xa ab, fun xb => trans x b a xb (symm a b ab)⟩,
   fun through => apart ((through x y merged).mp (refl x))⟩

end Learning.Training

namespace Registration

variable {S : Type u} {A : Type v} {X : Type w} {V : Type z}

/-- The new registration preserves distinctions of the old one. -/
def Keeps (alike : S → X → X → Prop) (s t : S) : Prop :=
  ∀ x y, alike t x y → alike s x y

theorem Keeps.refl (alike : S → X → X → Prop) (s : S) : Keeps alike s s :=
  fun _ _ h => h

theorem Keeps.trans {alike : S → X → X → Prop} {s t u : S}
    (st : Keeps alike s t) (tu : Keeps alike t u) : Keeps alike s u :=
  fun x y h => st x y (tu x y h)

/-- The criterion is exact, not an automatic consequence of being a revision. -/
theorem keeps_iff {alike : S → X → X → Prop} {s t : S}
    (refl : ∀ x, alike s x x) (symm : ∀ x y, alike s x y → alike s y x)
    (trans : ∀ x y z, alike s x y → alike s y z → alike s x z) :
    Keeps alike s t ↔
      ∀ select, Learning.Training.Through (alike s) select → Learning.Training.Through (alike t) select :=
  (Learning.Training.keeps_through_iff refl symm trans).symm

/-- This includes the existing web registration without equating propositions by propext. -/
theorem web_keeps_iff {F C : Type} {W : Web F C} {obs obs' : F → C → Prop}
    {f : F} {t u : Nat} :
    (∀ l l', W.RegistersAlikeUpTo obs' f l l' u → W.RegistersAlikeUpTo obs f l l' t) ↔
    (∀ select, W.SelectsThrough obs f t select → W.SelectsThrough obs' f u select) :=
  (Learning.Training.keeps_through_iff
    (fun _ _ _ => Web.RegistersAlike.refl _)
    (fun _ _ h => h.symm) (fun _ _ _ h k => h.trans k)).symm

/-- Preservation composes along the process's actual intermediate configurations. -/
theorem trace_keeps {P : Process S A} {alike : S → X → X → Prop}
    (step_keeps : ∀ s a t, P.step s a t → Keeps alike s t)
    {s t : S} {as : List A} (path : Trace P s as t) : Keeps alike s t := by
  induction path with
  | nil s => exact Keeps.refl alike s
  | cons step tail ih => exact (step_keeps _ _ _ step).trans ih

/-- No fresh reset of conditions is inserted between revisions. -/
theorem run_keeps {P : Process S A} (r : Run P) {alike : S → X → X → Prop}
    (step_keeps : ∀ s a t, P.step s a t → Keeps alike s t) (n k : Nat) :
    Keeps alike (r.state n) (r.state (n + k)) :=
  trace_keeps step_keeps (r.window_trace k n)

/-- The observations actually made through this step. Reading it as a usable present record
requires an actual retention mechanism; this definition does not provide one. -/
def History {P : Process S A} (r : Run P) (alike : S → X → X → Prop)
    (t : Nat) (x y : X) : Prop := ∀ n, n ≤ t → alike (r.state n) x y

theorem history_keeps {P : Process S A} (r : Run P) (alike : S → X → X → Prop)
    {t u : Nat} (le : t ≤ u) :
    ∀ x y, History r alike u x y → History r alike t x y :=
  fun _ _ h n before => h n (Nat.le_trans before le)

theorem through_history_later {P : Process S A} (r : Run P)
    {alike : S → X → X → Prop} {t u : Nat} {select : X → Prop}
    (through : Learning.Training.Through (History r alike t) select) (le : t ≤ u) :
    Learning.Training.Through (History r alike u) select :=
  fun x y h => through x y (history_keeps r alike le x y h)

/-- Registering through a jointly retained old and new reading preserves both. -/
theorem retained_keeps (old fresh : X → V) :
    ∀ x y, (old x, fresh x) = (old y, fresh y) → old x = old y :=
  fun _ _ h => congrArg Prod.fst h

/-- A new distinction in a retained reading is unavailable through the old reading. -/
theorem retained_gains {old fresh : X → V} {x y : X}
    (same : old x = old y) (different : fresh x ≠ fresh y) :
    ∃ select, Learning.Training.Through (fun a b => (old a, fresh a) = (old b, fresh b)) select ∧
      ¬ Learning.Training.Through (fun a b => old a = old b) select :=
  Learning.Training.lost_choice (fun _ => rfl) (fun _ _ h => h.symm)
    (fun _ _ _ h k => h.trans k) same (fun h => different (congrArg Prod.snd h))

end Registration

/-! ## A resource-dependent reconstruction within one Process -/

namespace Revising

/-- The stock supports activity; the mode records the distinguishing link, and the last
coordinate is the current response to a supplied target true.
These are coordinates of one configuration, not independent foundational entities. -/
abbrev State := Nat × Bool × Bool

inductive Act where
  | replenish
  | rebuild (mode : Bool)
  | correct

/-- Replenishment supplies one unit; rebuilding consumes one and changes registration;
correction consumes one, needs the distinguishing link, and changes the response to the
supplied target true. This is an actual response change, not a proof that the target is right. These local laws are supplied. -/
def P : Process State Act := ⟨fun s a t => match a with
  | .replenish => t = (s.1 + 1, s.2)
  | .rebuild b => ∃ n, s.1 = n + 1 ∧ t = (n, b, s.2.2)
  | .correct => s.2.1 = true ∧ ∃ n, s.1 = n + 1 ∧ t = (n, true, true)⟩

/-- The built link separates two represented alternatives. -/
def read (s : State) (b : Bool) : Bool := if s.2.1 then b else false

def alike (s : State) (b c : Bool) : Prop := read s b = read s c

theorem determined : Determined P := by
  intro s a t u h k
  cases a with
  | replenish => exact h.trans k.symm
  | rebuild b =>
    obtain ⟨n, hn, ht⟩ := h
    obtain ⟨m, hm, hu⟩ := k
    have eq := Nat.succ.inj (hn.symm.trans hm)
    exact ht.trans ((congrArg (fun i => (i, b, s.2.2)) eq).trans hu.symm)
  | correct =>
    obtain ⟨_, n, hn, ht⟩ := h
    obtain ⟨_, m, hm, hu⟩ := k
    have eq := Nat.succ.inj (hn.symm.trans hm)
    exact ht.trans ((congrArg (fun i => (i, true, true)) eq).trans hu.symm)

theorem rebuild_enabled_iff (s : State) (b : Bool) :
    Enabled P s (.rebuild b) ↔ ∃ n, s.1 = n + 1 :=
  ⟨fun ⟨_, n, stock, _⟩ => ⟨n, stock⟩,
   fun ⟨n, stock⟩ => ⟨(n, b, s.2.2), n, stock, rfl⟩⟩

theorem correction_enabled_iff (s : State) :
    Enabled P s .correct ↔ s.2.1 = true ∧ ∃ n, s.1 = n + 1 :=
  ⟨fun ⟨_, link, n, stock, _⟩ => ⟨link, n, stock⟩,
   fun ⟨link, n, stock⟩ => ⟨(n, true, true), link, n, stock, rfl⟩⟩

theorem opened_keeps (n m : Nat) : Registration.Keeps alike (n, false, false) (m, true, false) :=
  fun _ _ _ => rfl

theorem opened_choice (n : Nat) : Learning.Training.Through (alike (n, true, false)) (fun b => b = true) :=
  fun _ _ h => ⟨fun yes => h.symm.trans yes, fun yes => h.trans yes⟩

theorem closed_loses (n : Nat) : ¬ Learning.Training.Through (alike (n, false, false)) (fun b => b = true) :=
  fun through => Bool.noConfusion ((through true false rfl).mp rfl)

/-- Old registration cannot distinguish the two reconstruction choices, although one forms
and the other removes the link. The statement concerns represented modes, not all actions. -/
theorem old_cannot_select_rebuild (n : Nat) (select : Bool → Prop)
    (through : Learning.Training.Through (alike (n, false, false)) select) : select true ↔ select false :=
  through true false rfl

/-- Both changes occur in one admissible continuation, with replenishment and consumption. -/
theorem rebuild_then_close : Trace P (0, false, false)
    [.replenish, .replenish, .rebuild true, .correct, .replenish, .rebuild false] (0, false, true) :=
  .cons rfl (.cons rfl (.cons ⟨1, rfl, rfl⟩
    (.cons ⟨rfl, 0, rfl, rfl⟩ (.cons rfl (.cons ⟨0, rfl, rfl⟩ (.nil _))))))

/-- Forming a distinction can consume the last support for using it. -/
theorem opens_without_correction :
    P.step (1, false, false) (.rebuild true) (0, true, false) ∧
    Learning.Training.Through (alike (0, true, false)) (fun b => b = true) ∧ ¬ Enabled P (0, true, false) .correct :=
  ⟨⟨0, rfl, rfl⟩, opened_choice 0,
   fun h => match (correction_enabled_iff _).mp h with
     | ⟨_, _, bad⟩ => Nat.noConfusion bad⟩

/-- A remaining unit connects improved discrimination to an actual enabled correction. -/
theorem opens_with_correction :
    P.step (2, false, false) (.rebuild true) (1, true, false) ∧
    Learning.Training.Through (alike (1, true, false)) (fun b => b = true) ∧ Enabled P (1, true, false) .correct :=
  ⟨⟨1, rfl, rfl⟩, opened_choice 1, (0, true, true), rfl, 0, rfl, rfl⟩

/-- Actual closing destroys a formerly available distinction, even with support left. -/
theorem closes_choice : P.step (2, true, false) (.rebuild false) (1, false, false) ∧
    Learning.Training.Through (alike (2, true, false)) (fun b => b = true) ∧
    ¬ Learning.Training.Through (alike (1, false, false)) (fun b => b = true) ∧
    ¬ Enabled P (1, false, false) .correct :=
  ⟨⟨1, rfl, rfl⟩, opened_choice 2, closed_loses 1,
   fun h => Bool.noConfusion ((correction_enabled_iff _).mp h).1⟩

/-- A supplied controller reads current stock and the apparatus status: replenish when
empty, form the missing link when supported, otherwise use it. It observes no hidden target
bit. Its preference for forming the link is supplied, not derived from the old reading. -/
def choose : State → Act
  | (0, _) => .replenish
  | (_ + 1, false, _) => .rebuild true
  | (_ + 1, true, _) => .correct

def next : State → State
  | (0, b) => (1, b)
  | (n + 1, false, r) => (n, true, r)
  | (n + 1, true, _) => (n, true, true)

theorem chosen_step : ∀ s, P.step s (choose s) (next s)
  | (0, _) => rfl
  | (n + 1, false, _) => ⟨n, rfl, rfl⟩
  | (n + 1, true, _) => ⟨rfl, n, rfl, rfl⟩

/-- An actual closed-loop run of the existing process, not a reset between episodes. -/
def controlled : Run P :=
  ⟨Law.orbit next (0, false, false), fun n => choose (Law.orbit next (0, false, false) n),
   fun n => chosen_step (Law.orbit next (0, false, false) n)⟩

/-- The selected reconstruction forms a finer registration. Its support is exhausted there;
ordinary replenishment then restores the actual corrective continuation, which is taken. -/
theorem controlled_revision :
    controlled.act 1 = .rebuild true ∧ controlled.state 2 = (0, true, false) ∧
    ¬ Learning.Training.Through (alike (controlled.state 0)) (fun b => b = true) ∧
    Learning.Training.Through (alike (controlled.state 2)) (fun b => b = true) ∧
    ¬ Enabled P (controlled.state 2) .correct ∧
    controlled.act 2 = .replenish ∧ controlled.act 3 = .correct ∧
    P.step (controlled.state 3) .correct (controlled.state 4) ∧
    (controlled.state 3).2.2 = false ∧ (controlled.state 4).2.2 = true :=
  ⟨rfl, rfl, closed_loses 0, opened_choice 0, opens_without_correction.2.2,
   rfl, rfl, controlled.step 3, rfl, rfl⟩

/-! ### Revising is a registration process run jointly with its stock -/

/-- The registration side: the link (first) and the response (second). -/
def registration : Process (Bool × Bool) Act := ⟨fun s a t => match a with
  | .replenish => t = s
  | .rebuild b => t = (b, s.2)
  | .correct => s.1 = true ∧ t = (true, true)⟩

/-- What each act draws from the stock. -/
def draw : Act → Nat
  | .replenish => 0
  | .rebuild _ => 1
  | .correct => 1

/-- What each act restores to the stock. -/
def restore : Act → Nat
  | .replenish => 1
  | .rebuild _ => 0
  | .correct => 0

/-- **Revising is the stock process run jointly with the registration, step for step.** -/
theorem step_iff {s t : State} {a : Act} :
    P.step s a t ↔ (productProcess (Stock.process draw restore) registration).step s a t := by
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
    Trace P s w t ↔ Trace (productProcess (Stock.process draw restore) registration) s w t :=
  ⟨Stock.trace_mono (fun _ _ _ h => step_iff.mp h),
   Stock.trace_mono (fun _ _ _ h => step_iff.mpr h)⟩

/-- The stock of Revising is balanced and drawn only from what is held. -/
theorem stock_balanced_held : Stock.Balanced P (fun s => s.1) draw restore ∧
    Stock.DrawsHeld P (fun s => s.1) draw :=
  ⟨fun _ _ _ h => (step_iff.mp h).1.2, fun _ _ _ h => (step_iff.mp h).1.1⟩

/-- **Instance of `Stock.product_feasible_iff`.** A course of reconstruction and correction
is executable exactly where the registration side admits it and the stock covers it. -/
theorem feasible_iff {s : State} {w : List Act} :
    Feasible P s w ↔ Stock.Covered draw restore s.1 w ∧ Feasible registration s.2 w :=
  ⟨fun ⟨t, h⟩ => Stock.product_feasible_iff.mp ⟨t, trace_iff.mp h⟩,
   fun both => match Stock.product_feasible_iff.mpr both with
     | ⟨t, h⟩ => ⟨t, trace_iff.mpr h⟩⟩

/-- Stock does not enact: a correction the stock covers, which the registration blocks. -/
theorem covered_not_enacted :
    Stock.Covered draw restore 1 [.correct] ∧ ¬ Feasible P (1, false, false) [.correct] :=
  ⟨⟨Nat.le_refl 1, trivial⟩, fun ⟨_, h⟩ => match h with
    | .cons step _ => Bool.noConfusion step.1⟩

/-- Registration does not enact: the link admits correction, and no stock covers it. -/
theorem linked_not_enacted :
    Feasible registration (true, false) [.correct] ∧ ¬ Feasible P (0, true, false) [.correct] :=
  ⟨⟨(true, true), .cons ⟨rfl, rfl⟩ (.nil _)⟩, fun ⟨_, h⟩ => match h with
    | .cons step _ => match step.2 with
      | ⟨_, bad, _⟩ => Nat.noConfusion bad⟩

end Revising
end Becoming
