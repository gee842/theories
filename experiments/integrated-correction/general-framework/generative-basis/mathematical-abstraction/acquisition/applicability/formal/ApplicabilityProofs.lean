import AcquiredApplicability

/-!
Generic results for the declared protocol. These laws do not assert that every
admitted event ordering is the implemented policy: the independent finite-history
certificates additionally check `policyWord`, guards and actual source projection.
The source relation, receipt semantics, family, tariffs and policy remain supplied.
-/
namespace AcquiredApplicability

set_option maxHeartbeats 4000000
set_option maxRecDepth 16384

/-- Constructive arithmetic helpers avoid the classical dependencies of the
convenience arithmetic tactic/library cancellation wrappers. -/
theorem cancel_add_right (a b c : Nat) (h : a+c = b+c) : a=b := by
  induction c with
  | zero => exact h
  | succ c ih => exact ih (Nat.succ.inj h)

theorem debit_cancel (a d : Nat) (h : d ≤ a) : (a-d)+d = a := by
  induction d generalizing a with
  | zero => rfl
  | succ d ih =>
    cases a with
    | zero => exact False.elim (Nat.not_succ_le_zero _ h)
    | succ a =>
      rw [Nat.succ_sub_succ_eq_sub]
      exact congrArg Nat.succ (ih a (Nat.le_of_succ_le_succ h))

theorem swap_last (a b c : Nat) : a+b+c = a+c+b := by
  rw [Nat.add_assoc a b c,Nat.add_comm b c,←Nat.add_assoc a c b]

theorem balance_trans {a b c x y z : Nat}
    (h : b+x=a+y) (g : c+y=b+z) : c+x=a+z := by
  apply cancel_add_right _ _ y
  calc
    (c+x)+y = (c+y)+x := swap_last _ _ _
    _ = (b+z)+x := congrArg (fun n => n+x) g
    _ = (b+x)+z := swap_last _ _ _
    _ = (a+y)+z := congrArg (fun n => n+z) h
    _ = (a+z)+y := swap_last _ _ _

/-- Conserved quantities across one operation, stated without signed subtraction. -/
structure Conserves (b t : Body) : Prop where
  start : t.account.start = b.account.start
  ledger : t.account.fuel + t.account.spent + b.account.income =
    b.account.fuel + b.account.spent + t.account.income
  source : t.physical.source + t.physical.transferred + t.physical.wasted =
    b.physical.source + b.physical.transferred + b.physical.wasted
  actualCredit : t.account.income + 65536*b.physical.transferred =
    b.account.income + 65536*t.physical.transferred

theorem Conserves.refl (b : Body) : Conserves b b := ⟨rfl,rfl,rfl,rfl⟩
theorem Conserves.trans {b t u : Body} (h : Conserves b t) (g : Conserves t u) :
    Conserves b u :=
  ⟨g.start.trans h.start, balance_trans h.ledger g.ledger,
    g.source.trans h.source, balance_trans h.actualCredit g.actualCredit⟩

theorem fail_conserves (b : Body) (e : Error) : Conserves b (fail b e) := by
  constructor <;> rfl

theorem charge_conserves (b : Body) (w l t e r : Nat) :
    Conserves b (charge b w l t e r) := by
  unfold charge
  dsimp only
  split
  · exact fail_conserves _ _
  · split
    · exact fail_conserves _ _
    · constructor
      · rfl
      · dsimp only
        have hd := debit_cancel b.account.fuel (tariff b.account w l t e r)
          (Nat.le_of_not_lt ‹¬ b.account.fuel < tariff b.account w l t e r›)
        calc
          _ = ((b.account.fuel-tariff b.account w l t e r)+tariff b.account w l t e r)
            + b.account.spent + b.account.income := by
              rw [Nat.add_comm b.account.spent (tariff b.account w l t e r),
                ←Nat.add_assoc]
          _ = _ := congrArg (fun n => n+b.account.spent+b.account.income) hd
      · rfl
      · rfl

