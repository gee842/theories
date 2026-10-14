import Becoming.Countdown
import Becoming.Stock
import PendingTaskApplicability

set_option autoImplicit false

/-!
# The versioned task protocol as an instance of the core's countdown and stock laws (periphery)

`CorrectionVersioned`, `CommonTaskRevision` and `PendingTaskApplicability` use Mathlib's tactics,
so their instances of the pure core's laws are stated here and checked with Lean 4.30.0-rc2
against the pinned Mathlib. The core does not import this module.

* **The head of the queue is counted work.** One tick, with delivered outputs accumulated
  (`tickOut`), runs the queue as `drain` does (`drain_eq`). While the head is pending (same route
  and request, banks and active route unchanged, its remainder still delivering the request,
  nothing more delivered), a tick does one hop of its remaining path, and with none left it
  delivers the request and leaves the rest of the queue (`head_advances`, an instance of
  `Countdown.Advances`). So the head completes after its remaining length plus one tick
  (`head_completes`); `valid_head_completes` is an instance (`valid_head_instance`), and every
  shorter drain leaves the head pending with nothing delivered (`head_pending_before`).
* **Revision of the pending head.** Rewriting the head keeps its route, progress and the rest of
  the queue, so the revised head is pending for the new request with the same remaining work
  (`retarget_pending`); `revised_head_completes` is an instance (`revised_head_instance`).
* **Review and action draw on one stock.** The paid review draws one unit of work and the action
  two, so the course `[1, 2]` is covered exactly from three units (`review_course_covered_iff`,
  `Stock.Covered`). An endpoint completes its review and action exactly when the report clears
  the relevant risk and the work covers that course (`review_completes_iff`); the action itself
  runs exactly from two units (`enact_isSome_iff`).

Declarations may depend on `propext`, `Quot.sound` and `Classical.choice` only, through the
machines' definitions. Correspondence of the protocol to actual requests, authority or reviews
is not checked.
-/

namespace Becoming.VersionedTaskInstances

open Becoming.Countdown CorrectionVersioned CorrectionRelations

/-! ## The head of the queue is counted work -/

/-- One tick, with the delivered outputs accumulated. -/
def tickOut (x : Installation × List (Bool × Bool)) : Option (Installation × List (Bool × Bool)) :=
  some ((tick x.1).1, x.2 ++ (tick x.1).2.toList)

/-- Ticking with accumulated outputs runs the queue as `drain` does. -/
theorem drain_eq : ∀ (n : Nat) (s : Installation) (out : List (Bool × Bool)),
    ticks tickOut n (s, out) = some ((drain n s).1, out ++ (drain n s).2)
  | 0, s, out => by simp [ticks, drain]
  | n + 1, s, out => by
    show ticks tickOut n ((tick s).1, out ++ (tick s).2.toList) = _
    rw [drain_eq n]
    simp [drain, List.append_assoc]

/-- The remaining hops of the head of the queue. -/
def remaining (x : Installation × List (Bool × Bool)) : Nat :=
  match x.1.packets with
  | [] => 0
  | q :: _ => ((x.1.banks q.slot).path.drop q.cursor).length

/-- The head over `ps` is pending: route `slot` and request `requested` kept, banks `B` and
active route `act` unchanged, its remainder still delivering the request, nothing delivered
beyond `out`. -/
def Pending (B : Bool → Bank) (act slot requested : Bool) (ps : List Packet)
    (out : List (Bool × Bool)) (x : Installation × List (Bool × Bool)) : Prop :=
  ∃ q : Packet, x.1.packets = q :: ps ∧ q.slot = slot ∧ q.requested = requested ∧
    x.1.banks = B ∧ x.1.active = act ∧
    Follow ((B slot).path.drop q.cursor) q.payload = requested ∧ x.2 = out

