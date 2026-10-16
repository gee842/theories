import ReconfigurableSupportLogic

/-! Costed reads and atomic validated use in the existing access process.
Per-slot revisions are maintained by every admitted occupancy update. Reads
are coherent primitive observations; the model does not derive sensors or
hardware atomicity. The native projection erases reads, not their fuel cost. -/
namespace Generative.AcquiredSupportUse
open ReconfigurableSupportLogic
universe u
variable {R : Type u} [DecidableEq R]

structure World (R : Type u) where
  physical : Configuration R
  revision : R → Nat

structure Ticket (R : Type u) where
  slot : R
  revision : Nat
  occupied : Bool

def bump (rev : R → Nat) (r : R) : R → Nat :=
  fun i => if i = r then rev i + 1 else rev i

def update (w : World R) (e : Event R) : World R :=
  ⟨after w.physical e, match e with
    | .redirect _ => w.revision
    | .take => bump w.revision w.physical.route
    | .release r => bump w.revision r⟩

def sample (w : World R) : Ticket R :=
  ⟨w.physical.route, w.revision w.physical.route, w.physical.busy w.physical.route⟩

def Valid (w : World R) (t : Ticket R) : Prop :=
  t.revision ≤ w.revision t.slot ∧
    (t.revision = w.revision t.slot → t.occupied = w.physical.busy t.slot)

def Admits (w : World R) (t : Ticket R) : Prop :=
  t.slot = w.physical.route ∧ t.revision = w.revision t.slot ∧ t.occupied = false

omit [DecidableEq R] in
theorem sample_valid (w : World R) : Valid w (sample w) := ⟨Nat.le_refl _, fun _ => rfl⟩

theorem update_valid {w : World R} {t : Ticket R} (h : Valid w t) (e : Event R) :
    Valid (update w e) t := by
  cases e with
  | redirect r => exact h
  | take =>
    by_cases same : t.slot = w.physical.route
    · constructor
      · change t.revision ≤ bump w.revision w.physical.route t.slot
        simp only [bump, if_pos same]
        exact Nat.le_trans h.1 (Nat.le_succ _)
      · intro eq
        change t.revision = bump w.revision w.physical.route t.slot at eq
        simp only [bump, if_pos same] at eq
        have le := h.1
        omega
    · simpa [Valid, update, bump, after, setBusy, same] using h
  | release r =>
    by_cases same : t.slot = r
    · constructor
      · change t.revision ≤ bump w.revision r t.slot
        simp only [bump, if_pos same]
        exact Nat.le_trans h.1 (Nat.le_succ _)
      · intro eq
        change t.revision = bump w.revision r t.slot at eq
        simp only [bump, if_pos same] at eq
        have le := h.1
        omega
    · simpa [Valid, update, bump, after, setBusy, same] using h

omit [DecidableEq R] in
theorem admitted_is_free {w : World R} {t : Ticket R}
    (h : Valid w t) (ad : Admits w t) : w.physical.busy w.physical.route = false := by
  have eq := h.2 ad.2.1
  rw [ad.1] at eq
  exact eq.symm.trans ad.2.2

structure Session (R : Type u) where
  world : World R
  ticket : Option (Ticket R)
  fuel : Nat

inductive Action (R : Type u) where
  | change : Event R → Action R
  | read : Action R
  | use : Action R
  | reject : Action R

def Sound (s : Session R) : Prop := ∀ t, s.ticket = some t → Valid s.world t

def permitted (K : R → Prop) (s : Session R) : Action R → Prop
  | .change e => enabled K s.world.physical e
  | .read => K s.world.physical.route ∧ 0 < s.fuel
  | .use => K s.world.physical.route ∧ 0 < s.fuel ∧
      ∃ t, s.ticket = some t ∧ Admits s.world t
  | .reject => ∃ t, s.ticket = some t ∧ ¬ Admits s.world t

def next (s : Session R) : Action R → Session R
  | .change e => ⟨update s.world e, s.ticket, s.fuel⟩
  | .read => ⟨s.world, some (sample s.world), s.fuel - 1⟩
  | .use => ⟨update s.world .take, none, s.fuel - 1⟩
  | .reject => ⟨s.world, none, s.fuel⟩

def execution (K : R → Prop) : Process (Session R) (Action R) where
  step s a t := permitted K s a ∧ t = next s a

theorem next_sound {s : Session R} (h : Sound s) (a : Action R) : Sound (next s a) := by
  cases a with
  | change e => exact fun t ht => update_valid (h t ht) e
  | read =>
    intro t ht
    have eq : sample s.world = t := Option.some.inj ht
    subst t
    exact sample_valid _
  | use => intro t ht; cases ht
  | reject => intro t ht; cases ht

theorem trace_sound {K : R → Prop} {s t : Session R} {word : List (Action R)}
    (h : Sound s) (history : Trace (execution K) s word t) : Sound t := by
  induction history with
  | nil => exact h
  | cons step _ ih =>
    obtain ⟨_, rfl⟩ := step
    exact ih (next_sound h _)

theorem use_is_native {K : R → Prop} {s t : Session R}
    (h : Sound s) (step : (execution K).step s .use t) :
    (process K).step s.world.physical .take t.world.physical := by
  obtain ⟨⟨scope, _, receipt, stored, admitted⟩, rfl⟩ := step
  exact ⟨⟨scope, admitted_is_free (h receipt stored) admitted⟩, rfl⟩

