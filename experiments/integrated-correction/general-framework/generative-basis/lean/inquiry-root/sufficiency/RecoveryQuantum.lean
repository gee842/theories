import FormationClosure

/-!
# The recovery rate is the dissipation of one failed conversion

Study note: _process/research/2026-10-05-generative-foundation-review/root-foundation/
RECOVERY-QUANTUM.md.

`FormationClosure` recovers one spare pair from ten dissipated units and lists
that rate of ten as supplied. This module asks whether the rate follows from the
activity it recovers from.

1. **The quantum is native.** Every conversion in the native probe settles
   exactly ten units: it lowers the source coordinate by ten and raises either
   the arrived record or the dissipated record by ten, never both
   (`conversion_settles_quantum`). A failed conversion dissipates exactly ten
   (`failed_conversion_dissipates_quantum`). Every completed native command
   raises the dissipated record by ten when it is a failed conversion and by
   zero otherwise (`native_dissipation_step`). So the dissipated record of a
   history that started from zero is ten times its count of failed conversions
   (`failure_record_step`, `trace_failure_record`).
2. **The rate is fixed by one-pair-per-failure.** Recovery is stated for any
   rate `r` (`recoverAt`; `recoverAt_ten` shows the supplied model is `r = 10`).
   Two requirements are put on it: each recovered pair is backed by a distinct
   failed conversion recorded in the same activity (`PairsBackedAt`), and each
   recorded failed conversion not yet recovered can be recovered
   (`EachFailureRecoverableAt`). Together they hold exactly when `r = 10`
   (`rate_determined`). The rate is the dissipation quantum of the activity,
   not a free number.
3. **Executed countercases.** With the nearest coarser rate eleven, the one
   failed conversion of the closure history cannot be recovered and that
   history does not complete (`coarser_rate_strands_failure`). With the nearest
   finer rate nine, nine failed conversions yield ten pairs
   (`finer_rate_overcounts`).

Scope. The requirement that one pair corresponds to one failed conversion is
the claim under which the rate is determined; it is not derived here from the
native port. Without that requirement any rate is consistent with the port and
the countercases show what each other rate changes. The value ten of the
native conversion is inherited from the port and is not derived here.
-/

namespace Generative.InquirySufficiency.RecoveryQuantum

open Generative NativePacketProcess PacketLawDerivation FormationClosure
open FormationLaw

/-! ## 1. The dissipation quantum of the native activity -/

theorem conversion_settles_quantum (s : NativePacketProcess.State) :
    (convert s).source = s.source - 10 ∧
      (convert s).transferred + (convert s).wasted = s.transferred + s.wasted + 10 := by
  refine ⟨rfl, ?_⟩
  change s.transferred + (if arrival s then 10 else 0) +
      (s.wasted + (if arrival s then 0 else 10)) = s.transferred + s.wasted + 10
  cases arrival s
  · change s.transferred + 0 + (s.wasted + 10) = s.transferred + s.wasted + 10
    rw [Nat.add_zero, Nat.add_assoc]
  · change s.transferred + 10 + s.wasted = s.transferred + s.wasted + 10
    exact Nat.add_right_comm _ _ _

theorem failed_conversion_dissipates_quantum (s : NativePacketProcess.State)
    (failed : arrival s = false) :
    (convert s).wasted = s.wasted + 10 ∧ (convert s).transferred = s.transferred := by
  refine ⟨?_, ?_⟩
  · change s.wasted + (if arrival s then 0 else 10) = s.wasted + 10
    rw [failed]
    rfl
  · change s.transferred + (if arrival s then 10 else 0) = s.transferred
    rw [failed]
    rfl

/-- A completed native command is a failed conversion when it is a probe
that does not arrive. -/
def failedConversion (command : NativePacketProcess.Command) (s : NativePacketProcess.State) :
    Bool :=
  match command with
  | .probe => !arrival s
  | .a => false
  | .reset => false
  | .read => false

