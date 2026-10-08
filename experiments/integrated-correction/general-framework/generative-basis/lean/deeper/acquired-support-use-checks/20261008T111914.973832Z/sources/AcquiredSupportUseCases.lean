import AcquiredSupportUse

/-! Native interference, selective validation and exact paid retry histories.
The retry bound is for this specified word with a final quiet read/use pair;
it is not a fairness theorem or a bound on arbitrary physical concurrency. -/
namespace Generative.AcquiredSupportUseCases
open ReconfigurableSupportLogic AcquiredSupportUse

def allSlots {R : Type} (_ : R) : Prop := True

def idle (revision fuel : Nat) : Session Unit :=
  ⟨⟨⟨(), fun _ => false⟩, fun _ => revision⟩, none, fuel⟩

def cycle : List (Action Unit) := [.read, .change .take, .change (.release ()), .reject]

def cycleEnd (s : Session Unit) : Session Unit :=
  next (next (next (next s .read) (.change .take)) (.change (.release ()))) .reject

theorem cycle_end (revision fuel : Nat) :
    cycleEnd (idle revision fuel) = idle (revision + 2) (fuel - 1) := by
  simp [cycleEnd, idle, next, update, after, setBusy, bump, Nat.add_assoc]

theorem cycle_trace (revision fuel : Nat) :
    Trace (execution allSlots) (idle revision (fuel + 1)) cycle (idle (revision + 2) fuel) := by
  have trace : Trace (execution allSlots) (idle revision (fuel + 1)) cycle
      (cycleEnd (idle revision (fuel + 1))) := by
    refine .cons ⟨⟨True.intro, by simp [idle]⟩, rfl⟩
      (.cons ⟨⟨True.intro, rfl⟩, rfl⟩
        (.cons ⟨⟨True.intro, rfl⟩, rfl⟩ (.cons ?_ (.nil _))))
    refine ⟨⟨sample (idle revision (fuel + 1)).world, rfl, ?_⟩, rfl⟩
    intro ad
    have eq := ad.2.1
    change revision = revision + 1 + 1 at eq
    omega
  simpa [cycle_end] using trace

def retries : Nat → List (Action Unit)
  | 0 => []
  | n + 1 => cycle ++ retries n

theorem totalCharge_append {R : Type} (xs ys : List (Action R)) :
    totalCharge (xs ++ ys) = totalCharge xs + totalCharge ys := by
  induction xs with
  | nil => rfl
  | cons a xs ih => simp [totalCharge, ih, Nat.add_assoc]

theorem retries_charge (n : Nat) : totalCharge (retries n) = n := by
  induction n with
  | zero => rfl
  | succ n ih => simp [retries, totalCharge_append, cycle, totalCharge, charge, ih, Nat.add_comm]