/-- The head has delivered its request and left the rest of the queue as it was. -/
def Delivered (B : Bool → Bank) (act requested : Bool) (ps : List Packet)
    (out : List (Bool × Bool)) (x : Installation × List (Bool × Bool)) : Prop :=
  x.1.packets = ps ∧ x.1.banks = B ∧ x.1.active = act ∧ x.2 = out ++ [(requested, requested)]

/-- The head after one hop. -/
def hop (q : Packet) (bit : Bool) : Packet :=
  {q with cursor := q.cursor + 1, payload := xor q.payload bit}

/-- The installation with another queue. -/
def withQueue (s : Installation) (ps : List Packet) : Installation :=
  {s with packets := ps}

/-- **The head of the queue is counted work**: each tick does one hop of its remaining path,
and with none left it delivers the request. -/
theorem head_advances (B : Bool → Bank) (act slot requested : Bool) (ps : List Packet)
    (out : List (Bool × Bool)) :
    Advances tickOut (Pending B act slot requested ps out) (Delivered B act requested ps out)
      remaining := by
  constructor
  · rintro ⟨s, o⟩ ⟨q, hq, hslot, hreq, hB, hact, hfollow, ho⟩ positive
    simp only at hq hB hact ho
    cases hd : (B slot).path.drop q.cursor with
    | nil =>
      simp [remaining, hq, hB, hslot, hd] at positive
    | cons bit tail =>
      have hd' : (s.banks q.slot).path.drop q.cursor = bit :: tail := by
        rw [hB, hslot]
        exact hd
      refine ⟨(withQueue s (hop q bit :: ps), o), ?_, ?_, ?_⟩
      · simp [tickOut, tick, hq, hd', ho, withQueue, hop]
      · refine ⟨hop q bit, rfl, hslot, hreq, hB, hact, ?_, ho⟩
        rw [hd] at hfollow
        show Follow ((B slot).path.drop (q.cursor + 1)) (xor q.payload bit) = requested
        rw [drop_after_hop _ _ _ _ hd]
        exact hfollow
      · simp [remaining, hq, hB, hslot, hd, drop_after_hop _ _ _ _ hd, withQueue, hop]
  · rintro ⟨s, o⟩ ⟨q, hq, hslot, hreq, hB, hact, hfollow, ho⟩ finished
    simp only at hq hB hact ho
    have hd : (B slot).path.drop q.cursor = [] := by
      simp only [remaining, hq, hB, hslot] at finished
      exact List.eq_nil_of_length_eq_zero finished
    have hd' : (s.banks q.slot).path.drop q.cursor = [] := by
      rw [hB, hslot]
      exact hd
    rw [hd] at hfollow
    have hpay : q.payload = requested := hfollow
    refine ⟨(withQueue s ps, o ++ [(q.requested, q.payload)]), ?_, ?_⟩
    · simp [tickOut, tick, hq, hd', ho, withQueue]
    · exact ⟨rfl, hB, hact, by rw [ho, hreq, hpay]⟩

/-- A head valid under the bank and queue invariant is pending. -/
theorem valid_pending (span : Nat) (s : Installation) (h : CorrectionVersioned.Invariant span s) (p : Packet)
    (ps : List Packet) (hp : s.packets = p :: ps) :
    Pending s.banks s.active p.slot p.requested ps [] (s, []) :=
  ⟨p, hp, rfl, rfl, rfl, rfl, (h.2.2 p (by simp [hp])).2.2, rfl⟩

/-- **Under the invariant, the head completes after its remaining length plus one tick.** -/
theorem head_completes (span : Nat) (s : Installation) (h : CorrectionVersioned.Invariant span s) (p : Packet)
    (ps : List Packet) (hp : s.packets = p :: ps) :
    ∃ t, ticks tickOut (remaining (s, []) + 1) (s, []) = some t ∧
      Delivered s.banks s.active p.requested ps [] t :=
  (head_advances s.banks s.active p.slot p.requested ps []).completes
    (valid_pending span s h p ps hp)

/-- **`valid_head_completes` is an instance.** -/
theorem valid_head_instance (span : Nat) (s : Installation) (h : CorrectionVersioned.Invariant span s) (p : Packet)
    (ps : List Packet) (hp : s.packets = p :: ps) :
    let result := drain (((s.banks p.slot).path.drop p.cursor).length + 1) s
    result.1.packets = ps ∧ result.1.banks = s.banks ∧ result.1.active = s.active ∧
      result.2 = [(p.requested, p.requested)] := by
  obtain ⟨t, ran, delivered⟩ := head_completes span s h p ps hp
  have work : remaining (s, []) = ((s.banks p.slot).path.drop p.cursor).length := by
    simp [remaining, hp]
  rw [work, drain_eq] at ran
  cases ran
  simpa using delivered

/-- **No shorter drain completes the head**: within its remaining hops the head stays pending,
with the remaining work lowered by the ticks taken and nothing delivered. -/
theorem head_pending_before (span : Nat) (s : Installation) (h : CorrectionVersioned.Invariant span s) (p : Packet)
    (ps : List Packet) (hp : s.packets = p :: ps) {k : Nat}
    (within : k ≤ ((s.banks p.slot).path.drop p.cursor).length) :
    ∃ q : Packet, (drain k s).1.packets = q :: ps ∧ q.slot = p.slot ∧ q.requested = p.requested ∧
      (drain k s).2 = [] ∧
      remaining ((drain k s).1, []) + k = ((s.banks p.slot).path.drop p.cursor).length := by
  have work : remaining (s, []) = ((s.banks p.slot).path.drop p.cursor).length := by
    simp [remaining, hp]
  have ran := drain_eq k s []
  obtain ⟨⟨q, hq, hslot, hreq, _, _, _, hout⟩, lowered⟩ :=
    pending_before (head_advances s.banks s.active p.slot p.requested ps []).counts
      (valid_pending span s h p ps hp) (work ▸ within) ran
  simp only [List.nil_append] at hout lowered
  refine ⟨q, hq, hslot, hreq, hout, ?_⟩
  have shape : remaining ((drain k s).1, []) = remaining ((drain k s).1, (drain k s).2) := rfl
  rw [shape, lowered, work]

/-! ## Revision of the pending head -/

/-- **Rewriting the head keeps its route, progress and the rest of the queue**: the revised
head is pending for the new request, with the same remaining work. -/
theorem retarget_pending (span : Nat) (s : Installation) (h : CorrectionVersioned.Invariant span s) (p : Packet)
    (ps : List Packet) (hp : s.packets = p :: ps) (next : Bool) :
    Pending s.banks s.active p.slot next ps [] (CommonTaskRevision.retargetHead s next, []) ∧
      remaining (CommonTaskRevision.retargetHead s next, []) = remaining (s, []) := by
  have valid := CommonTaskRevision.retarget_head_invariant span s h next
  have hp' : (CommonTaskRevision.retargetHead s next).packets =
      CommonTaskRevision.retarget p next :: ps := by
    simp [CommonTaskRevision.retargetHead, hp]
  refine ⟨⟨CommonTaskRevision.retarget p next, hp', rfl, rfl, ?_, ?_, ?_, rfl⟩, ?_⟩
  · simp [CommonTaskRevision.retargetHead, hp]
  · simp [CommonTaskRevision.retargetHead, hp]
  · have pv := (valid.2.2 (CommonTaskRevision.retarget p next) (by simp [hp'])).2.2
    have hb : (CommonTaskRevision.retargetHead s next).banks = s.banks := by
      simp [CommonTaskRevision.retargetHead, hp]
    rw [hb] at pv
    exact pv
  · simp [remaining, hp, CommonTaskRevision.retarget, CommonTaskRevision.retargetHead]

/-- **`revised_head_completes` is an instance.** -/
theorem revised_head_instance (span : Nat) (s : Installation) (h : CorrectionVersioned.Invariant span s) (p : Packet)
    (ps : List Packet) (hp : s.packets = p :: ps) (next : Bool) :
    let result := drain (((s.banks p.slot).path.drop p.cursor).length + 1)
      (CommonTaskRevision.retargetHead s next)
    result.1.packets = ps ∧ result.1.banks = s.banks ∧ result.1.active = s.active ∧
      result.2 = [(next, next)] := by
  obtain ⟨pending, same⟩ := retarget_pending span s h p ps hp next
  obtain ⟨t, ran, delivered⟩ :=
    (head_advances s.banks s.active p.slot next ps []).completes pending
  have work : remaining (s, []) = ((s.banks p.slot).path.drop p.cursor).length := by
    simp [remaining, hp]
  rw [same, work, drain_eq] at ran
  cases ran
  have keep : (CommonTaskRevision.retargetHead s next).banks = s.banks ∧
      (CommonTaskRevision.retargetHead s next).active = s.active := by
    simp [CommonTaskRevision.retargetHead, hp]
  simpa using delivered

/-! ## Review and action draw on one stock -/

/-- **Review draws one unit and action two: the course is covered exactly from three units.** -/
theorem review_course_covered_iff (w : Nat) :
    Stock.Covered (fun n : Nat => n) (fun _ => 0) w [1, 2] ↔ 3 ≤ w := by
  show (1 ≤ w ∧ 2 ≤ w - 1 + 0 ∧ True) ↔ 3 ≤ w
  constructor
  · rintro ⟨_, two, -⟩
    omega
  · intro three
    exact ⟨by omega, by omega, trivial⟩

/-- **The action runs exactly from two units of work.** -/
theorem enact_isSome_iff (c : GoalFormationRevision.Conditions) (l : GoalFormationRevision.State)
    (value : Bool) : (CommonTaskRevision.enact c l value).isSome ↔ 2 ≤ l.account.work := by
  constructor
  · intro some
    by_contra short
    have none : CommonTaskRevision.enact c l value = none := by
      simp [CommonTaskRevision.enact, GoalFormationRevision.operate, GoalFormationRevision.cycle,
        GoalFormationRevision.charge, short]
    simp [none] at some
  · intro work
    obtain ⟨l', h⟩ := PendingTaskApplicability.funded_operation_exists c l value work
    simp [h]

/-- **An endpoint completes its review and action exactly when the report clears the relevant
risk and the work covers the review-and-action course.** -/
theorem review_completes_iff (c : GoalFormationRevision.Conditions) (report : Option Bool)
    (l : GoalFormationRevision.State) (value : Bool) :
    (PendingTaskApplicability.reviewAndAct c report ⟨l, value, true, []⟩).pending = false ↔
      report = some false ∧ Stock.Covered (fun n : Nat => n) (fun _ => 0) l.account.work [1, 2] := by
  rw [review_course_covered_iff]
  unfold PendingTaskApplicability.reviewAndAct
  simp only [Bool.not_true, Bool.false_eq_true, ↓reduceIte]
  cases hc : GoalFormationRevision.charge 1 l.account with
  | none =>
    have short : l.account.work < 1 := by
      by_contra enough
      simp [GoalFormationRevision.charge, show 1 ≤ l.account.work by omega] at hc
    simp only [Bool.true_eq_false, false_iff, not_and]
    intro _
    omega
  | some a =>
    have ha : a.work + 1 = l.account.work := by
      unfold GoalFormationRevision.charge at hc
      split at hc
      · cases hc
        simp only
        omega
      · cases hc
    simp only
    by_cases accepted : report = some false
    · simp only [accepted, ↓reduceIte, true_and]
      cases he : CommonTaskRevision.enact c {l with account := a} value with
      | none =>
        have short := (enact_isSome_iff c {l with account := a} value).not.mp (by simp [he])
        simp only [Bool.true_eq_false, false_iff]
        simp only at short
        omega
      | some l' =>
        have enough := (enact_isSome_iff c {l with account := a} value).mp (by simp [he])
        simp only [true_iff]
        simp only at enough
        omega
    · simp [accepted]

end Becoming.VersionedTaskInstances
