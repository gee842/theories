import EnactedOrientation -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Change.held_over_stretch`, `Becoming.Change.over_stretch` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md

/-!
# Actual restoration keeps the interruption in the history

This module closes the immediate/eventual adequacy question left by the
enacted-orientation handoff. It does not introduce a moral predicate.

For one derived or supplied Boolean capacity, loss and recovery are counted at
the same immediate level in the actual `Run`. Unavailable destination occasions
are retained separately. The counts compose, and loss/recovery balance is fixed
by endpoints. The interruption count is not canceled by recovery.

A single two-state process admits continuously open histories and histories
which close and restore an activity arbitrarily many times. Every action remains
eventually realizable at every state. Nevertheless the latter histories contain
arbitrarily many unavailable occasions. A return path can also be postponed
arbitrarily long. Thus recoverability and matched recovery do not license a
reduction of the whole-history appraisal to eventual realizability.

The observation occasions and the capacity being followed remain model inputs;
counts are not durations or ethical weights. The concrete capacity is derived
from the enabling relation of the same process, not independently labeled.
-/

namespace Generative.Naturalism.ActualRecovery

universe u v
variable {State : Type u} {Action : Type v} {P : Process State Action}

def present : Bool → Nat
  | false => 0
  | true => 1

def absent : Bool → Nat
  | false => 1
  | true => 0

def loss (x y : Bool) : Nat :=
  match x with
  | false => 0
  | true => match y with
    | false => 1
    | true => 0

def recovery (x y : Bool) : Nat :=
  match x with
  | true => 0
  | false => match y with
    | false => 0
    | true => 1

def losses (c : State → Bool) : {s t : State} → Run P s t → Nat
  | _, _, .nil _ => 0
  | s, _, .cons (m := m) _ _ r => loss (c s) (c m) + losses c r

def recoveries (c : State → Bool) : {s t : State} → Run P s t → Nat
  | _, _, .nil _ => 0
  | s, _, .cons (m := m) _ _ r => recovery (c s) (c m) + recoveries c r

/-- The initial state is excluded, so concatenation never duplicates its boundary. -/
def interruptions (c : State → Bool) : {s t : State} → Run P s t → Nat
  | _, _, .nil _ => 0
  | _, _, .cons (m := m) _ _ r => absent (c m) + interruptions c r

theorem local_balance (x y : Bool) :
    loss x y + present y = recovery x y + present x := by
  cases x <;> cases y <;> rfl

theorem losses_append (c : State → Bool) {s m t : State}
    (r : Run P s m) (r' : Run P m t) :
    losses c (r.append r') = losses c r + losses c r' := by
  induction r with
  | nil => exact (Nat.zero_add _).symm
  | cons _ _ r ih =>
    change _ + losses c (r.append r') = (_ + _) + _
    rw [ih, Nat.add_assoc]

theorem recoveries_append (c : State → Bool) {s m t : State}
    (r : Run P s m) (r' : Run P m t) :
    recoveries c (r.append r') = recoveries c r + recoveries c r' := by
  induction r with
  | nil => exact (Nat.zero_add _).symm
  | cons _ _ r ih =>
    change _ + recoveries c (r.append r') = (_ + _) + _
    rw [ih, Nat.add_assoc]

theorem interruptions_append (c : State → Bool) {s m t : State}
    (r : Run P s m) (r' : Run P m t) :
    interruptions c (r.append r') = interruptions c r + interruptions c r' := by
  induction r with
  | nil => exact (Nat.zero_add _).symm
  | cons _ _ r ih =>
    change _ + interruptions c (r.append r') = (_ + _) + _
    rw [ih, Nat.add_assoc]

/-- This balance counts actual events at one level; hypothetical paths do not enter. -/
theorem actual_balance (c : State → Bool) {s t : State} (r : Run P s t) :
    losses c r + present (c t) = recoveries c r + present (c s) := by
  induction r with
  | nil => rfl
  | @cons s m t a h r ih =>
    change loss (c s) (c m) + losses c r + present (c t) =
      recovery (c s) (c m) + recoveries c r + present (c s)
    cases hs : c s <;> cases hm : c m
    · simpa only [hs, hm, loss, recovery, present, Nat.zero_add, Nat.add_zero] using ih
    · rw [hm] at ih
      change losses c r + present (c t) = recoveries c r + 1 at ih
      simpa only [hs, hm, loss, recovery, present, Nat.zero_add, Nat.add_zero,
        Nat.add_comm 1] using ih
    · rw [hm] at ih
      change losses c r + present (c t) = recoveries c r + 0 at ih
      rw [Nat.add_zero] at ih
      change (1 + losses c r) + present (c t) = (0 + recoveries c r) + 1
      rw [Nat.zero_add, Nat.add_assoc, ih, Nat.add_comm]
    · rw [hm] at ih
      simpa only [hs, hm, loss, recovery, present, Nat.zero_add] using ih

theorem restored_balance (c : State → Bool) {s t : State} (r : Run P s t)
    (h : c s = c t) : losses c r = recoveries c r := by
  have hb := actual_balance c r
  rw [h] at hb
  cases hc : c t
  · rw [hc] at hb
    exact hb
  · rw [hc] at hb
    exact Nat.succ.inj hb

/-- The past interruption remains part of the whole after any continuation. -/
theorem continuation_keeps_interruption (c : State → Bool) {s m t : State}
    (r : Run P s m) (r' : Run P m t) :
    interruptions c r ≤ interruptions c (r.append r') := by
  rw [interruptions_append]
  exact Nat.le_add_right _ _

/-- Actual losses cannot exceed unavailable occasions in this observation convention. -/
theorem losses_le_interruptions (c : State → Bool) {s t : State} (r : Run P s t) :
    losses c r ≤ interruptions c r := by
  induction r with
  | nil => exact Nat.le_refl _
  | @cons s m t a h r ih =>
    change loss (c s) (c m) + losses c r ≤ absent (c m) + interruptions c r
    have hl : loss (c s) (c m) ≤ absent (c m) := by
      cases c s <;> cases c m <;> decide
    exact Nat.add_le_add hl ih

/-- A restored history containing a loss has recovery AND a retained interruption. -/
theorem restored_loss_is_not_erased (c : State → Bool) {s t : State}
    (r : Run P s t) (heq : c s = c t) (hl : 0 < losses c r) :
    0 < recoveries c r ∧ 0 < interruptions c r := by
  constructor
  · rw [← restored_balance c r heq]
    exact hl
  · exact Nat.lt_of_lt_of_le hl (losses_le_interruptions c r)

/-! ## A finite, same-process rival to eventual-level reduction -/

inductive Act where
  | close
  | restore
  | hold
  | realize

/-- The states describe one relation: whether `realize` is currently enabled.
`close`/`restore` change that relation; `hold` retains it. -/
def recurring : Process Bool Act where
  step s a t := match a with
    | .close => s = true ∧ t = false
    | .restore => s = false ∧ t = true
    | .hold => t = s
    | .realize => s = true ∧ t = true

theorem ready_is_enabled (s : Bool) : s = true ↔ Enabled recurring s .realize := by
  constructor
  · intro hs
    exact ⟨true, hs, rfl⟩
  · rintro ⟨t, hs, _⟩
    exact hs

theorem states_reach (s t : Bool) : Reach recurring s t := by
  cases s <;> cases t
  · exact ⟨[], .nil _⟩
  · exact ⟨[.restore], .cons ⟨rfl, rfl⟩ (.nil _)⟩
  · exact ⟨[.close], .cons ⟨rfl, rfl⟩ (.nil _)⟩
  · exact ⟨[], .nil _⟩

theorem every_action_eventually (s : Bool) (a : Act) : Can recurring s a := by
  have enabled_somewhere : ∃ t, Enabled recurring t a := by
    cases a with
    | close => exact ⟨true, false, rfl, rfl⟩
    | restore => exact ⟨false, true, rfl, rfl⟩
    | hold => exact ⟨true, true, rfl⟩
    | realize => exact ⟨true, true, rfl, rfl⟩
  obtain ⟨t, ht⟩ := enabled_somewhere
  obtain ⟨w, hw⟩ := states_reach s t
  exact can_of_reach hw (can_of_enabled ht)

/-- Neither the full eventual activity profile nor its orientation distinguishes states. -/
theorem eventual_profiles_identical (s t : Bool) :
    CanLe recurring s t ∧ CanLe recurring t s :=
  ⟨fun a _ => every_action_eventually t a, fun a _ => every_action_eventually s a⟩

def episode : Run recurring true true :=
  .cons .close ⟨rfl, rfl⟩ (.cons .restore ⟨rfl, rfl⟩ (.nil true))

def episodes : Nat → Run recurring true true
  | 0 => .nil true
  | n + 1 => episode.append (episodes n)

def maintained : Nat → Run recurring true true
  | 0 => .nil true
  | n + 1 => .cons .realize ⟨rfl, rfl⟩
      (.cons .hold rfl (maintained n))

theorem episode_profile :
    losses id episode = 1 ∧ recoveries id episode = 1 ∧
      interruptions id episode = 1 := ⟨rfl, rfl, rfl⟩

theorem episodes_profile (n : Nat) :
    losses id (episodes n) = n ∧ recoveries id (episodes n) = n ∧
      interruptions id (episodes n) = n := by
  induction n with
  | zero => exact ⟨rfl, rfl, rfl⟩
  | succ n ih =>
    change losses id (episode.append (episodes n)) = n + 1 ∧
      recoveries id (episode.append (episodes n)) = n + 1 ∧
      interruptions id (episode.append (episodes n)) = n + 1
    rw [losses_append, recoveries_append, interruptions_append,
      episode_profile.1, episode_profile.2.1, episode_profile.2.2,
      ih.1, ih.2.1, ih.2.2, Nat.add_comm 1 n]
    exact ⟨rfl, rfl, rfl⟩

theorem maintained_profile (n : Nat) :
    losses id (maintained n) = 0 ∧ recoveries id (maintained n) = 0 ∧
      interruptions id (maintained n) = 0 := by
  induction n with
  | zero => exact ⟨rfl, rfl, rfl⟩
  | succ n ih =>
    change 0 + (0 + losses id (maintained n)) = 0 ∧
      0 + (0 + recoveries id (maintained n)) = 0 ∧
      0 + (0 + interruptions id (maintained n)) = 0
    simpa only [Nat.zero_add] using ih

theorem histories_same_length (n : Nat) :
    (episodes n).word.length = n * 2 ∧ (maintained n).word.length = n * 2 := by
  induction n with
  | zero => exact ⟨rfl, rfl⟩
  | succ n ih =>
    constructor
    · change (episode.append (episodes n)).word.length = (n + 1) * 2
      rw [Run.word_append, length_append_word]
      change 2 + (episodes n).word.length = (n + 1) * 2
      rw [ih.1, Nat.succ_mul, Nat.add_comm 2]
    · change (maintained n).word.length + 1 + 1 = (n + 1) * 2
      rw [ih.2, Nat.succ_mul, Nat.add_assoc]

/-- A real return after every loss still leaves arbitrarily much actual interruption. -/
theorem matched_recovery_unbounded :
    ∀ n, ∃ r : Run recurring true true,
      losses id r = recoveries id r ∧ interruptions id r = n := by
  intro n
  exact ⟨episodes n, (episodes_profile n).1.trans (episodes_profile n).2.1.symm,
    (episodes_profile n).2.2⟩

def postponed : Nat → Run recurring false false
  | 0 => .nil false
  | n + 1 => .cons .hold rfl (postponed n)

theorem postponed_profile (n : Nat) :
    recoveries id (postponed n) = 0 ∧ interruptions id (postponed n) = n := by
  induction n with
  | zero => exact ⟨rfl, rfl⟩
  | succ n ih =>
    constructor
    · change 0 + recoveries id (postponed n) = 0
      rw [Nat.zero_add, ih.1]
    · change 1 + interruptions id (postponed n) = n + 1
      rw [ih.2, Nat.add_comm]

/-- Reachable restoration guarantees no actual recovery or finite delay bound. -/
theorem eventual_is_not_actual_recovery :
    Can recurring false .realize ∧ ∀ n, ∃ r : Run recurring false false,
      recoveries id r = 0 ∧ interruptions id r = n :=
  ⟨every_action_eventually false .realize, fun n => ⟨postponed n, postponed_profile n⟩⟩

/-- No function of endpoints alone represents the actual interruption profile. -/
theorem interruptions_not_endpoint_determined :
    ¬ ∃ f : Bool → Bool → Nat,
      ∀ s t (r : Run recurring s t), interruptions id r = f s t := by
  rintro ⟨f, hf⟩
  have h0 := hf true true (maintained 1)
  have h1 := hf true true (episodes 1)
  rw [(maintained_profile 1).2.2] at h0
  rw [(episodes_profile 1).2.2] at h1
  exact Nat.noConfusion (h0.trans h1.symm)

end Generative.Naturalism.ActualRecovery

#print axioms Generative.Naturalism.ActualRecovery.local_balance
#print axioms Generative.Naturalism.ActualRecovery.losses_append
#print axioms Generative.Naturalism.ActualRecovery.recoveries_append
#print axioms Generative.Naturalism.ActualRecovery.interruptions_append
#print axioms Generative.Naturalism.ActualRecovery.actual_balance
#print axioms Generative.Naturalism.ActualRecovery.restored_balance
#print axioms Generative.Naturalism.ActualRecovery.continuation_keeps_interruption
#print axioms Generative.Naturalism.ActualRecovery.losses_le_interruptions
#print axioms Generative.Naturalism.ActualRecovery.restored_loss_is_not_erased
#print axioms Generative.Naturalism.ActualRecovery.ready_is_enabled
#print axioms Generative.Naturalism.ActualRecovery.states_reach
#print axioms Generative.Naturalism.ActualRecovery.every_action_eventually
#print axioms Generative.Naturalism.ActualRecovery.eventual_profiles_identical
#print axioms Generative.Naturalism.ActualRecovery.episode_profile
#print axioms Generative.Naturalism.ActualRecovery.episodes_profile
#print axioms Generative.Naturalism.ActualRecovery.maintained_profile
#print axioms Generative.Naturalism.ActualRecovery.histories_same_length
#print axioms Generative.Naturalism.ActualRecovery.matched_recovery_unbounded
#print axioms Generative.Naturalism.ActualRecovery.postponed_profile
#print axioms Generative.Naturalism.ActualRecovery.eventual_is_not_actual_recovery
#print axioms Generative.Naturalism.ActualRecovery.interruptions_not_endpoint_determined
