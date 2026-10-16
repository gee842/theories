import GenerativeCore
import RecipientCorrection

/- A paid client of actual coupling boundary fields. The source availability,
fixed target laws, faithful channel and finite stabilized lifecycle are premises.
The original stochastic formation/prefix reachability is checked separately. -/
namespace RecipientIdentification

open RecipientCorrection (Target Laws lookup pack unpack packedAct packedWrite receiptOf)

structure Registers where
  q : Nat
  flag : Bool
  deriving DecidableEq, Repr

def actor (m : Registers) : Bool := packedAct m.q .actor
def candidate (m : Registers) : Bool := packedAct m.q .recipient
def Sound (m : Registers) (z : Bool) : Prop := m.flag = true → candidate m = z

def revise (m : Registers) (returned : Bool) : Registers :=
  if m.flag then m
  else if returned then { m with flag := true }
  else { m with q := packedWrite m.q .recipient (!candidate m) }

def feedback (m : Registers) (target : Target) (record : Option Bool) : Registers :=
  match target, record with
  | .recipient, some returned => revise m returned
  | _, _ => m

theorem positive_receipt_identifies (action z available : Bool)
    (h : receiptOf action z available = true) : action = z := by
  cases action <;> cases z <;> cases available <;> simp_all [receiptOf]

theorem zero_receipt_ambiguity :
    receiptOf false false false = receiptOf false true true ∧ (false : Bool) ≠ true := by decide

theorem no_total_zero_decoder :
    ¬ ∃ d : Bool → Bool → Bool, ∀ a z v, d a (receiptOf a z v) = z := by
  rintro ⟨d,h⟩
  have h₀ := h false false false
  have h₁ := h false true true
  change d false false = false at h₀
  change d false false = true at h₁
  rw [h₀] at h₁
  contradiction

theorem revise_sound (m : Registers) (z returned : Bool)
    (hs : Sound m z) (faithful : returned = true → candidate m = z) :
    Sound (revise m returned) z := by
  cases hf : m.flag <;> cases returned <;>
    simp_all [Sound, revise, candidate]

theorem recipient_physical_feedback_sound (m : Registers) (z available : Bool)
    (hs : Sound m z) : Sound (revise m (receiptOf (candidate m) z available)) z :=
  revise_sound m z _ hs (positive_receipt_identifies _ _ _)

theorem unknown_zero_explores (m : Registers) (h : m.flag = false) :
    candidate (revise m false) = !candidate m ∧ (revise m false).flag = false := by
  simp [revise, h, candidate, RecipientCorrection.packed_write_sets_queried_cell]

theorem unknown_positive_qualifies (m : Registers) (h : m.flag = false) :
    candidate (revise m true) = candidate m ∧ (revise m true).flag = true := by
  simp [revise, h, candidate]

theorem qualified_record_retained (m : Registers) (h : m.flag = true) (r : Bool) :
    revise m r = m := by simp [revise,h]

theorem actor_cell_preserved (m : Registers) (r : Bool) :
    actor (revise m r) = actor m := by
  cases hf : m.flag <;> cases r <;>
    simp [revise,hf,actor,RecipientCorrection.recipient_write_preserves_actor_cell]

theorem actor_feedback_is_sham (m : Registers) (record : Option Bool) :
    feedback m .actor record = m := by cases record <;> rfl

theorem missing_feedback_retains (m : Registers) (target : Target) :
    feedback m target none = m := by cases target <;> rfl

theorem revise_bounded (m : Registers) (r : Bool) (h : m.q < 4) :
    (revise m r).q < 4 := by
  cases hf : m.flag <;> cases r <;>
    simp [revise,hf] <;> first | exact h | exact RecipientCorrection.packed_write_bounded _ _ _

def encode (a c k : Bool) : Registers := ⟨pack (a,c),k⟩

theorem three_bits_decode (a c k : Bool) :
    actor (encode a c k) = a ∧ candidate (encode a c k) = c ∧
    (encode a c k).flag = k ∧ (encode a c k).q < 5 := by
  simp [encode,actor,candidate,packedAct,RecipientCorrection.unpack_pack,lookup]
  exact RecipientCorrection.existing_five_code_register_suffices _