def dissipated (failed : Bool) : Nat := if failed then 10 else 0

theorem native_dissipation_step {s t : NativePacketProcess.State}
    {command : NativePacketProcess.Command} {o : Observation}
    (actual : execute s command = .complete t o) :
    t.wasted = s.wasted + dissipated (failedConversion command s) := by
  cases command with
  | probe =>
    obtain ⟨_, rfl, _⟩ := (probe_complete_iff s t o).mp actual
    rw [(probe_final_effects s).2.2.2.2.2.2]
    change s.wasted + (if arrival s then 0 else 10) = s.wasted + (if (!arrival s) then 10 else 0)
    cases arrival s <;> rfl
  | a =>
    unfold execute at actual
    generalize interface : charge s = payment at actual
    cases payment with
    | capacity => cases actual
    | funding => cases actual
    | paid ready =>
      obtain ⟨_, rfl⟩ := (charge_paid_iff s ready).mp interface
      cases actual
      rfl
  | reset =>
    unfold execute at actual
    generalize interface : charge s = payment at actual
    cases payment with
    | capacity => cases actual
    | funding => cases actual
    | paid ready =>
      obtain ⟨_, rfl⟩ := (charge_paid_iff s ready).mp interface
      cases actual
      rfl
  | read =>
    unfold execute at actual
    generalize interface : charge s = payment at actual
    cases payment with
    | capacity => cases actual
    | funding => cases actual
    | paid ready =>
      obtain ⟨_, rfl⟩ := (charge_paid_iff s ready).mp interface
      cases actual
      rfl

/-- The dissipated record shows `count` failed conversions. -/
def FailureRecord (s : NativePacketProcess.State) (count : Nat) : Prop :=
  s.wasted = 10 * count

def countStep (failed : Bool) : Nat := if failed then 1 else 0

theorem failure_record_step {s t : NativePacketProcess.State}
    {command : NativePacketProcess.Command} {o : Observation} {count : Nat}
    (actual : execute s command = .complete t o) (record : FailureRecord s count) :
    FailureRecord t (count + countStep (failedConversion command s)) := by
  unfold FailureRecord
  rw [native_dissipation_step actual, record, Nat.mul_add]
  cases failedConversion command s <;> rfl

/-- Along every history of the closure process the dissipated record stays a
whole number of failed conversions, and recovered pairs never exceed it. -/
theorem trace_failure_record {x y : Port} {events : List FormationClosure.Event} {count : Nat}
    (trace : Trace FormationClosure.process x events y)
    (record : FailureRecord x.native count) (backed : x.recovered ≤ count) :
    ∃ later, count ≤ later ∧ FailureRecord y.native later ∧ y.recovered ≤ later := by
  induction trace generalizing count with
  | nil => exact ⟨count, Nat.le_refl _, record, backed⟩
  | @cons s m t event rest step _ ih =>
    cases event with
    | inl e =>
      cases e with
      | inl command =>
        obtain ⟨⟨o, actual⟩, _, kept⟩ := step
        have next := failure_record_step actual record
        obtain ⟨later, grew, final, bound⟩ :=
          ih next (by rw [kept]; exact Nat.le_trans backed (Nat.le_add_right _ _))
        exact ⟨later, Nat.le_trans (Nat.le_add_right _ _) grew, final, bound⟩
      | inr _ =>
        obtain ⟨_, enough, rfl⟩ := (recover_complete_iff s m).mp step
        have counted : s.recovered + 1 ≤ count := by
          have h : 10 * (s.recovered + 1) ≤ 10 * count := by
            rw [← record]; exact enough
          exact Nat.le_of_mul_le_mul_left h (by decide)
        exact ih record counted
    | inr _ =>
      obtain ⟨_, _, rfl⟩ := (formPort_complete_iff s m).mp step
      exact ih record backed

/-! ## 2. Recovery at any rate, and the rate the activity fixes -/