theorem retries_trace (n revision fuel : Nat) :
    Trace (execution allSlots) (idle revision (n + fuel)) (retries n)
      (idle (revision + 2 * n) fuel) := by
  induction n generalizing revision with
  | zero => simpa [retries] using (Trace.nil (idle revision fuel) :
      Trace (execution allSlots) _ [] _)
  | succ n ih =>
    have first := cycle_trace revision (n + fuel)
    have rest := ih (revision + 2)
    have both := trace_append_iff.mpr ⟨_, first, rest⟩
    simpa [retries, Nat.mul_add, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using both

theorem retries_then_use_iff (n revision fuel : Nat) :
    Feasible (execution allSlots) (idle revision fuel) (retries n ++ [.read, .use]) ↔
      n + 2 ≤ fuel := by
  constructor
  · intro h
    have needed := budget_necessary h
    simpa [totalCharge_append, retries_charge, totalCharge, charge] using needed
  · intro enough
    have first := retries_trace n revision (fuel - n)
    have start : n + (fuel - n) = fuel := by omega
    rw [start] at first
    have last := fresh_read_use (idle (revision + 2 * n) (fuel - n)) True.intro rfl (by
      change 2 ≤ fuel - n; omega)
    exact ⟨_, trace_append_iff.mpr ⟨_, first, last⟩⟩

theorem finite_budget_can_be_exhausted (n : Nat) :
    Trace (execution allSlots) (idle 0 n) (retries n) (idle (2 * n) 0) ∧
      ¬ Enabled (execution allSlots) (idle (2 * n) 0) .read ∧
      ¬ Enabled (execution allSlots) (idle (2 * n) 0) .use := by
  refine ⟨by simpa using retries_trace n 0 0, ?_, ?_⟩
  · rintro ⟨t, en, _⟩
    exact Nat.not_lt_zero _ en.2
  · rintro ⟨t, en, _⟩
    exact Nat.not_lt_zero _ en.2.1

def readOnly := next (idle 0 2) .read
def occupied := next readOnly (.change .take)
def restored := next occupied (.change (.release ()))

theorem acquired_ticket_initially_usable :
    Sound readOnly ∧ Enabled (execution allSlots) readOnly .use := by
  constructor
  · apply next_sound
    intro t ht; cases ht
  · exact ⟨next readOnly .use, ⟨True.intro, by decide, sample (idle 0 2).world,
      rfl, rfl, rfl, rfl⟩, rfl⟩

theorem stale_read_rejected : Sound occupied ∧ ¬ Enabled (execution allSlots) occupied .use := by
  constructor
  · exact next_sound acquired_ticket_initially_usable.1 _
  · rintro ⟨last, _, _, t, stored, ad, _⟩
    have eq : sample (idle 0 2).world = t := Option.some.inj stored
    subst t
    exact intervening_take_rejects (idle 0 2) ad

theorem restored_value_still_rejected :
    restored.world.physical.busy () = false ∧
      ¬ Enabled (execution allSlots) restored .use := by
  constructor
  · rfl
  · rintro ⟨last, _, _, t, stored, ad, _⟩
    have eq : sample (idle 0 2).world = t := Option.some.inj stored
    subst t
    have impossible : (0 : Nat) = 2 := ad.2.1
    cases impossible

def twoSlots : Session Bool :=
  ⟨⟨⟨false, fun r => r⟩, fun _ => 0⟩, none, 2⟩

theorem unrelated_change_then_use :
    Trace (execution allSlots) twoSlots [.read, .change (.release true), .use]
      (next (next (next twoSlots .read) (.change (.release true))) .use) := by
  refine .cons ⟨⟨True.intro, by decide⟩, rfl⟩
    (.cons ⟨⟨True.intro, rfl⟩, rfl⟩ (.cons ?_ (.nil _)))
  exact ⟨⟨True.intro, by decide, sample twoSlots.world, rfl, rfl, rfl, rfl⟩, rfl⟩

theorem wrong_route_rejected :
    ¬ Enabled (execution allSlots) (next (next twoSlots .read) (.change (.redirect true))) .use := by
  rintro ⟨last, _, _, t, stored, ad, _⟩
  have eq : sample twoSlots.world = t := Option.some.inj stored
  subst t
  have bad : (false : Bool) = true := ad.1
  cases bad

/-- A writer bypassing revision tracking is outside the admitted law. -/
def bypass : Session Unit :=
  { readOnly with world := ⟨⟨(), fun _ => true⟩, readOnly.world.revision⟩ }

theorem bypass_breaks_correspondence :
    permitted allSlots bypass .use ∧ ¬ Sound bypass ∧
      ¬ Enabled (process allSlots) bypass.world.physical .take := by
  refine ⟨⟨True.intro, by decide, sample (idle 0 2).world, rfl, rfl, rfl, rfl⟩, ?_, ?_⟩
  · intro h
    have valid := h (sample (idle 0 2).world) rfl
    have bad : (false : Bool) = true := valid.2 rfl
    cases bad
  · rintro ⟨t, en, _⟩
    have bad : (true : Bool) = false := en.2
    cases bad

end Generative.AcquiredSupportUseCases

#print axioms Generative.AcquiredSupportUseCases.cycle_end
#print axioms Generative.AcquiredSupportUseCases.cycle_trace
#print axioms Generative.AcquiredSupportUseCases.totalCharge_append
#print axioms Generative.AcquiredSupportUseCases.retries_charge
#print axioms Generative.AcquiredSupportUseCases.retries_trace
#print axioms Generative.AcquiredSupportUseCases.retries_then_use_iff
#print axioms Generative.AcquiredSupportUseCases.finite_budget_can_be_exhausted
#print axioms Generative.AcquiredSupportUseCases.acquired_ticket_initially_usable
#print axioms Generative.AcquiredSupportUseCases.stale_read_rejected
#print axioms Generative.AcquiredSupportUseCases.restored_value_still_rejected
#print axioms Generative.AcquiredSupportUseCases.unrelated_change_then_use
#print axioms Generative.AcquiredSupportUseCases.wrong_route_rejected
#print axioms Generative.AcquiredSupportUseCases.bypass_breaks_correspondence
