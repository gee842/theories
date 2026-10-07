import ContactFormation

/-!
Whole-process reachability and an actually formed condition are different
descriptions of the same history. A future target that is reachable after a
prefix was already reachable through that prefix. This does not say that its
present organization already existed, or that its formation requires import.

The concrete witness reuses the actual, resource-guarded contact formation.
It does not introduce another dynamics, certify unbounded renewal, or identify
an operational distinction with ethical worth. NativeReachOpen includes the
empty trace: it describes reachability of an open contact, not funded delivery.
-/

namespace Generative.InquirySufficiency.GenerativePossibility

open Generative

universe u v

def CanReach {S : Type u} {A : Type v} (P : Process S A)
    (target : S → Prop) (s : S) : Prop :=
  ∃ commands t, Trace P s commands t ∧ target t

theorem actual_is_reachable {S : Type u} {A : Type v}
    (P : Process S A) (target : S → Prop) (s : S) (actual : target s) :
    CanReach P target s :=
  ⟨[], s, .nil s, actual⟩

theorem reachable_before {S : Type u} {A : Type v}
    {P : Process S A} {target : S → Prop} {s t : S} {earlierCommands : List A}
    (history : Trace P s earlierCommands t) (later : CanReach P target t) :
    CanReach P target s := by
  obtain ⟨suffix, last, continuation, achieved⟩ := later
  exact ⟨earlierCommands ++ suffix, last,
    trace_append_iff.mpr ⟨t, history, continuation⟩, achieved⟩

theorem unreachable_stays_unreachable {S : Type u} {A : Type v}
    {P : Process S A} {target : S → Prop} {s t : S} {earlierCommands : List A}
    (history : Trace P s earlierCommands t) (unreachable : ¬ CanReach P target s) :
    ¬ CanReach P target t :=
  fun later => unreachable (reachable_before history later)

def NativeReachOpen (x : ContactFormation.Formed) : Prop :=
  ∃ commands t, Trace NativePacketProcess.process x.port commands t ∧
    t.blocked = false

theorem native_reach_open_iff (x : ContactFormation.Formed) :
    NativeReachOpen x ↔ x.port.blocked = false := by
  constructor
  · rintro ⟨commands, last, history, opened⟩
    exact (ContactFormation.native_trace_retains_contact history).1.symm.trans opened
  · intro opened
    exact ⟨[], x.port, .nil x.port, opened⟩

theorem actual_formation_creates_open_condition (x : ContactFormation.Formed)
    (blocked : x.port.blocked = true)
    (funded : NativePacketProcess.Supportable x.port) (pair : 1 ≤ x.spare) :
    ∃ y, ContactFormation.process.step x .form y ∧
      ¬ NativeReachOpen x ∧ NativeReachOpen y ∧
      CanReach ContactFormation.process (fun z => z.port.blocked = false) x ∧
      CanReach ContactFormation.process (fun z => z.port.blocked = false) y := by
  let y := ContactFormation.formedState x
  have formed : ContactFormation.process.step x .form y :=
    ContactFormation.form_complete x funded pair
  have opened : y.port.blocked = false := rfl
  have later := actual_is_reachable ContactFormation.process
    (fun z => z.port.blocked = false) y opened
  refine ⟨y, formed, ?_, (native_reach_open_iff y).mpr opened,
    reachable_before (.cons formed (.nil y)) later, later⟩
  intro earlier
  have impossible := (native_reach_open_iff x).mp earlier
  rw [blocked] at impossible
  cases impossible

end Generative.InquirySufficiency.GenerativePossibility

#print axioms Generative.InquirySufficiency.GenerativePossibility.CanReach
#print axioms Generative.InquirySufficiency.GenerativePossibility.actual_is_reachable
#print axioms Generative.InquirySufficiency.GenerativePossibility.reachable_before
#print axioms Generative.InquirySufficiency.GenerativePossibility.unreachable_stays_unreachable
#print axioms Generative.InquirySufficiency.GenerativePossibility.NativeReachOpen
#print axioms Generative.InquirySufficiency.GenerativePossibility.native_reach_open_iff
#print axioms Generative.InquirySufficiency.GenerativePossibility.actual_formation_creates_open_condition