def finishRecoveryAt (rate : Nat) (x : Port) (ready : NativePacketProcess.State) : Outcome :=
  if rate * (x.recovered + 1) ≤ ready.wasted then
    .complete ⟨ready, x.spare + 1, x.recovered + 1⟩
  else .stopped ⟨ready, x.spare, x.recovered⟩

/-- `FormationClosure.recover` with its rate left open. -/
def recoverAt (rate : Nat) (x : Port) : Outcome :=
  match charge x.native with
  | .capacity => .stopped x
  | .funding => .stopped x
  | .paid ready => finishRecoveryAt rate x ready

theorem recoverAt_ten : recoverAt 10 = recover := rfl

theorem recoverAt_complete_iff (rate : Nat) (x y : Port) :
    recoverAt rate x = .complete y ↔
      Payable x.native ∧ rate * (x.recovered + 1) ≤ x.native.wasted ∧
        y = ⟨debit x.native, x.spare + 1, x.recovered + 1⟩ := by
  constructor
  · intro completed
    unfold recoverAt at completed
    generalize interface : charge x.native = payment at completed
    cases payment with
    | capacity => cases completed
    | funding => cases completed
    | paid ready =>
      obtain ⟨sustained, equality⟩ := (charge_paid_iff x.native ready).mp interface
      cases equality
      dsimp only at completed
      unfold finishRecoveryAt at completed
      by_cases backed : rate * (x.recovered + 1) ≤ (debit x.native).wasted
      · rw [if_pos backed] at completed
        cases completed
        exact ⟨sustained, backed, rfl⟩
      · rw [if_neg backed] at completed
        cases completed
  · rintro ⟨sustained, backed, rfl⟩
    unfold recoverAt
    rw [charge_paid x.native sustained.1 sustained.2]
    dsimp only
    unfold finishRecoveryAt
    rw [if_pos (show rate * (x.recovered + 1) ≤ (debit x.native).wasted from backed)]

/-- Each recovered pair is backed by a distinct recorded failed conversion. -/
def PairsBackedAt (rate : Nat) : Prop :=
  ∀ (x y : Port) (count : Nat), FailureRecord x.native count →
    recoverAt rate x = .complete y → y.recovered ≤ count

/-- Each recorded failed conversion not yet recovered can be recovered when
the interface draw is met. -/
def EachFailureRecoverableAt (rate : Nat) : Prop :=
  ∀ (x : Port) (count : Nat), Payable x.native → FailureRecord x.native count →
    x.recovered + 1 ≤ count → ∃ y, recoverAt rate x = .complete y

/-- A port state used only to test the two requirements. -/
def witness (dissipatedUnits recoveredPairs : Nat) : Port :=
  ⟨{ phase := .p0, tau := false, sigma := false, broken := false, blocked := true,
     receiptFlip := false, source := 0, fuel := 100000, live := 0, workspace := 0,
     capacity := 10, spent := 0, income := 0, transferred := 0,
     wasted := dissipatedUnits }, 0, recoveredPairs⟩

theorem witness_sustainable (d r : Nat) : Payable (witness d r).native :=
  ⟨show 2 ≤ 10 by decide, show 16386 ≤ 100000 by decide⟩

theorem ten_backs_pairs : PairsBackedAt 10 := by
  intro x y count record completed
  obtain ⟨_, enough, rfl⟩ := (recoverAt_complete_iff 10 x y).mp completed
  have h : 10 * (x.recovered + 1) ≤ 10 * count := by
    rw [← record]; exact enough
  exact Nat.le_of_mul_le_mul_left h (by decide)

theorem ten_recovers_each_failure : EachFailureRecoverableAt 10 := by
  intro x count sustained record room
  refine ⟨_, (recoverAt_complete_iff 10 x _).mpr ⟨sustained, ?_, rfl⟩⟩
  rw [record]
  exact Nat.mul_le_mul_left 10 room

