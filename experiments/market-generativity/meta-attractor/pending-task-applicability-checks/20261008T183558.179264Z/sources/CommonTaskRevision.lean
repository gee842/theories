import CorrectionVersioned
import GoalFormationRevision

set_option autoImplicit false

/-!
A scoped composition within one modeled learning/communication/work history.
The head packet represents a pending practice, before its effect is committed.
Revision rewrites its actual encoded remainder, retaining its path, progress and
other queued work. The inherited acquisition and G0/J correspondence are supplied;
this does not derive shared motivation, arbitrary task semantics or authority.
-/
namespace CommonTaskRevision
open CorrectionRelations CorrectionVersioned

/-- This binary encoding applies only to the two inherited practices. -/
def goalBit : GoalFormationRevision.Goal → Bool
  | .attendance => false
  | .learning => true

def bitGoal (b : Bool) : GoalFormationRevision.Goal :=
  if b then .learning else .attendance

/-- Rewrite the pending instruction at its actual current cursor, without
    replacing the path or guessing an unencoded command. Atomic with respect
    to the inherited tick; authority and that physical access are supplied. -/
def retarget (p : Packet) (next : Bool) : Packet :=
  { p with payload := xor (xor p.payload p.requested) next, requested := next }

def retargetHead (s : Installation) (next : Bool) : Installation :=
  match s.packets with
  | [] => s
  | p :: ps => { s with packets := retarget p next :: ps }

theorem retarget_preserves_remaining (path : List Bool) (p : Packet) (next : Bool)
    (h : Follow path p.payload = p.requested) :
    Follow path (retarget p next).payload = next := by
  rw [propagation_parity] at h ⊢
  simp only [retarget]
  cases hp : p.payload <;> cases hr : p.requested <;>
    cases hn : next <;> cases hx : Parity path <;> simp_all

theorem retarget_preserves_route_and_progress (p : Packet) (next : Bool) :
    (retarget p next).slot = p.slot ∧ (retarget p next).cursor = p.cursor :=
  ⟨rfl, rfl⟩

theorem retarget_valid (span : Nat) (s : Installation) (p : Packet) (next : Bool)
    (h : PacketValid span s p) : PacketValid span s (retarget p next) := by
  exact ⟨h.1, h.2.1, retarget_preserves_remaining _ p next h.2.2⟩

theorem retarget_head_invariant (span : Nat) (s : Installation)
    (h : Invariant span s) (next : Bool) : Invariant span (retargetHead s next) := by
  cases hp : s.packets with
  | nil => simpa [retargetHead, hp] using h
  | cons p ps =>
    simp only [retargetHead, hp]
    refine ⟨h.1, h.2.1, ?_⟩
    intro q hq
    simp only [List.mem_cons] at hq
    rcases hq with rfl | hq
    · exact retarget_valid span s p next (h.2.2 p (by simp [hp]))
    · exact h.2.2 q (by simp [hp, hq])

theorem revised_head_completes (span : Nat) (s : Installation)
    (h : Invariant span s) (p : Packet) (ps : List Packet)
    (hp : s.packets = p :: ps) (next : Bool) :
    let result := drain (((s.banks p.slot).path.drop p.cursor).length + 1)
      (retargetHead s next)
    result.1.packets = ps ∧ result.1.banks = s.banks ∧ result.1.active = s.active ∧
      result.2 = [(next, next)] := by
  have r := valid_head_completes span (retargetHead s next)
    (retarget_head_invariant span s h next) (retarget p next) ps
    (by simp [retargetHead, hp])
  simpa [retargetHead, hp, retarget] using r

/-- The inherited learning account pays one unit for an authorized rewrite.
    The communication route's physical maintenance is not charged by this law. -/
def paidRetarget (authorized : Bool) (learning : GoalFormationRevision.State)
    (s : Installation) : Option (GoalFormationRevision.State × Installation) := do
  if !authorized then none else do
    let g ← learning.goal
    if s.packets.isEmpty then none else do
      let account ← GoalFormationRevision.charge 1 learning.account
      pure ({ learning with account }, retargetHead s (goalBit g))

/-- Endpoint actuation uses the bit actually delivered, not the earlier goal
    record. Its archive and loss count retain the inherited history. -/
def enact (c : GoalFormationRevision.Conditions) (learning : GoalFormationRevision.State)
    (value : Bool) : Option GoalFormationRevision.State :=
  GoalFormationRevision.operate c { learning with goal := some (bitGoal value) }

def deliverAndAct (c : GoalFormationRevision.Conditions)
    (learning : GoalFormationRevision.State) (s : Installation) :
    Option GoalFormationRevision.State := do
  let p ← s.packets.head?
  let result := drain (((s.banks p.slot).path.drop p.cursor).length + 1) s
  let output ← result.2.head?
  enact c learning output.2

def continuation (c : GoalFormationRevision.Conditions) (s : Installation) :
    Option GoalFormationRevision.State := do
  let learning ← GoalFormationRevision.completed c
  let adapted ← paidRetarget true learning s
  deliverAndAct c adapted.1 adapted.2

theorem retargeted_act_uses_delivered_revision (span : Nat) (s : Installation)
    (h : Invariant span s) (p : Packet) (ps : List Packet)
    (hp : s.packets = p :: ps) (next : Bool)
    (c : GoalFormationRevision.Conditions) (learning : GoalFormationRevision.State) :
    deliverAndAct c learning (retargetHead s next) = enact c learning next := by
  have r := (revised_head_completes span s h p ps hp next).2.2.2
  unfold deliverAndAct
  simp only [retargetHead, hp, List.head?_cons]
  simpa only [retargetHead, hp, retarget, r, List.head?_cons, Option.bind_some] using
    congrArg (fun outputs : List (Bool × Bool) => outputs.head? >>= fun o => enact c learning o.2) r

