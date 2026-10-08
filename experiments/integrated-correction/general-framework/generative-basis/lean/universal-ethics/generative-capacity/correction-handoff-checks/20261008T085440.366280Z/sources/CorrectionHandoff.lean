import Mathlib.Tactic

/- Two channels are roles within one installation. Their records are produced
by an explicit probe. The probe/operational decoder correspondence, atomic
steps and exclusive configuration mediation are model premises. Bool commands
stand for two already-authorized outcomes; this model does not confer authority. -/
namespace CorrectionHandoff

structure Record where
  epoch : Nat
  polarity : Bool
  deriving DecidableEq, Repr

structure Channel where
  epoch : Nat
  polarity : Bool
  live : Bool
  record : Option Record
  deriving DecidableEq, Repr

def decode (c : Channel) (command : Bool) : Bool := xor command c.polarity

def Sound (c : Channel) : Prop := ∀ r, c.record = some r →
  r.epoch ≤ c.epoch ∧ (r.epoch = c.epoch → r.polarity = c.polarity)

def Ready (c : Channel) : Prop := c.live = true ∧
  ∃ r, c.record = some r ∧ r.epoch = c.epoch

instance readyDecidable (c : Channel) : Decidable (Ready c) := by
  unfold Ready
  cases c.record <;> simp <;> infer_instance

def probe (c : Channel) : Channel :=
  { c with record := some ⟨c.epoch, decode c false⟩ }

def configure (c : Channel) (p : Bool) : Channel :=
  { c with epoch := c.epoch + 1, polarity := p, live := false }

def power (c : Channel) (b : Bool) : Channel := { c with live := b }

def execute (c : Channel) (requested : Bool) : Option Bool :=
  if c.live then c.record.map (fun r => decode c (xor requested r.polarity)) else none

theorem probe_learns_decoder (c : Channel) : decode c false = c.polarity := by
  cases c.polarity <;> rfl

theorem probe_sound (c : Channel) : Sound (probe c) := by
  intro r hr
  simp only [probe, Option.some.injEq] at hr
  subst r
  simp [probe, probe_learns_decoder]

theorem configure_sound (c : Channel) (h : Sound c) (p : Bool) : Sound (configure c p) := by
  intro r hr
  have hh := h r hr
  simp only [configure]
  constructor
  · omega
  · intro eqv
    omega

theorem power_sound (c : Channel) (h : Sound c) (b : Bool) : Sound (power c b) := h

theorem ready_executes (c : Channel) (hs : Sound c) (hr : Ready c) (requested : Bool) :
    execute c requested = some requested := by
  rcases hr with ⟨live,r,record,epoch⟩
  have polarity := (hs r record).2 epoch
  simp only [execute, live, ↓reduceIte, record, Option.map_some, decode, polarity]
  cases requested <;> cases c.polarity <;> rfl

theorem probe_preserves_ready (c : Channel) (h : Ready c) : Ready (probe c) := by
  exact ⟨h.1, ⟨c.epoch, decode c false⟩, rfl, rfl⟩

theorem power_on_ready (c : Channel) (h : Ready c) : Ready (power c true) := by
  exact ⟨rfl,h.2⟩

theorem configure_rejects_old_record (c : Channel) (h : Sound c) (p : Bool) :
    ¬ Ready (power (configure c p) true) := by
  rintro ⟨_,r,record,epoch⟩
  have hh := (h r record).1
  change r.epoch = c.epoch + 1 at epoch
  omega

structure Installation where
  active : Bool
  channels : Bool → Channel

def replace (s : Installation) (slot : Bool) (c : Channel) : Installation :=
  { s with channels := fun b => if b = slot then c else s.channels b }

def Invariant (s : Installation) : Prop :=
  (∀ b, Sound (s.channels b)) ∧ Ready (s.channels s.active)

inductive Operation where
  | test (slot : Bool)
  | reconfigure (slot polarity : Bool)
  | enable (slot : Bool)
  | switch (slot : Bool)
  | retire (slot : Bool)
  | pause
  deriving DecidableEq, Repr

def step (s : Installation) : Operation → Installation
  | .test b => replace s b (probe (s.channels b))
  | .reconfigure b p => if b = s.active then s else replace s b (configure (s.channels b) p)
  | .enable b => replace s b (power (s.channels b) true)
  | .switch b => if Ready (s.channels b) then { s with active := b } else s
  | .retire b => if b = s.active then s else replace s b (power (s.channels b) false)
  | .pause => s

theorem replace_inactive (s : Installation) (h : Invariant s)
    (b : Bool) (different : b ≠ s.active) (c : Channel) (sound : Sound c) :
    Invariant (replace s b c) := by
  constructor
  · intro j
    simp only [replace]
    split_ifs
    · exact sound
    · exact h.1 j
  · simpa [replace, Ne.symm different] using h.2