theorem encoded_state_injective (a c k a' c' k' : Bool)
    (h : encode a c k = encode a' c' k') : a = a' ∧ c = c' ∧ k = k' := by
  have ha := congrArg actor h
  have hc := congrArg candidate h
  have hk := congrArg Registers.flag h
  constructor
  · simpa [encode,actor,packedAct,RecipientCorrection.unpack_pack,lookup] using ha
  constructor
  · simpa [encode,candidate,packedAct,RecipientCorrection.unpack_pack,lookup] using hc
  · exact hk

/- Physical fields read at the unchanged coupling client's handoff. Diagnostic
witness flags are not inputs. q and last are the inherited ten-state capacity. -/
structure Boundary where
  fuel : Nat
  stage : Nat
  life : Nat
  gateLife : Nat
  coupling : Int
  couplingLife : Nat
  written : Bool
  q : Nat
  last : Bool
  deriving DecidableEq, Repr

def Eligible (b : Boundary) : Prop := b.stage = 2 ∧ 0 < b.life ∧ 0 < b.gateLife ∧
  b.coupling = 0 ∧ 0 < b.couplingLife ∧ b.written = true ∧ (b.q = 0 ∨ b.q = 4)

def registers (b : Boundary) : Registers := ⟨b.q,b.last⟩
def setRegisters (b : Boundary) (m : Registers) : Boundary := { b with q := m.q, last := m.flag }

def retrofit (b : Boundary) : Boundary :=
  { b with fuel := b.fuel-4, q := pack (b.q == 4,b.q == 4), last := false }

theorem retrofit_paid (b : Boundary) (h : 4 ≤ b.fuel) : (retrofit b).fuel + 4 = b.fuel := by
  simp [retrofit]; omega

theorem retrofit_is_unknown (b : Boundary) (z : Bool) :
    Sound (registers (retrofit b)) z ∧ (retrofit b).last = false := by
  simp [Sound,registers,retrofit]

theorem retrofit_preserves_acquired_actor (b : Boundary) :
    actor (registers (retrofit b)) = (b.q == 4) ∧
    candidate (registers (retrofit b)) = (b.q == 4) := by
  simp [actor,candidate,registers,retrofit,packedAct,RecipientCorrection.unpack_pack,lookup]

theorem retrofit_preserves_hardware (b : Boundary) :
    (retrofit b).life = b.life ∧ (retrofit b).gateLife = b.gateLife ∧
    (retrofit b).coupling = b.coupling ∧ (retrofit b).couplingLife = b.couplingLife ∧
    (retrofit b).stage = b.stage ∧ (retrofit b).written = b.written := by
  exact ⟨rfl,rfl,rfl,rfl,rfl,rfl⟩

inductive Phase where
  | ready | rented | sensed (target : Target) | reserved (target : Target)
  | worked (target : Target) (receipt : Bool)
  | acquired (target : Target) (record : Option Bool)
  deriving DecidableEq, Repr

def targetOf : Phase → Target
  | .sensed t | .reserved t | .worked t _ | .acquired t _ => t
  | _ => .actor

def requiredEscrow : Phase → Nat
  | .reserved _ | .worked _ _ => 3
  | .acquired _ _ => 2
  | _ => 0

structure State where
  hardware : Boundary
  patient : Nat
  packets : Nat
  escrow : Nat
  phase : Phase
  active : Bool
  deriving DecidableEq, Repr

def initial (b : Boundary) (packets : Nat) : State :=
  ⟨retrofit b,0,packets,0,.ready,true⟩
def Valid (s : State) : Prop := s.hardware.q < 4 ∧ s.escrow = requiredEscrow s.phase

def Handoff (b : Boundary) (packets : Nat) (s : State) : Prop :=
  Eligible b ∧ 4 ≤ b.fuel ∧ s = initial b packets

def issued (s : State) : Bool := packedAct s.hardware.q (targetOf s.phase)
def returned (laws : Laws) (s : State) (available : Bool) : Bool :=
  receiptOf (issued s) (lookup laws (targetOf s.phase)) available

def credit (target : Target) (r : Bool) : Nat := if target == .actor && r then 10 else 0
def patientCredit (target : Target) (r : Bool) : Nat := if target == .recipient && r then 10 else 0

def acquiredRecord : Phase → Option Bool | .acquired _ r => r | _ => none

inductive Event where
  | rent | sense (target : Target) | reserve | work (available : Bool)
  | acquire (channel : Bool) | write | miss
  deriving DecidableEq, Repr

def Enabled (s : State) : Event → Prop
  | .rent => s.active = true ∧ s.phase = .ready ∧ 0 < s.packets ∧ 8 ≤ s.hardware.fuel
  | .sense _ => s.phase = .rented ∧ 1 ≤ s.hardware.fuel
  | .reserve => (∃ t, s.phase = .sensed t) ∧ 6 ≤ s.hardware.fuel ∧ 0 < s.packets
  | .work _ => (∃ t, s.phase = .reserved t) ∧ 3 ≤ s.hardware.fuel ∧ 0 < s.packets
  | .acquire _ => (∃ t r, s.phase = .worked t r) ∧ 1 ≤ s.escrow
  | .write => (∃ t r, s.phase = .acquired t r) ∧ 2 ≤ s.escrow
  | .miss => s.phase = .ready ∧ 0 < s.packets ∧ (s.active = false ∨ s.hardware.fuel < 8)

def advance (laws : Laws) (s : State) : Event → State
  | .rent => { s with hardware := { s.hardware with fuel := s.hardware.fuel-1 }, phase := .rented }
  | .sense target => { s with hardware := { s.hardware with fuel := s.hardware.fuel-1 }, phase := .sensed target }
  | .reserve => { s with hardware := { s.hardware with fuel := s.hardware.fuel-3 }, escrow := 3, phase := .reserved (targetOf s.phase) }
  | .work av => { s with
      hardware := { s.hardware with fuel := s.hardware.fuel-3+credit (targetOf s.phase) (returned laws s av) },
      patient := s.patient+patientCredit (targetOf s.phase) (returned laws s av),
      packets := s.packets-1, phase := .worked (targetOf s.phase) (returned laws s av) }
  | .acquire channel => { s with
      escrow := s.escrow-1,
      phase := match s.phase with
        | .worked target r => .acquired target (if channel then some r else none)
        | _ => s.phase }
  | .write => { s with
      hardware := setRegisters s.hardware (feedback (registers s.hardware) (targetOf s.phase) (acquiredRecord s.phase)),
      escrow := s.escrow-2, phase := .ready }
  | .miss => { s with active := false, packets := s.packets-1 }

def Step (laws : Laws) (s : State) (e : Event) (t : State) : Prop :=
  Valid s ∧ Enabled s e ∧ t = advance laws s e

def process (laws : Laws) : Generative.Process State Event := ⟨Step laws⟩
def energy (s : State) : Nat := s.hardware.fuel+s.patient+10*s.packets+s.escrow

def spending : Event → Nat
  | .rent | .sense _ | .acquire _ => 1
  | .work _ => 3
  | .write => 2
  | _ => 0

def waste (laws : Laws) (s : State) : Event → Nat
  | .work av => if returned laws s av then 0 else 10
  | .miss => 10
  | _ => 0

def spentAlong (laws : Laws) (s : State) : List Event → Nat
  | [] => 0
  | e :: es => spending e + waste laws s e + spentAlong laws (advance laws s e) es

instance (b : Boundary) : Decidable (Eligible b) := by unfold Eligible; infer_instance
instance (s : State) : Decidable (Valid s) := by unfold Valid; infer_instance

instance (s : State) (e : Event) : Decidable (Enabled s e) := by
  cases e <;> cases hp : s.phase <;> simp [Enabled,hp] <;> infer_instance

instance (laws : Laws) (s : State) (e : Event) (t : State) : Decidable (Step laws s e t) := by
  unfold Step; infer_instance

theorem handoff_valid (b : Boundary) (packets : Nat) : Valid (initial b packets) := by
  simp [Valid,initial,retrofit,requiredEscrow]
  exact RecipientCorrection.packed_code_bounded _

theorem handoff_energy (b : Boundary) (packets : Nat) (h : 4 ≤ b.fuel) :
    energy (initial b packets)+4 = b.fuel+10*packets := by
  simp [energy,initial,retrofit]; omega

theorem qualified_command (s : State) (z : Bool)
    (h : Sound (registers s.hardware) z) (hk : s.hardware.last = true)
    (ht : targetOf s.phase = .recipient) : issued s = z := by
  simpa [issued,ht,candidate,registers] using h hk


theorem feedback_bounded (m : Registers) (target : Target) (r : Option Bool)
    (h : m.q < 4) : (feedback m target r).q < 4 := by
  cases target <;> cases r <;> simp only [feedback] <;>
    first | exact h | exact revise_bounded _ _ h

theorem step_valid {laws : Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : Valid t := by
  rcases h with ⟨hv,he,rfl⟩
  cases e with
  | rent => simp_all [Valid,Enabled,advance,requiredEscrow]
  | sense target => simp_all [Valid,Enabled,advance,requiredEscrow]
  | reserve =>
      rcases he with ⟨⟨target,hp⟩,_,_⟩
      simpa [Valid,advance,hp,targetOf,requiredEscrow] using hv.1
  | work av =>
      rcases he with ⟨⟨target,hp⟩,_,_⟩
      simpa [Valid,advance,hp,targetOf,requiredEscrow] using hv
  | acquire channel =>
      rcases he with ⟨⟨target,r,hp⟩,_⟩
      simpa [Valid,advance,hp,requiredEscrow] using hv
  | write =>
      rcases he with ⟨⟨target,r,hp⟩,_⟩
      have hb := feedback_bounded (registers s.hardware) target r hv.1
      have heq : s.escrow = 2 := by simpa [Valid,hp,requiredEscrow] using hv.2
      simpa [Valid,advance,hp,setRegisters,targetOf,acquiredRecord,requiredEscrow,heq] using hb
  | miss => simpa [Valid,advance] using hv

theorem step_energy {laws : Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : energy t + spending e + waste laws s e = energy s := by
  rcases h with ⟨hv,he,rfl⟩
  cases e with
  | rent => simp_all [Enabled,advance,energy,spending,waste]; omega
  | sense target => simp_all [Enabled,advance,energy,spending,waste]; omega
  | reserve =>
      rcases he with ⟨⟨target,hp⟩,hf,_⟩
      have heq : s.escrow = 0 := by simpa [hp,requiredEscrow] using hv.2
      simp [advance,energy,spending,waste,heq]; omega
  | work av =>
      rcases he with ⟨⟨target,hp⟩,hf,hs⟩
      have hpack : 10*(s.packets-1)+10 = 10*s.packets := by omega
      cases target <;> cases hr : returned laws s av <;>
        simp [advance,energy,spending,waste,hp,targetOf,hr,credit,patientCredit] <;> omega
  | acquire channel =>
      rcases he with ⟨⟨target,r,hp⟩,hf⟩
      simp [advance,energy,spending,waste]; omega
  | write =>
      rcases he with ⟨⟨target,r,hp⟩,hf⟩
      simp [advance,energy,spending,waste,setRegisters]; omega
  | miss =>
      have hs := he.2.1
      simp [advance,energy,spending,waste]; omega

theorem trace_energy {laws : Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : energy t + spentAlong laws s es = energy s := by
  induction h with
  | nil => simp [spentAlong]
  | @cons s u t e es hs _ ih =>
      have he := step_energy hs
      rcases hs with ⟨_,_,rfl⟩
      simp only [spentAlong]
      omega

theorem admission_prefunded (s : State) (h : Enabled s .rent) : 8 ≤ s.hardware.fuel := h.2.2.2

theorem unpayable_no_query (s : State) (h : s.hardware.fuel < 8) : ¬ Enabled s .rent := by
  simp only [Enabled]; omega

theorem inactive_no_query (s : State) (h : s.active = false) : ¬ Enabled s .rent := by
  simp [Enabled,h]

theorem recipient_cannot_fund_own_query (s : State) (h : s.hardware.fuel < 8) (p : Nat) :
    ¬ Enabled { s with patient := p } .rent := by
  simp only [Enabled]; omega

def trial (target : Target) (av channel : Bool) : List Event :=
  [.rent,.sense target,.reserve,.work av,.acquire channel,.write]
def run (laws : Laws) (s : State) (events : List Event) : State := events.foldl (advance laws) s

theorem trial_exists (laws : Laws) (s : State) (target : Target) (av channel : Bool)
    (hv : Valid s) (hp : s.phase = .ready) (ha : s.active = true)
    (hf : 8 ≤ s.hardware.fuel) (hn : 0 < s.packets) :
    Generative.Trace (process laws) s (trial target av channel) (run laws s (trial target av channel)) := by
  have h₁ : Step laws s .rent (advance laws s .rent) := ⟨hv,⟨ha,hp,hn,hf⟩,rfl⟩
  have h₂ : Step laws (advance laws s .rent) (.sense target)
      (advance laws (advance laws s .rent) (.sense target)) := by
    refine ⟨step_valid h₁,?_,rfl⟩
    simp [Enabled,advance]; omega
  let u := advance laws (advance laws s .rent) (.sense target)
  have hu : Valid u := step_valid h₂
  have h₃ : Step laws u .reserve (advance laws u .reserve) := by
    refine ⟨hu,?_,rfl⟩
    simp [Enabled,u,advance,hn]; omega
  let v := advance laws u .reserve
  have h₄ : Step laws v (.work av) (advance laws v (.work av)) := by
    refine ⟨step_valid h₃,?_,rfl⟩
    simp [Enabled,v,u,advance,hn]; omega
  let w := advance laws v (.work av)
  have h₅ : Step laws w (.acquire channel) (advance laws w (.acquire channel)) := by
    refine ⟨step_valid h₄,?_,rfl⟩
    simp [Enabled,w,v,advance]
  have h₆ : Step laws (advance laws w (.acquire channel)) .write
      (advance laws (advance laws w (.acquire channel)) .write) := by
    refine ⟨step_valid h₅,?_,rfl⟩
    simp [Enabled,w,v,advance]
  exact .cons h₁ (.cons h₂ (.cons h₃ (.cons h₄ (.cons h₅ (.cons h₆ (.nil _))))))

theorem trial_registers (laws : Laws) (s : State) (target : Target) (av channel : Bool) :
    registers (run laws s (trial target av channel)).hardware =
      feedback (registers s.hardware) target
        (if channel then some (receiptOf (packedAct s.hardware.q target) (lookup laws target) av) else none) := by
  cases target <;> cases channel <;>
    simp [registers,run,trial,advance,setRegisters,targetOf,acquiredRecord,returned,issued]

theorem trial_actor_preserved (laws : Laws) (s : State) (target : Target) (av channel : Bool) :
    actor (registers (run laws s (trial target av channel)).hardware) = actor (registers s.hardware) := by
  rw [trial_registers]
  cases target <;> cases channel <;> simp [feedback,actor_cell_preserved]

theorem trial_sound (laws : Laws) (s : State) (target : Target) (av channel : Bool)
    (hs : Sound (registers s.hardware) laws.2) :
    Sound (registers (run laws s (trial target av channel)).hardware) laws.2 := by
  rw [trial_registers]
  cases target <;> cases channel <;> simp only [Bool.false_eq_true,if_false,if_true,feedback] <;>
    first | exact hs | exact recipient_physical_feedback_sound _ _ _ hs

theorem trial_positive_qualifies (laws : Laws) (s : State) (av : Bool)
    (h : receiptOf (candidate (registers s.hardware)) laws.2 av = true)
    (hs : Sound (registers s.hardware) laws.2) :
    (run laws s (trial .recipient av true)).hardware.last = true ∧
    candidate (registers (run laws s (trial .recipient av true)).hardware) = laws.2 := by
  have hr := trial_registers laws s .recipient av true
  have hz := trial_sound laws s .recipient av true hs
  have hk : (run laws s (trial .recipient av true)).hardware.last = true := by
    have he := congrArg Registers.flag hr
    have hp : receiptOf (packedAct s.hardware.q .recipient) laws.2 av = true := h
    cases hf : s.hardware.last <;>
      simpa [feedback,revise,registers,lookup,hf,hp] using he
  exact ⟨hk,hz hk⟩



theorem trace_run {laws : Laws} {s t : State} {events : List Event}
    (h : Generative.Trace (process laws) s events t) : t = run laws s events := by
  induction h with
  | nil => rfl
  | cons hs _ ih =>
      rcases hs with ⟨_,_,rfl⟩
      exact ih

theorem paid_trial_sound {laws : Laws} {s t : State} {target : Target} {av channel : Bool}
    (h : Generative.Trace (process laws) s (trial target av channel) t)
    (hs : Sound (registers s.hardware) laws.2) : Sound (registers t.hardware) laws.2 := by
  rw [trace_run h]
  exact trial_sound _ _ _ _ _ hs

theorem paid_qualified_use {laws : Laws} {s t : State} {channel : Bool}
    (h : Generative.Trace (process laws) s (trial .recipient true channel) t)
    (hs : Sound (registers s.hardware) laws.2) (hk : s.hardware.last = true) :
    t.patient = s.patient + 10 := by
  have hc : packedAct s.hardware.q .recipient = laws.2 := hs hk
  rw [trace_run h]
  simp [run,trial,advance,targetOf,returned,issued,lookup,hc,receiptOf,patientCredit]

def exampleBoundary (fuel : Nat) : Boundary := ⟨fuel,2,6,2,0,2,true,0,false⟩
def exampleStart (fuel : Nat) : State := initial (exampleBoundary fuel) 5
def exampleLaws : Laws := (false,true)
def rTrial := trial .recipient true true
def aTrial := trial .actor true true
def afterR₁ (fuel : Nat) := run exampleLaws (exampleStart fuel) rTrial
def afterA₁ (fuel : Nat) := run exampleLaws (afterR₁ fuel) aTrial
def afterR₂ (fuel : Nat) := run exampleLaws (afterA₁ fuel) rTrial
def afterA₂ (fuel : Nat) := run exampleLaws (afterR₂ fuel) aTrial
def afterR₃ (fuel : Nat) := run exampleLaws (afterA₂ fuel) rTrial
def fiveTrials := rTrial ++ aTrial ++ rTrial ++ aTrial ++ rTrial

theorem actual_client_handoff : Handoff (exampleBoundary 28) 5 (exampleStart 28) := by
  unfold Handoff
  decide

theorem actual_five_query_trace :
    Generative.Trace (process exampleLaws) (exampleStart 28) fiveTrials (afterR₃ 28) := by
  have h₁ := trial_exists exampleLaws (exampleStart 28) .recipient true true
    (by decide) (by decide) (by decide) (by decide) (by decide)
  have h₂ := trial_exists exampleLaws (afterR₁ 28) .actor true true
    (by decide) (by decide) (by decide) (by decide) (by decide)
  have h₃ := trial_exists exampleLaws (afterA₁ 28) .recipient true true
    (by decide) (by decide) (by decide) (by decide) (by decide)
  have h₄ := trial_exists exampleLaws (afterR₂ 28) .actor true true
    (by decide) (by decide) (by decide) (by decide) (by decide)
  have h₅ := trial_exists exampleLaws (afterA₂ 28) .recipient true true
    (by decide) (by decide) (by decide) (by decide) (by decide)
  have h₁₂ := Generative.trace_append_iff.mpr ⟨_,h₁,h₂⟩
  have h₁₂₃ := Generative.trace_append_iff.mpr ⟨_,h₁₂,h₃⟩
  have h₁₂₃₄ := Generative.trace_append_iff.mpr ⟨_,h₁₂₃,h₄⟩
  exact Generative.trace_append_iff.mpr ⟨_,h₁₂₃₄,h₅⟩

theorem paid_exploration_then_qualified_use :
    (afterR₁ 28).hardware.last = false ∧
    candidate (registers (afterR₁ 28).hardware) = true ∧
    (afterR₁ 28).patient = 0 ∧
    (afterR₂ 28).hardware.last = true ∧
    candidate (registers (afterR₂ 28).hardware) = true ∧
    (afterR₂ 28).patient = 10 ∧ (afterR₃ 28).patient = 20 ∧
    (afterR₃ 28).hardware.fuel = 4 ∧ (afterR₃ 28).packets = 0 := by decide

theorem concrete_whole_suffix_account :
    energy (afterR₃ 28) + spentAlong exampleLaws (exampleStart 28) fiveTrials + 4 = 28+5*10 ∧
    spentAlong exampleLaws (exampleStart 28) fiveTrials = 50 := by decide

def FiveAffordable (fuel : Nat) : Prop :=
  8 ≤ (exampleStart fuel).hardware.fuel ∧ 8 ≤ (afterR₁ fuel).hardware.fuel ∧
  8 ≤ (afterA₁ fuel).hardware.fuel ∧ 8 ≤ (afterR₂ fuel).hardware.fuel ∧
  8 ≤ (afterA₂ fuel).hardware.fuel

theorem five_query_budget_iff (fuel : Nat) : FiveAffordable fuel ↔ 26 ≤ fuel := by
  simp [FiveAffordable,exampleStart,exampleBoundary,initial,retrofit,afterR₁,afterA₁,
    afterR₂,afterA₂,rTrial,aTrial,run,trial,advance,targetOf,returned,issued,exampleLaws,
    registers,setRegisters,feedback,revise,candidate,acquiredRecord,receiptOf,lookup,
    packedAct,packedWrite,RecipientCorrection.update,unpack,pack,RecipientCorrection.bitNat,
    credit]
  omega

theorem twenty_five_blocks_second_actor :
    (afterR₂ 25).hardware.fuel = 7 ∧ ¬ Enabled (afterR₂ 25) .rent ∧
    Enabled (afterR₂ 25) .miss ∧
    (advance exampleLaws (afterR₂ 25) .miss).active = false ∧
    (advance exampleLaws (afterR₂ 25) .miss).hardware.fuel = 7 := by
  unfold Enabled
  decide

theorem no_exploration_can_stall (z : Bool) :
    receiptOf (!z) z true = false ∧ receiptOf (!z) z false = false := by cases z <;> decide

theorem changed_target_invalidates_old_qualification :
    Sound (encode false true true) true ∧ ¬ Sound (encode false true true) false := by
  unfold Sound
  decide

end RecipientIdentification

#print axioms RecipientIdentification.positive_receipt_identifies
#print axioms RecipientIdentification.zero_receipt_ambiguity
#print axioms RecipientIdentification.no_total_zero_decoder
#print axioms RecipientIdentification.revise_sound
#print axioms RecipientIdentification.recipient_physical_feedback_sound
#print axioms RecipientIdentification.unknown_zero_explores
#print axioms RecipientIdentification.unknown_positive_qualifies
#print axioms RecipientIdentification.qualified_record_retained
#print axioms RecipientIdentification.actor_cell_preserved
#print axioms RecipientIdentification.actor_feedback_is_sham
#print axioms RecipientIdentification.missing_feedback_retains
#print axioms RecipientIdentification.revise_bounded
#print axioms RecipientIdentification.three_bits_decode
#print axioms RecipientIdentification.encoded_state_injective
#print axioms RecipientIdentification.retrofit_paid
#print axioms RecipientIdentification.retrofit_is_unknown
#print axioms RecipientIdentification.retrofit_preserves_acquired_actor
#print axioms RecipientIdentification.retrofit_preserves_hardware
#print axioms RecipientIdentification.handoff_valid
#print axioms RecipientIdentification.handoff_energy
#print axioms RecipientIdentification.qualified_command
#print axioms RecipientIdentification.feedback_bounded
#print axioms RecipientIdentification.step_valid
#print axioms RecipientIdentification.step_energy
#print axioms RecipientIdentification.trace_energy
#print axioms RecipientIdentification.admission_prefunded
#print axioms RecipientIdentification.unpayable_no_query
#print axioms RecipientIdentification.inactive_no_query
#print axioms RecipientIdentification.recipient_cannot_fund_own_query
#print axioms RecipientIdentification.trial_exists
#print axioms RecipientIdentification.trial_registers
#print axioms RecipientIdentification.trial_actor_preserved
#print axioms RecipientIdentification.trial_sound
#print axioms RecipientIdentification.trial_positive_qualifies
#print axioms RecipientIdentification.trace_run
#print axioms RecipientIdentification.paid_trial_sound
#print axioms RecipientIdentification.paid_qualified_use
#print axioms RecipientIdentification.actual_client_handoff
#print axioms RecipientIdentification.actual_five_query_trace
#print axioms RecipientIdentification.paid_exploration_then_qualified_use
#print axioms RecipientIdentification.concrete_whole_suffix_account
#print axioms RecipientIdentification.five_query_budget_iff
#print axioms RecipientIdentification.twenty_five_blocks_second_actor
#print axioms RecipientIdentification.no_exploration_can_stall
#print axioms RecipientIdentification.changed_target_invalidates_old_qualification