/-- A named view of the existing fully acquired, calibrated and reformed history.
    This is a reuse alias, not another formation theorem. -/
def formed : GoalFormationRevision.State :=
  (GoalFormationRevision.completed GoalFormationRevision.harmful).getD
    (GoalFormationRevision.start .attendance)

/-- The previously acquired and calibrated grounds are consumed, and the
    actual output law then protects access and maintenance. Other queued work
    and the pinned route are preserved by revised_head_completes. -/
theorem acquired_revision_changes_pending_action (span : Nat) (s : Installation)
    (h : Invariant span s) (p : Packet) (ps : List Packet)
    (hp : s.packets = p :: ps) :
    (continuation GoalFormationRevision.harmful s).map (fun l =>
      (l.goal, l.losses, l.archive.length, l.account.work, l.account.reserve, l.account.spent)) =
      some (some .learning, 1, 3, 2, 6, 10) := by
  have d := retargeted_act_uses_delivered_revision span s h p ps hp true
    GoalFormationRevision.harmful {formed with account := ⟨2,8,8⟩}
  have hc : GoalFormationRevision.completed GoalFormationRevision.harmful = some formed := by decide
  have prep : paidRetarget true formed s =
      some ({formed with account := ⟨2,8,8⟩}, retargetHead s true) := by
    simp only [paidRetarget, hp, List.isEmpty_cons]
    rfl
  unfold continuation
  rw [hc]
  change ((paidRetarget true formed s >>= fun a =>
    deliverAndAct GoalFormationRevision.harmful a.1 a.2).map _) = _
  rw [prep]
  change ((deliverAndAct GoalFormationRevision.harmful {formed with account := ⟨2,8,8⟩}
    (retargetHead s true)).map _) = _
  rw [d]
  decide

theorem warranted_revision_and_pending_delivery (span : Nat) (s : Installation)
    (h : Invariant span s) (p : Packet) (ps : List Packet)
    (hp : s.packets = p :: ps) :
    PracticalJudgment.Better
      (GoalFormationRevision.protects GoalFormationRevision.harmful)
      (GoalFormationRevision.gains GoalFormationRevision.harmful) .learning .attendance ∧
    (continuation GoalFormationRevision.harmful s).map (fun l =>
      (l.goal, l.losses, l.archive.length, l.account.work, l.account.reserve, l.account.spent)) =
      some (some .learning, 1, 3, 2, 6, 10) :=
  ⟨GoalFormationRevision.joined_revision_has_warrant_and_actual_continuation.1,
   acquired_revision_changes_pending_action span s h p ps hp⟩

/-- Work and dependence are not invented by retargeting. The existing account
    conservation lemma is consumed; accumulated outcomes are unchanged. -/
theorem paid_retarget_keeps_history (authorized : Bool)
    (l l' : GoalFormationRevision.State) (s s' : Installation)
    (h : paidRetarget authorized l s = some (l', s')) :
    l'.archive = l.archive ∧ l'.losses = l.losses ∧
      GoalFormationRevision.total l'.account = GoalFormationRevision.total l.account := by
  unfold paidRetarget at h
  split at h
  · simp at h
  · cases hg : l.goal with
    | none => simp [hg] at h
    | some g =>
      simp only [hg] at h
      split at h
      · simp at h
      · cases hc : GoalFormationRevision.charge 1 l.account with
        | none => simp [hc] at h
        | some a =>
          simp only [hc] at h
          rcases h with ⟨rfl, rfl⟩
          exact ⟨rfl, rfl, GoalFormationRevision.charge_conserves hc⟩

/-- A concrete already-started task: its first hop has happened. -/
def pending : Installation :=
  (tick (beginRequest 2 (initial [true, true]) false)).1

theorem pending_is_valid : Invariant 2 pending :=
  (tick_preserves_and_output 2 _
    (begin_preserves 2 2 _ (initial_invariant [true, true]) false)).1

theorem old_route_faithfully_executes_outdated_task :
    (drain 2 pending).2 = [(false, false)] ∧
    (GoalFormationRevision.completed GoalFormationRevision.harmful >>= fun l =>
      deliverAndAct GoalFormationRevision.harmful l pending).map
      (fun l => (l.goal, l.losses)) = some (some .attendance, 2) := by decide

theorem declaration_only_fails :
    let p : Packet := ⟨false, 1, true, false⟩
    Follow [true] ({ p with requested := true }).payload ≠ true := by decide

theorem unencoded_replacement_fails : Follow [true] true ≠ true := by decide

theorem no_authority_blocks_rewrite (l : GoalFormationRevision.State) (s : Installation) :
    paidRetarget false l s = none := by simp [paidRetarget]

theorem insufficient_rewrite_support :
    (GoalFormationRevision.completed GoalFormationRevision.harmful >>= fun l =>
      paidRetarget true {l with account := ⟨0, 8, 10⟩} pending) = none := by decide

theorem stale_conditions_defeat_the_new_practice :
    (GoalFormationRevision.completed GoalFormationRevision.harmful >>= fun l =>
      let adapted := paidRetarget true l pending
      adapted >>= fun a => deliverAndAct GoalFormationRevision.conflict a.1 a.2).map
      (fun l => l.losses) = some 2 := by decide

/-- Neither new goals nor network correctness undo an already committed loss. -/
theorem correction_retains_past_loss :
    (continuation GoalFormationRevision.harmful pending).map
      (fun l => (l.losses, l.archive.length)) = some (1, 3) := by decide

end CommonTaskRevision