theorem recoverable_rate_at_most_ten {rate : Nat} (each : EachFailureRecoverableAt rate) :
    rate ≤ 10 := by
  obtain ⟨y, completed⟩ := each (witness 10 0) 1 (witness_sustainable 10 0) rfl (Nat.le_refl 1)
  obtain ⟨_, enough, _⟩ := (recoverAt_complete_iff rate _ y).mp completed
  change rate * 1 ≤ 10 at enough
  rw [Nat.mul_one] at enough
  exact enough

theorem backed_rate_at_least_ten {rate : Nat} (backed : PairsBackedAt rate) : 10 ≤ rate := by
  cases Nat.lt_or_ge rate 10 with
  | inr enough => exact enough
  | inl finer =>
    exfalso
    have fits : rate * (rate + 1) ≤ (witness (10 * rate) rate).native.wasted := by
      change rate * (rate + 1) ≤ 10 * rate
      rw [Nat.mul_comm 10 rate]
      exact Nat.mul_le_mul_left rate finer
    have completed := (recoverAt_complete_iff rate (witness (10 * rate) rate) _).mpr
      ⟨witness_sustainable _ _, fits, rfl⟩
    have bound := backed (witness (10 * rate) rate) _ rate rfl completed
    exact Nat.not_succ_le_self rate bound

/-- The recovery rate is determined: one pair per failed conversion holds
exactly at the dissipation quantum of the native conversion. -/
theorem rate_determined (rate : Nat) :
    (PairsBackedAt rate ∧ EachFailureRecoverableAt rate) ↔ rate = 10 := by
  constructor
  · intro both
    exact Nat.le_antisymm (recoverable_rate_at_most_ten both.2) (backed_rate_at_least_ten both.1)
  · intro equal
    subst equal
    exact ⟨ten_backs_pairs, ten_recovers_each_failure⟩

/-! ## 3. Executed countercases at the neighbouring rates -/

def runEventAt (rate : Nat) (x : Port) : FormationClosure.Event → Option Port
  | .inl (.inl command) => completeNative x (execute x.native command)
  | .inl (.inr _) => completeOutcome (recoverAt rate x)
  | .inr _ => completeOutcome (formPort x)

def runAt (rate : Nat) (x : Port) : List FormationClosure.Event → Option Port
  | [] => some x
  | event :: rest => match runEventAt rate x event with
    | some y => runAt rate y rest
    | none => none

theorem runEventAt_ten (x : Port) (event : FormationClosure.Event) :
    runEventAt 10 x event = runEvent x event := by
  cases event with
  | inl e => cases e <;> rfl
  | inr _ => rfl

theorem runAt_ten (x : Port) (events : List FormationClosure.Event) :
    runAt 10 x events = run x events := by
  induction events generalizing x with
  | nil => rfl
  | cons event rest ih =>
    unfold runAt run
    rw [runEventAt_ten]
    cases runEvent x event with
    | none => rfl
    | some y => exact ih y

/-- At rate eleven the one failed conversion of the closure history cannot be
recovered, and the history that opens the contact at rate ten stops. -/
theorem coarser_rate_strands_failure :
    (∃ y, runAt 10 start history = some y ∧ y.recovered = 1) ∧
      runAt 11 start history = none ∧
      (∃ m, runAt 11 start [nativeE .a, nativeE .a, nativeE .probe] = some m ∧
        FailureRecord m.native 1 ∧ m.recovered = 0 ∧ Payable m.native ∧
        ∀ y, recoverAt 11 m ≠ .complete y) := by
  refine ⟨⟨_, rfl, rfl⟩, rfl, ⟨_, rfl, rfl, rfl, ⟨by decide, by decide⟩, ?_⟩⟩
  intro y completed
  have enough := ((recoverAt_complete_iff 11 _ y).mp completed).2.1
  exact absurd enough (by decide)

