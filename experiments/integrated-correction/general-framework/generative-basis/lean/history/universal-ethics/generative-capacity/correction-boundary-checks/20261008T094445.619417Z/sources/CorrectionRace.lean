import Mathlib.Tactic

/- A local refinement of the test/use interval. Snapshot and reservation are
atomic primitives. All modeled changes honor the reservation. Physical faults,
compromised monitors and request authentication are outside the transition law. -/
namespace CorrectionRace

structure Device where
  epoch : Nat
  polarity : Bool
  locked : Bool
  deriving DecidableEq, Repr

structure Ticket where
  epoch : Nat
  polarity : Bool
  requested : Bool
  deriving DecidableEq, Repr

def sample (d : Device) (requested : Bool) : Ticket :=
  ⟨d.epoch, xor false d.polarity, requested⟩

def Valid (d : Device) (t : Ticket) : Prop :=
  t.epoch ≤ d.epoch ∧ (t.epoch = d.epoch → t.polarity = d.polarity)

def change (d : Device) (p : Bool) : Device :=
  if d.locked then d else ⟨d.epoch+1,p,false⟩

def reserve (d : Device) (t : Ticket) : Device :=
  if t.epoch = d.epoch then { d with locked := true } else d

def deliver (d : Device) (t : Ticket) : Option Bool :=
  if d.locked && (t.epoch == d.epoch) then
    some (xor (xor t.requested t.polarity) d.polarity)
  else none

def release (d : Device) : Device := { d with locked := false }

def changes : Device → List Bool → Device
  | d, [] => d
  | d, p :: ps => changes (change d p) ps

theorem sample_valid (d : Device) (requested : Bool) : Valid d (sample d requested) := by
  simp [Valid, sample]

theorem change_valid (d : Device) (t : Ticket) (h : Valid d t) (p : Bool) :
    Valid (change d p) t := by
  unfold change
  split_ifs
  · exact h
  · rcases h with ⟨le,_⟩
    constructor
    · simp; omega
    · simp; omega

theorem reserve_valid (d : Device) (t : Ticket) (h : Valid d t) :
    Valid (reserve d t) t := by
  unfold reserve
  split_ifs <;> exact h

theorem changes_valid (d : Device) (t : Ticket) (h : Valid d t) (ps : List Bool) :
    Valid (changes d ps) t := by
  induction ps generalizing d with
  | nil => exact h
  | cons p ps ih => exact ih _ (change_valid d t h p)

theorem reserved_changes_freeze (d : Device) (locked : d.locked = true) (ps : List Bool) :
    changes d ps = d := by
  induction ps with
  | nil => rfl
  | cons p ps ih => simpa [changes, change, locked] using ih

theorem deliver_only_correct (d : Device) (t : Ticket) (h : Valid d t) :
    deliver d t = none ∨ deliver d t = some t.requested := by
  unfold deliver
  split_ifs with guard
  · right
    have epoch : t.epoch = d.epoch := by simpa using (Bool.and_eq_true.mp guard).2
    rw [h.2 epoch]
    cases t.requested <;> cases d.polarity <;> rfl
  · exact Or.inl rfl

theorem matched_reservation_delivers (d : Device) (t : Ticket) (h : Valid d t)
    (epoch : t.epoch = d.epoch) : deliver (reserve d t) t = some t.requested := by
  simp only [reserve, epoch, ↓reduceIte, deliver, beq_self_eq_true, Bool.and_self]
  rw [h.2 epoch]
  cases t.requested <;> cases d.polarity <;> rfl

theorem protected_interval_delivers (d : Device) (t : Ticket) (h : Valid d t)
    (epoch : t.epoch = d.epoch) (ps : List Bool) :
    deliver (changes (reserve d t) ps) t = some t.requested := by
  have locked : (reserve d t).locked = true := by simp [reserve,epoch]
  rw [reserved_changes_freeze _ locked]
  exact matched_reservation_delivers d t h epoch

theorem delayed_test_remains_safe (d : Device) (requested : Bool) (before after : List Bool) :
    let t := sample d requested
    let current := changes d before
    deliver (changes (reserve current t) after) t = none ∨
      deliver (changes (reserve current t) after) t = some requested := by
  dsimp
  have h := changes_valid d (sample d requested) (sample_valid d requested) before
  exact deliver_only_correct _ _ (changes_valid _ _ (reserve_valid _ _ h) after)

theorem fresh_test_then_reservation_completes (d : Device) (requested : Bool) (ps : List Bool) :
    deliver (changes (reserve d (sample d requested)) ps) (sample d requested) = some requested := by
  exact protected_interval_delivers d _ (sample_valid d requested) rfl ps

theorem release_allows_change (d : Device) (p : Bool) :
    (change (release d) p).epoch = d.epoch + 1 ∧
    (change (release d) p).polarity = p := by simp [change,release]

def initial : Device := ⟨0,false,false⟩

def unprotectedUse (d : Device) (t : Ticket) : Bool :=
  xor (xor t.requested t.polarity) d.polarity

theorem check_then_change_then_use_fails :
    (sample initial true).epoch = initial.epoch ∧
    unprotectedUse (change initial true) (sample initial true) = false := by decide

theorem stale_test_is_rejected :
    deliver (reserve (change initial true) (sample initial true)) (sample initial true) = none := by decide

theorem reservation_blocks_race :
    deliver (change (reserve initial (sample initial true)) true) (sample initial true) = some true := by decide

def bypass (d : Device) (p : Bool) : Device := { d with polarity := p }

theorem bypass_defeats_reservation :
    deliver (bypass (reserve initial (sample initial true)) true) (sample initial true) = some false := by decide

end CorrectionRace