def nativeWord : Action R → List (Event R)
  | .change e => [e]
  | .use => [.take]
  | .read | .reject => []

theorem step_projects {K : R → Prop} {s t : Session R} {a : Action R}
    (h : Sound s) (step : (execution K).step s a t) :
    Trace (process K) s.world.physical (nativeWord a) t.world.physical := by
  cases a with
  | change e =>
    obtain ⟨en, rfl⟩ := step
    exact .cons ⟨en, rfl⟩ (.nil _)
  | use => exact .cons (use_is_native h step) (.nil _)
  | read => obtain ⟨_, rfl⟩ := step; exact .nil _
  | reject => obtain ⟨_, rfl⟩ := step; exact .nil _

theorem trace_projects {K : R → Prop} {s t : Session R} {word : List (Action R)}
    (h : Sound s) (history : Trace (execution K) s word t) :
    Trace (process K) s.world.physical (word.flatMap nativeWord) t.world.physical := by
  induction history with
  | nil => exact .nil _
  | cons step _ ih =>
    have sn : Sound _ := by
      obtain ⟨_, rfl⟩ := step
      exact next_sound h _
    exact trace_append_iff.mpr ⟨_, step_projects h step, ih sn⟩

def charge : Action R → Nat
  | .read | .use => 1
  | .change _ | .reject => 0

def totalCharge : List (Action R) → Nat
  | [] => 0
  | a :: rest => charge a + totalCharge rest

theorem step_budget {K : R → Prop} {s t : Session R} {a : Action R}
    (step : (execution K).step s a t) : t.fuel + charge a = s.fuel := by
  obtain ⟨en, rfl⟩ := step
  cases a with
  | change e => rfl
  | reject => rfl
  | read => have pos := en.2; simp only [next, charge]; omega
  | use => have pos := en.2.1; simp only [next, charge]; omega

theorem trace_budget {K : R → Prop} {s t : Session R} {word : List (Action R)}
    (history : Trace (execution K) s word t) : t.fuel + totalCharge word = s.fuel := by
  induction history with
  | nil => rfl
  | cons step _ ih =>
    have first := step_budget step
    simp only [totalCharge]
    omega

theorem budget_necessary {K : R → Prop} {s : Session R} {word : List (Action R)}
    (history : Feasible (execution K) s word) : totalCharge word ≤ s.fuel := by
  obtain ⟨t, ht⟩ := history
  have balance := trace_budget ht
  omega

theorem fresh_read_use {K : R → Prop} (s : Session R)
    (scope : K s.world.physical.route) (free : s.world.physical.busy s.world.physical.route = false)
    (budget : 2 ≤ s.fuel) :
    Trace (execution K) s [.read, .use] (next (next s .read) .use) := by
  refine .cons ⟨⟨scope, by omega⟩, rfl⟩ (.cons ?_ (.nil _))
  refine ⟨⟨scope, ?_, sample s.world, rfl, rfl, rfl, free⟩, rfl⟩
  change 0 < s.fuel - 1
  omega

theorem fresh_read_use_iff (K : R → Prop) (s : Session R) :
    Feasible (execution K) s [.read, .use] ↔
      K s.world.physical.route ∧ s.world.physical.busy s.world.physical.route = false ∧
      2 ≤ s.fuel := by
  constructor
  · intro feasible
    have budget := budget_necessary feasible
    obtain ⟨t, history⟩ := feasible
    obtain ⟨mid, first, tail⟩ := trace_cons_iff.mp history
    obtain ⟨readEn, rfl⟩ := first
    have useStep := trace_singleton_iff.mp tail
    obtain ⟨_, _, receipt, stored, ad⟩ := useStep.1
    have eq : sample s.world = receipt := Option.some.inj stored
    subst receipt
    exact ⟨readEn.1, ad.2.2, budget⟩
  · rintro ⟨scope, free, budget⟩
    exact ⟨_, fresh_read_use s scope free budget⟩

theorem unrelated_release_admits {w : World R} {t : Ticket R} (h : Admits w t)
    (r : R) (different : t.slot ≠ r) : Admits (update w (.release r)) t := by
  simpa [Admits, update, after, bump, different] using h

theorem intervening_take_rejects (s : Session R) :
    ¬ Admits (update s.world .take) (sample s.world) := by
  intro h
  have eq := h.2.1
  change s.world.revision s.world.physical.route =
    bump s.world.revision s.world.physical.route s.world.physical.route at eq
  simp [bump] at eq

end Generative.AcquiredSupportUse

#print axioms Generative.AcquiredSupportUse.sample_valid
#print axioms Generative.AcquiredSupportUse.update_valid
#print axioms Generative.AcquiredSupportUse.admitted_is_free
#print axioms Generative.AcquiredSupportUse.next_sound
#print axioms Generative.AcquiredSupportUse.trace_sound
#print axioms Generative.AcquiredSupportUse.use_is_native
#print axioms Generative.AcquiredSupportUse.step_projects
#print axioms Generative.AcquiredSupportUse.trace_projects
#print axioms Generative.AcquiredSupportUse.step_budget
#print axioms Generative.AcquiredSupportUse.trace_budget
#print axioms Generative.AcquiredSupportUse.budget_necessary
#print axioms Generative.AcquiredSupportUse.fresh_read_use
#print axioms Generative.AcquiredSupportUse.fresh_read_use_iff
#print axioms Generative.AcquiredSupportUse.unrelated_release_admits
#print axioms Generative.AcquiredSupportUse.intervening_take_rejects