/-- A blocked port with enough held amount for nine failed conversions. -/
def nineFailuresStart : Port :=
  ⟨{ phase := .p0, tau := false, sigma := false, broken := false, blocked := true,
     receiptFlip := false, source := 90, fuel := 1000000, live := 0, workspace := 0,
     capacity := 10, spent := 0, income := 0, transferred := 0, wasted := 0 }, 0, 0⟩

def nineFailuresThenTenRecoveries : List FormationClosure.Event :=
  List.replicate 9 (nativeE .probe) ++ List.replicate 10 recoverE

/-- At rate nine, nine recorded failed conversions yield ten pairs; the same
history stops at rate ten. -/
theorem finer_rate_overcounts :
    (∃ y, runAt 9 nineFailuresStart nineFailuresThenTenRecoveries = some y ∧
      FailureRecord y.native 9 ∧ y.recovered = 10 ∧ y.spare = 10) ∧
      runAt 10 nineFailuresStart nineFailuresThenTenRecoveries = none :=
  ⟨⟨_, rfl, rfl, rfl, rfl⟩, rfl⟩

end Generative.InquirySufficiency.RecoveryQuantum

#print axioms Generative.InquirySufficiency.RecoveryQuantum.conversion_settles_quantum
#print axioms Generative.InquirySufficiency.RecoveryQuantum.failed_conversion_dissipates_quantum
#print axioms Generative.InquirySufficiency.RecoveryQuantum.failedConversion
#print axioms Generative.InquirySufficiency.RecoveryQuantum.dissipated
#print axioms Generative.InquirySufficiency.RecoveryQuantum.native_dissipation_step
#print axioms Generative.InquirySufficiency.RecoveryQuantum.FailureRecord
#print axioms Generative.InquirySufficiency.RecoveryQuantum.countStep
#print axioms Generative.InquirySufficiency.RecoveryQuantum.failure_record_step
#print axioms Generative.InquirySufficiency.RecoveryQuantum.trace_failure_record
#print axioms Generative.InquirySufficiency.RecoveryQuantum.finishRecoveryAt
#print axioms Generative.InquirySufficiency.RecoveryQuantum.recoverAt
#print axioms Generative.InquirySufficiency.RecoveryQuantum.recoverAt_ten
#print axioms Generative.InquirySufficiency.RecoveryQuantum.recoverAt_complete_iff
#print axioms Generative.InquirySufficiency.RecoveryQuantum.PairsBackedAt
#print axioms Generative.InquirySufficiency.RecoveryQuantum.EachFailureRecoverableAt
#print axioms Generative.InquirySufficiency.RecoveryQuantum.witness
#print axioms Generative.InquirySufficiency.RecoveryQuantum.witness_sustainable
#print axioms Generative.InquirySufficiency.RecoveryQuantum.ten_backs_pairs
#print axioms Generative.InquirySufficiency.RecoveryQuantum.ten_recovers_each_failure
#print axioms Generative.InquirySufficiency.RecoveryQuantum.recoverable_rate_at_most_ten
#print axioms Generative.InquirySufficiency.RecoveryQuantum.backed_rate_at_least_ten
#print axioms Generative.InquirySufficiency.RecoveryQuantum.rate_determined
#print axioms Generative.InquirySufficiency.RecoveryQuantum.runEventAt
#print axioms Generative.InquirySufficiency.RecoveryQuantum.runAt
#print axioms Generative.InquirySufficiency.RecoveryQuantum.runEventAt_ten
#print axioms Generative.InquirySufficiency.RecoveryQuantum.runAt_ten
#print axioms Generative.InquirySufficiency.RecoveryQuantum.coarser_rate_strands_failure
#print axioms Generative.InquirySufficiency.RecoveryQuantum.nineFailuresStart
#print axioms Generative.InquirySufficiency.RecoveryQuantum.nineFailuresThenTenRecoveries
#print axioms Generative.InquirySufficiency.RecoveryQuantum.finer_rate_overcounts