theorem replace_ready (s : Installation) (h : Invariant s)
    (b : Bool) (c : Channel) (sound : Sound c)
    (ready : b = s.active → Ready c) : Invariant (replace s b c) := by
  constructor
  · intro j
    simp only [replace]
    split_ifs
    · exact sound
    · exact h.1 j
  · simp only [replace]
    split_ifs with eqv
    · exact ready eqv.symm
    · exact h.2

theorem step_preserves (s : Installation) (h : Invariant s) (op : Operation) :
    Invariant (step s op) := by
  cases op with
  | test b =>
    apply replace_ready s h b _ (probe_sound _)
    intro eqv
    apply probe_preserves_ready
    simpa [eqv] using h.2
  | reconfigure b p =>
    simp only [step]
    split_ifs with eqv
    · exact h
    · exact replace_inactive s h b eqv _ (configure_sound _ (h.1 b) p)
  | enable b =>
    apply replace_ready s h b _ (power_sound _ (h.1 b) true)
    intro eqv
    apply power_on_ready
    simpa [eqv] using h.2
  | switch b =>
    simp only [step]
    split_ifs with ready
    · exact ⟨h.1,ready⟩
    · exact h
  | retire b =>
    simp only [step]
    split_ifs with eqv
    · exact h
    · exact replace_inactive s h b eqv _ (power_sound _ (h.1 b) false)
  | pause => exact h

def run (s : Installation) : List Operation → Installation
  | [] => s
  | op :: ops => run (step s op) ops

theorem run_preserves (s : Installation) (h : Invariant s) (ops : List Operation) :
    Invariant (run s ops) := by
  induction ops generalizing s with
  | nil => exact h
  | cons op ops ih => exact ih _ (step_preserves s h op)

theorem every_interruptible_prefix (s : Installation) (h : Invariant s)
    (ops : List Operation) (n : Nat) (requested : Bool) :
    execute ((run s (ops.take n)).channels (run s (ops.take n)).active) requested = some requested := by
  have hr := run_preserves s h (ops.take n)
  exact ready_executes _ (hr.1 _) hr.2 requested

theorem unbounded_schedule_safety (states : Nat → Installation) (ops : Nat → Operation)
    (initial : Invariant (states 0)) (law : ∀ n, states (n+1) = step (states n) (ops n)) :
    ∀ n requested, execute ((states n).channels (states n).active) requested = some requested := by
  have inv : ∀ n, Invariant (states n) := by
    intro n
    induction n with
    | zero => exact initial
    | succ n ih => rw [law]; exact step_preserves _ ih _
  intro n requested
  exact ready_executes _ ((inv n).1 _) (inv n).2 requested

def handoff (s : Installation) (polarity : Bool) : List Operation :=
  [.reconfigure (!s.active) polarity, .enable (!s.active), .test (!s.active),
   .switch (!s.active), .retire s.active]

theorem handoff_completes (s : Installation) (p : Bool) :
    (run s (handoff s p)).active = !s.active ∧
    ((run s (handoff s p)).channels s.active).live = false ∧
    ((run s (handoff s p)).channels (!s.active)).polarity = p := by
  cases ha : s.active <;>
    simp [handoff, run, step, replace, configure, power, probe, Ready, ha]

def initial : Installation :=
  ⟨false, fun b => if b then ⟨0,false,false,none⟩ else ⟨0,false,true,some ⟨0,false⟩⟩⟩

theorem initial_invariant : Invariant initial := by
  constructor
  · intro b; cases b <;> simp [initial, Sound]
  · simp [initial, Ready]

-- A mutation for the counterexample: switch on a live channel and any record,
-- ignoring whether the revision still matches.
def uncheckedSwitch (s : Installation) (b : Bool) : Installation :=
  if (s.channels b).live && (s.channels b).record.isSome then { s with active := b } else s

def stalePreparation : List Operation :=
  [.reconfigure true false, .enable true, .test true,
   .reconfigure true true, .enable true]

theorem stale_record_switch_fails :
    execute ((uncheckedSwitch (run initial stalePreparation) true).channels true) true = some false := by
  decide

theorem guarded_stale_switch_retains_service :
    (step (run initial stalePreparation) (.switch true)).active = false ∧
    execute ((step (run initial stalePreparation) (.switch true)).channels false) true = some true := by
  decide

theorem fresh_retest_restores_switch :
    (run initial (stalePreparation ++ [.test true,.switch true,.retire false])).active = true ∧
    execute ((run initial (stalePreparation ++ [.test true,.switch true,.retire false])).channels true) true = some true := by
  decide

theorem early_retirement_breaks_service :
    execute (power (initial.channels false) false) true = none := by rfl

theorem pause_does_not_complete_handoff : (run initial [.pause,.pause]).active = false := by rfl

end CorrectionHandoff