theorem paid_conserves (b : Body) (w l t e r : Nat) (f : Body → Body)
    (hf : ∀ x, Conserves x (f x)) : Conserves b (paid b w l t e r f) := by
  unfold paid
  dsimp only
  split
  · exact (charge_conserves b w l t e r).trans (hf _)
  · exact charge_conserves b w l t e r

theorem native_conserves (b : Body) (f : Body → Body)
    (hf : ∀ x, Conserves x (f x)) : Conserves b (nativeCharge b f) :=
  paid_conserves _ _ _ _ _ _ _ hf

theorem extracted_conserves (cfg : Config) (b : Body) : Conserves b (extracted cfg b) := by
  unfold extracted
  split
  · exact fail_conserves _ _
  · have hd := debit_cancel b.physical.source 10
      (Nat.le_of_not_lt ‹¬ b.physical.source < 10›)
    dsimp only
    split
    · constructor
      · rfl
      · dsimp only
        rw [swap_last b.account.fuel 655360 b.account.spent,
          swap_last (b.account.fuel+b.account.spent) 655360 b.account.income,
          Nat.add_assoc]
      · dsimp only
        calc
          _ = ((b.physical.source-10)+10) + b.physical.transferred + b.physical.wasted := by
              rw [Nat.add_zero b.physical.wasted, Nat.add_comm b.physical.transferred 10,
                ←Nat.add_assoc (b.physical.source-10) 10 b.physical.transferred]
          _ = _ := congrArg (fun n => n+b.physical.transferred+b.physical.wasted) hd
      · dsimp only
        rw [Nat.mul_add]
        change (b.account.income+655360)+65536*b.physical.transferred =
          b.account.income+(65536*b.physical.transferred+655360)
        rw [swap_last b.account.income 655360 (65536*b.physical.transferred), Nat.add_assoc]
    · constructor
      · rfl
      · rfl
      · dsimp only
        calc
          _ = ((b.physical.source-10)+10) + b.physical.transferred + b.physical.wasted := by
              rw [Nat.add_zero, ←Nat.add_assoc,
                swap_last ((b.physical.source-10)+b.physical.transferred) b.physical.wasted 10,
                swap_last (b.physical.source-10) b.physical.transferred 10]
          _ = _ := congrArg (fun n => n+b.physical.transferred+b.physical.wasted) hd
      · rfl

/-- Even a denied operation preserves earlier actual effects and conserves the
ledger. No operation can create credit independently of source transfer. -/
theorem advanceBody_conserves (H : Machine) (cfg : Config) (b : Body) (e : Event) :
    Conserves b (advanceBody H cfg b e) := by
  cases e with
  | install => dsimp only [advanceBody]; apply paid_conserves; intro t; constructor <;> rfl
  | prepare => dsimp only [advanceBody]; apply paid_conserves; intro t; constructor <;> rfl
  | reset => dsimp only [advanceBody]; apply native_conserves; intro t; constructor <;> rfl
  | advance => dsimp only [advanceBody]; apply native_conserves; intro t; constructor <;> rfl
  | sense => dsimp only [advanceBody]; apply native_conserves; intro t; constructor <;> rfl
  | checkSensor =>
    dsimp only [advanceBody]
    apply paid_conserves
    intro t
    split
    · constructor <;> rfl
    · exact fail_conserves _ _
  | extract => exact native_conserves _ _ (extracted_conserves cfg)
  | readReceipt =>
    dsimp only [advanceBody]
    apply paid_conserves
    intro t
    cases cfg.receiptMode <;> constructor <;> rfl
  | commit =>
    dsimp only [advanceBody]
    split
    · exact fail_conserves _ _
    · apply paid_conserves
      intro t
      dsimp only
      split <;> constructor <;> rfl
  | closeRoute => dsimp only [advanceBody]; constructor <;> rfl
  | scan =>
    dsimp only [advanceBody]
    apply paid_conserves
    intro t
    split <;> constructor <;> rfl
  | select => dsimp only [advanceBody]; apply paid_conserves; intro t; constructor <;> rfl
  | clamp => dsimp only [advanceBody]; apply paid_conserves; intro t; constructor <;> rfl
  | stop => dsimp only [advanceBody]; constructor <;> rfl
  | finish => dsimp only [advanceBody]; constructor <;> rfl
  | retain =>
    dsimp only [advanceBody]
    split
    · exact fail_conserves _ _
    · apply paid_conserves; intro t; constructor <;> rfl

@[simp] theorem advance_H (s : State) (e : Event) : (advance s e).H = s.H := rfl
@[simp] theorem advance_config (s : State) (e : Event) :
    (advance s e).config = s.config := rfl

theorem run_preserves_H (s : State) (es : List Event) : (run s es).H = s.H := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih => exact ih _

theorem run_conserves (s : State) (es : List Event) : Conserves s.body (run s es).body := by
  induction es generalizing s with
  | nil => exact Conserves.refl _
  | cons e es ih => exact (advanceBody_conserves s.H s.config s.body e).trans (ih (advance s e))

/-- A successful guard certificate is a path in the shared relational core. -/
theorem runnable_trace (s : State) (es : List Event) (h : Runnable s es) :
    Generative.Trace process s es (run s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih =>
    exact .cons ⟨h.1,rfl⟩ (ih _ h.2)

theorem trace_is_run {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) : t = run s es := by
  induction h with
  | nil => rfl
  | @cons s m t e es hs ht ih =>
    have hm : m = advance s e := hs.2
    subst m
    exact ih

theorem trace_preserves_H {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) : t.H = s.H := by
  rw [trace_is_run h]
  exact run_preserves_H s es

theorem trace_conserves {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) : Conserves s.body t.body := by
  rw [trace_is_run h]
  exact run_conserves s es

/-- Actual credit, in exact fuel ticks, is tied to transferred packets, including
histories ending in a denial or unavailable receipt. -/
theorem trace_no_phantom_credit {s t : State} {es : List Event}
    (h : Generative.Trace process s es t)
    (hi : s.body.account.income = 0) (ht : s.body.physical.transferred = 0) :
    t.body.account.income = 65536*t.body.physical.transferred := by
  have hc := (trace_conserves h).actualCredit
  rw [hi,ht,Nat.mul_zero,Nat.add_zero,Nat.zero_add] at hc
  exact hc

theorem trace_ledger {s t : State} {es : List Event}
    (h : Generative.Trace process s es t)
    (hl : s.body.account.fuel + s.body.account.spent =
      s.body.account.start + s.body.account.income) :
    t.body.account.fuel + t.body.account.spent =
      t.body.account.start + t.body.account.income := by
  have hc := trace_conserves h
  apply cancel_add_right _ _ s.body.account.income
  calc
    _ = s.body.account.fuel + s.body.account.spent + t.body.account.income := hc.ledger
    _ = (s.body.account.start+s.body.account.income)+t.body.account.income :=
      congrArg (fun n => n+t.body.account.income) hl
    _ = (t.body.account.start+t.body.account.income)+s.body.account.income := by
      rw [hc.start]
      exact swap_last _ _ _


/-- Retention of a supplied candidate is conditional on the acquired outcome
agreeing with that candidate; truth is not inferred from the mere write. -/
theorem mem_update_iff (c : Candidate) (cs : List Candidate) (b r : Bool) :
    c ∈ update cs b r ↔ c ∈ cs ∧ arrival c b = r := by
  induction cs with
  | nil =>
    constructor
    · intro h; cases h
    · intro h; cases h.1
  | cons x xs ih =>
    cases hp : (arrival x b == r) with
    | false =>
      have hf : update (x::xs) b r = update xs b r := by
        change (match arrival x b == r with | true => x::update xs b r | false => update xs b r) = _
        rw [hp]
      rw [hf]
      constructor
      · intro h
        exact ⟨.tail _ (ih.mp h).1,(ih.mp h).2⟩
      · rintro ⟨h,hr⟩
        cases h with
        | head =>
          have ht : (arrival c b == r) = true := beq_iff_eq.mpr hr
          rw [hp] at ht
          cases ht
        | tail _ h => exact ih.mpr ⟨h,hr⟩
    | true =>
      have hf : update (x::xs) b r = x::update xs b r := by
        change (match arrival x b == r with | true => x::update xs b r | false => update xs b r) = _
        rw [hp]
      rw [hf]
      constructor
      · intro h
        cases h with
        | head => exact ⟨.head _,beq_iff_eq.mp hp⟩
        | tail _ h => exact ⟨.tail _ (ih.mp h).1,(ih.mp h).2⟩
      · rintro ⟨h,hr⟩
        cases h with
        | head => exact .head _
        | tail _ h => exact .tail _ (ih.mpr ⟨h,hr⟩)

theorem faithful_candidate_retained (c : Candidate) (cs : List Candidate) (b r : Bool)
    (hc : c ∈ cs) (faithful : arrival c b = r) : c ∈ update cs b r :=
  (mem_update_iff _ _ _ _).mpr ⟨hc,faithful⟩

theorem zero_is_ambiguous : update family true false = [.complement,.blocked] := by decide
theorem positive_first : update family true true = [.identity] := by decide
theorem productive_disagreement (b : Bool) :
    conflicting [.complement,.blocked] b = !b := by cases b <;> rfl

theorem second_positive_disambiguates :
    update [.complement,.blocked] false true = [.complement] := by decide
theorem second_zero_disambiguates :
    update [.complement,.blocked] false false = [.blocked] := by decide

theorem misleading_receipt_can_remove_true_candidate :
    Candidate.complement ∈ family ∧
    Candidate.complement ∉ update family true true := by
  constructor
  · exact .tail _ (.head _)
  · intro h
    change Candidate.complement ∈ [Candidate.identity] at h
    cases h with
    | tail _ h => cases h

/-- These are pre-debit constraints. Nat subtraction cannot turn an
unaffordable debit into a successful operation. -/
def CanPay (b : Body) (work newLive temporary extra rewrites : Nat) : Prop :=
  b.error = .none ∧
  max b.account.live newLive + b.account.workspace + temporary ≤ b.account.capacity ∧
  tariff b.account work newLive temporary extra rewrites ≤ b.account.fuel

theorem charge_when_affordable (b : Body) (w l t e r : Nat)
    (h : CanPay b w l t e r) :
    charge b w l t e r =
      {b with account:={b.account with
        fuel:=b.account.fuel-tariff b.account w l t e r,
        spent:=b.account.spent+tariff b.account w l t e r,
        live:=l,peak:=max b.account.peak (max b.account.live l+b.account.workspace+t)}} := by
  rcases h with ⟨_,hc,hf⟩
  simp only [charge]
  split
  · exact False.elim (Nat.not_lt_of_ge hc ‹_›)
  · split
    · exact False.elim (Nat.not_lt_of_ge hf ‹_›)
    · rfl

theorem charge_error_affordable (b : Body) (w l t e r : Nat)
    (h : CanPay b w l t e r) : (charge b w l t e r).error = .none :=
  (congrArg Body.error (charge_when_affordable b w l t e r h)).trans h.1

theorem charge_preserves_observational_fields (b : Body) (w l t e r : Nat) :
    (charge b w l t e r).control.record = b.control.record ∧
    (charge b w l t e r).control.candidates = b.control.candidates ∧
    (charge b w l t e r).physical = b.physical := by
  dsimp only [charge]
  split
  · exact ⟨rfl,rfl,rfl⟩
  · split <;> exact ⟨rfl,rfl,rfl⟩

theorem paid_apply (b : Body) (w l t e r : Nat) (f : Body → Body)
    (h : (charge b w l t e r).error = .none) :
    paid b w l t e r f = f (charge b w l t e r) := if_pos h

theorem charge_insufficient (b : Body) (w l t e r : Nat)
    (h : b.account.fuel < tariff b.account w l t e r) :
    (charge b w l t e r).account = b.account ∧
    (charge b w l t e r).physical = b.physical ∧
    (charge b w l t e r).control.record = b.control.record ∧
    (charge b w l t e r).error ≠ .none := by
  simp only [charge]
  split
  · exact ⟨rfl,rfl,rfl,fun q => Error.noConfusion q⟩
  · exact ⟨rfl,rfl,rfl,fun q => Error.noConfusion q⟩

/-- The charged write changes applicability while retaining the old sensory H
(by `advance_H`). It is not itself a proof that the acquired receipt is faithful. -/
theorem commit_updates_acquired_record (H : Machine) (cfg : Config) (b : Body)
    (hd : cfg.deny ≠ .commit)
    (hp : CanPay b (2*b.control.candidates.length+1)
      (liveCells b.control (update b.control.candidates (b.sensor.getD false)
        (b.receipt.getD false)) b.control.word)
      (2*b.control.candidates.length+2) 0
      ((update b.control.candidates (b.sensor.getD false) (b.receipt.getD false)).length+4)) :
    (advanceBody H cfg b .commit).control.candidates =
      update b.control.candidates (b.sensor.getD false) (b.receipt.getD false) ∧
    (advanceBody H cfg b .commit).control.record =
      some ⟨b.sensor.getD false,b.receipt.getD false⟩ ∧
    (advanceBody H cfg b .commit).control.attempts = b.control.attempts+1 := by
  dsimp only [advanceBody]
  have hn : ¬ (cfg.deny == Deny.commit) = true := fun q => hd (beq_iff_eq.mp q)
  rw [if_neg hn]
  dsimp only [paid]
  rw [charge_when_affordable _ _ _ _ _ _ hp]
  dsimp only
  rw [if_pos hp.1]
  split <;> exact ⟨rfl,rfl,rfl⟩

/-- A write interruption retains old candidates and the old committed record;
source effects have already occurred and are not rolled back. -/
theorem commit_denied_preserves (H : Machine) (cfg : Config) (b : Body)
    (h : cfg.deny = .commit) :
    (advanceBody H cfg b .commit).control.candidates = b.control.candidates ∧
    (advanceBody H cfg b .commit).control.record = b.control.record ∧
    (advanceBody H cfg b .commit).physical = b.physical ∧
    (advanceBody H cfg b .commit).error = .commitDenied := by
  dsimp only [advanceBody]
  rw [h]
  exact ⟨rfl,rfl,rfl,rfl⟩

theorem missing_receipt_is_not_zero (H : Machine) (cfg : Config) (b : Body)
    (hm : cfg.receiptMode = .missing) (hp : CanPay b 0 b.account.live 2 16384 0) :
    (advanceBody H cfg b .readReceipt).error = .missing ∧
    (advanceBody H cfg b .readReceipt).control.record = b.control.record ∧
    (advanceBody H cfg b .readReceipt).control.candidates = b.control.candidates ∧
    (advanceBody H cfg b .readReceipt).physical = b.physical := by
  dsimp only [advanceBody]
  rw [hm]
  rw [paid_apply b 0 b.account.live 2 16384 0 _ (charge_error_affordable _ _ _ _ _ _ hp)]
  have hc := charge_preserves_observational_fields b 0 b.account.live 2 16384 0
  exact ⟨rfl,hc.1,hc.2.1,hc.2.2⟩

theorem retention_denied_preserves_committed (H : Machine) (cfg : Config) (b : Body)
    (h : cfg.deny = .retain) :
    (advanceBody H cfg b .retain).control.record = b.control.record ∧
    (advanceBody H cfg b .retain).control.retained = false ∧
    (advanceBody H cfg b .retain).physical = b.physical := by
  dsimp only [advanceBody]
  rw [h]
  exact ⟨rfl,rfl,rfl⟩

/-- The query computation has no access to apparatus configuration. -/
theorem scan_config_independent (H : Machine) (c d : Config) (b : Body) :
    advanceBody H c b .scan = advanceBody H d b .scan := rfl

/-- In the surviving ambiguous family, exactly H-negative queries can both
separate outcomes and possibly produce the sought arrival. This applies to any
H, not only the ordinary three-state fixture. -/
theorem scan_ambiguous_selects (H : Machine) (cfg : Config) (b : Body)
    (hc : b.control.candidates = [.complement,.blocked])
    (hb : H.answer b.scanIndex = false)
    (hp : CanPay b (2*(b.scanIndex+1)+b.control.candidates.length) b.account.live
      (b.scanIndex+3+b.control.candidates.length) 0 0) :
    (advanceBody H cfg b .scan).pc = .choosing ∧
    (advanceBody H cfg b .scan).scanIndex = b.scanIndex := by
  dsimp only [advanceBody,paid]
  rw [charge_when_affordable _ _ _ _ _ _ hp]
  dsimp only
  rw [if_pos hp.1]
  try dsimp only
  rw [hc,hb]
  exact ⟨rfl,rfl⟩

theorem scan_ambiguous_skips (H : Machine) (cfg : Config) (b : Body)
    (hc : b.control.candidates = [.complement,.blocked])
    (hb : H.answer b.scanIndex = true)
    (hp : CanPay b (2*(b.scanIndex+1)+b.control.candidates.length) b.account.live
      (b.scanIndex+3+b.control.candidates.length) 0 0) :
    (advanceBody H cfg b .scan).pc = .searching ∧
    (advanceBody H cfg b .scan).scanIndex = b.scanIndex+1 := by
  dsimp only [advanceBody,paid]
  rw [charge_when_affordable _ _ _ _ _ _ hp]
  dsimp only
  rw [if_pos hp.1]
  try dsimp only
  rw [hc,hb]
  exact ⟨rfl,rfl⟩

theorem selection_installs_scanned_word (H : Machine) (cfg : Config) (b : Body)
    (hp : CanPay b (b.scanIndex+1)
      (liveCells b.control b.control.candidates b.scanIndex)
      (b.scanIndex+3) 0 (b.scanIndex+2)) :
    (advanceBody H cfg b .select).control.word = b.scanIndex := by
  dsimp only [advanceBody,paid]
  rw [charge_when_affordable _ _ _ _ _ _ hp]
  dsimp only
  rw [if_pos hp.1]

/-- The read clamp preserves the acquired record and the old word while still
incurring its declared work. It is an intervention on use, not on acquisition. -/
theorem clamp_preserves_old_word_and_record (H : Machine) (cfg : Config) (b : Body)
    (hp : CanPay b (b.control.word+1) b.account.live (b.control.word+3) 0 0) :
    (advanceBody H cfg b .clamp).control.word = b.control.word ∧
    (advanceBody H cfg b .clamp).control.record = b.control.record ∧
    (advanceBody H cfg b .clamp).control.candidates = b.control.candidates := by
  dsimp only [advanceBody,paid]
  rw [charge_when_affordable _ _ _ _ _ _ hp]
  dsimp only
  rw [if_pos hp.1]
  exact ⟨rfl,rfl,rfl⟩

/-- Early stopping is a policy property. A positive acquired record does not
thereby certify actual arrival when receipt fidelity is absent. -/
theorem policy_stops_after_first_positive (s : State)
    (he : s.body.error = .none) (hp : s.body.pc = .between)
    (hn : s.body.control.attempts = 1)
    (hr : s.body.control.record.any (fun r => r.receipt) = true) :
    nextEvent s = some .stop := by
  dsimp only [nextEvent]
  rw [he]
  try dsimp only
  rw [hp]
  try dsimp only
  rw [hn]
  try dsimp only
  rw [hr]
  rfl

theorem policy_reads_acquired_failure (s : State)
    (he : s.body.error = .none) (hp : s.body.pc = .between)
    (hn : s.body.control.attempts = 1)
    (hr : s.body.control.record = some ⟨true,false⟩)
    (hc : s.config.clamp = false) : nextEvent s = some .scan := by
  dsimp only [nextEvent]
  rw [he]
  try dsimp only
  rw [hp]
  try dsimp only
  rw [hn]
  try dsimp only
  rw [hr]
  try dsimp only
  rw [hc]
  rfl

theorem policy_clamped_failure (s : State)
    (he : s.body.error = .none) (hp : s.body.pc = .between)
    (hn : s.body.control.attempts = 1)
    (hr : s.body.control.record = some ⟨true,false⟩)
    (hc : s.config.clamp = true) : nextEvent s = some .clamp := by
  dsimp only [nextEvent]
  rw [he]
  try dsimp only
  rw [hp]
  try dsimp only
  rw [hn]
  try dsimp only
  rw [hr]
  try dsimp only
  rw [hc]
  rfl

end AcquiredApplicability
