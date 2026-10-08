import RecursiveSelection

/-! A costed continuation of the two causal-source models. A supplied successor
recipe changes carrier yield between two and three; outputs debit a represented
feed stock. Probes, repair, receipts and replacements share the actual state.
Material conversion, faithful sensing, route isolation and supply remain local
laws. None is an ethical verdict or an empirical identification claim. -/

namespace CarrierDiagnosis
open RecursiveSelection (Source)

structure Receipt where
  carrier : Nat
  before : Nat
  amount : Nat
  after : Nat
  cut : Bool
  deriving DecidableEq, Repr

structure State where
  condition : Nat
  carrier : Nat
  rich : Bool
  parts : Nat
  feed : Nat
  funds : Nat
  source : Source
  receipt : Option Receipt
  deriving DecidableEq, Repr

structure Input where
  parts : Nat
  feed : Nat
  cut : Bool
  deriving DecidableEq, Repr

def capacity (s : State) : Nat := if s.rich then 3 else 2
def emitted (s : State) : Nat := if 3 ≤ s.condition then capacity s else 0
def returned (cut : Bool) (s : State) : Nat :=
  match s.source with
  | .activity => if cut then 0 else emitted s
  | .substitute => emitted s
def charge (cut : Bool) : Nat := if cut then 1 else 0
def Ready (i : Input) (s : State) : Prop :=
  0 < s.parts ∧ emitted s ≤ s.feed ∧ charge i.cut ≤ s.funds
instance (i : Input) (s : State) : Decidable (Ready i s) := inferInstanceAs (Decidable (_ ∧ _ ∧ _))

def outcome (i : Input) (s : State) : State :=
  let q := min 8 (s.condition - 1 + returned i.cut s)
  { condition := q, carrier := s.carrier+1, rich := !s.rich,
    parts := s.parts-1+i.parts, feed := s.feed-emitted s+i.feed,
    funds := s.funds-charge i.cut, source := s.source,
    receipt := some ⟨s.carrier, s.condition, capacity s, q, i.cut⟩ }

def run (i : Input) (s : State) : State := if Ready i s then outcome i s else s
theorem performed (i : Input) (s : State) (hr : Ready i s) : run i s = outcome i s := by
  rw [run, if_pos hr]

def ordinary : Input := ⟨1, 3, false⟩
def probeInput : Input := ⟨0, 0, true⟩

def Stable (s : State) : Prop :=
  3 ≤ s.condition ∧ s.condition ≤ 8 ∧ 0 < s.parts ∧ 3 ≤ s.feed
instance (s : State) : Decidable (Stable s) := inferInstanceAs (Decidable (_ ∧ _ ∧ _ ∧ _))

def recurring (s : State) : Nat → State
  | 0 => s
  | t+1 => run ordinary (recurring s t)

def RepairReady (s : State) : Prop :=
  s.condition < 3 ∧ 0 < s.feed ∧ 0 < s.funds
instance (s : State) : Decidable (RepairReady s) := inferInstanceAs (Decidable (_ ∧ _ ∧ _))

/-- Actual repair transfers one feed unit to the maintained condition, paying
one funding unit. It does not reconstruct a carrier or replenish its parts. -/
def repaired (s : State) : State :=
  { s with condition := s.condition+1, feed := s.feed-1, funds := s.funds-1 }
def repair (s : State) : State := if RepairReady s then repaired s else s

inductive Action where
  | cycle : Input → Action
  | repair

def process : Generative.Process State Action where
  step s a t := match a with
    | .cycle i => Ready i s ∧ t = outcome i s
    | .repair => RepairReady s ∧ t = repaired s

/-- This readout uses the probe receipt alone, with a declared comparison class.
It receives neither the source field nor an oracle for that field. -/
def classify (r : Receipt) : Option Source :=
  if r.cut = true ∧ 3 ≤ r.before ∧ r.before ≤ 8 ∧ 2 ≤ r.amount then
    if r.after = r.before-1 then some .activity
    else if r.after = min 8 (r.before-1+r.amount) then some .substitute
    else none
  else none

def readSource (s : State) : Option Source := s.receipt.bind classify

def diagnose (s : State) : State :=
  let t := run probeInput s
  if readSource t = some .activity then repair t else t

/-- Failed probes do not certify an inherited receipt as a new diagnosis. -/
def diagnosisResult (s : State) : Option (Source × State) :=
  if Ready probeInput s then
    (readSource (diagnose s)).map fun source => (source, diagnose s)
  else none

theorem capacity_bounds (s : State) : 2 ≤ capacity s ∧ capacity s ≤ 3 := by
  unfold capacity
  split <;> omega

theorem emitted_bounds (s : State) : emitted s ≤ 3 := by
  have := capacity_bounds s
  unfold emitted
  split <;> omega

theorem ordinary_return (s : State) : returned false s = emitted s := by
  cases h : s.source <;> simp [returned, h]

theorem return_bound (cut : Bool) (s : State) : returned cut s ≤ emitted s := by
  unfold returned
  cases s.source <;> cases cut <;> simp

theorem ordinary_ready (s : State) (hs : Stable s) : Ready ordinary s := by
  have he := emitted_bounds s
  unfold Ready ordinary charge
  simp only [Bool.false_eq_true, ↓reduceIte]
  unfold Stable at hs
  omega

theorem ordinary_preserves (s : State) (hs : Stable s) :
    Stable (run ordinary s) := by
  have hr := ordinary_ready s hs
  have hc := capacity_bounds s
  have hq : 3 ≤ s.condition := hs.1
  have he : emitted s = capacity s := by simp [emitted, hq]
  unfold run
  rw [if_pos hr]
  unfold Stable outcome ordinary
  simp only [ordinary_return, he]
  unfold Stable at hs
  omega

theorem recurrence_with_variant_carriers (s : State) (hs : Stable s) (t : Nat) :
    Stable (recurring s t) ∧
    (recurring s t).carrier = s.carrier+t ∧
    (recurring s t).source = s.source := by
  induction t with
  | zero => exact ⟨hs, by rfl, by rfl⟩
  | succ t ih =>
    have hr := ordinary_ready (recurring s t) ih.1
    have hn := ordinary_preserves (recurring s t) ih.1
    refine ⟨hn, ?_, ?_⟩
    · simp only [recurring, run, if_pos hr, outcome]
      omega
    · simp only [recurring, run, if_pos hr, outcome]
      exact ih.2.2

theorem different_carrier_yields (s : State) (hs : Stable s) :
    capacity (run ordinary s) ≠ capacity s := by
  have hr := ordinary_ready s hs
  simp only [run, if_pos hr, capacity, outcome]
  cases s.rich <;> decide

theorem actual_recurring_trace (s : State) (hs : Stable s) (t : Nat) :
    Generative.Trace process s (List.replicate t (.cycle ordinary)) (recurring s t) := by
  induction t with
  | zero => exact .nil s
  | succ t ih =>
    have hv := (recurrence_with_variant_carriers s hs t).1
    have hr := ordinary_ready _ hv
    have step : process.step (recurring s t) (.cycle ordinary) (recurring s (t+1)) := by
      refine ⟨hr, ?_⟩
      simp [recurring, run, hr]
    have ht := Generative.trace_append_iff.mpr
      ⟨recurring s t, ih, Generative.trace_singleton_iff.mpr step⟩
    rw [← List.replicate_succ'] at ht
    exact ht

theorem ordinary_progress (s : State) (hs : Stable s) :
    min 8 (s.condition+1) ≤ (run ordinary s).condition := by
  have hr := ordinary_ready s hs
  have hc := capacity_bounds s
  have hq := hs.1
  rw [performed _ _ hr]
  change min 8 (s.condition+1) ≤ min 8 (s.condition-1+returned false s)
  rw [ordinary_return, show emitted s = capacity s by simp [emitted, hq]]
  omega

theorem recurrence_progress (s : State) (hs : Stable s) (t : Nat) :
    min 8 (s.condition+t) ≤ (recurring s t).condition := by
  induction t with
  | zero => simp only [recurring, Nat.add_zero]; omega
  | succ t ih =>
    have hv := (recurrence_with_variant_carriers s hs t).1
    have hn := ordinary_progress (recurring s t) hv
    change min 8 (s.condition+(t+1)) ≤ (run ordinary (recurring s t)).condition
    omega

theorem finite_arrival_with_turnover (s : State) (hs : Stable s) (t : Nat)
    (ht : 5 ≤ t) : (recurring s t).condition=8 ∧
    (recurring s (t+1)).carrier ≠ (recurring s t).carrier := by
  have lower := recurrence_progress s hs t
  have now := recurrence_with_variant_carriers s hs t
  have next := recurrence_with_variant_carriers s hs (t+1)
  unfold Stable at hs
  have upper := now.1.2.1
  constructor <;> omega

theorem ordinary_source_change (s : State) (source : Source) :
    run ordinary {s with source := source} = {run ordinary s with source := source} := by
  by_cases hr : Ready ordinary s
  · have hr' : Ready ordinary {s with source := source} := hr
    simp only [run, if_pos hr, if_pos hr']
    cases s with
    | mk q c rich parts feed funds actual receipt =>
      cases actual <;> cases source <;> rfl
  · have hr' : ¬ Ready ordinary {s with source := source} := hr
    simp only [run, if_neg hr, if_neg hr']

theorem recurring_source_change (s : State) (source : Source) (t : Nat) :
    recurring {s with source := source} t = {recurring s t with source := source} := by
  induction t with
  | zero => rfl
  | succ t ih => simp only [recurring, ih, ordinary_source_change]

def visible (s : State) : Nat × Nat × Bool × Nat × Nat × Nat × Option Receipt :=
  (s.condition,s.carrier,s.rich,s.parts,s.feed,s.funds,s.receipt)

theorem full_passive_record_equal (s : State) (t : Nat) :
    visible (recurring {s with source := .activity} t) =
    visible (recurring {s with source := .substitute} t) := by
  simp only [recurring_source_change]
  rfl

def overflow (i : Input) (s : State) : Nat := s.condition-1+returned i.cut s-8
def diverted (i : Input) (s : State) : Nat := emitted s-returned i.cut s
def worn (s : State) : Nat := min 1 s.condition

theorem resource_accounting (i : Input) (s : State) (hr : Ready i s) :
    (outcome i s).condition + (outcome i s).feed + worn s +
      overflow i s + diverted i s = s.condition+s.feed+i.feed := by
  have hb := return_bound i.cut s
  unfold Ready at hr
  unfold outcome worn overflow diverted
  dsimp only
  omega

theorem replacement_accounting (i : Input) (s : State) (hr : Ready i s) :
    (outcome i s).parts+1 = s.parts+i.parts ∧
    (outcome i s).funds+charge i.cut = s.funds := by
  unfold Ready at hr
  unfold outcome
  dsimp only
  omega

theorem empty_feed_blocks (s : State) (hq : 3 ≤ s.condition) (hf : s.feed=0) :
    ¬ Ready ordinary s := by
  have hc := capacity_bounds s
  unfold Ready emitted
  rw [if_pos hq, hf]
  omega

theorem no_advance_funding (s : State) (h : s.funds=0) : ¬ Ready probeInput s := by
  unfold Ready probeInput charge
  simp only [↓reduceIte]
  omega

theorem probe_classifies_actual_source (s : State) (hr : Ready probeInput s)
    (hq : 3 ≤ s.condition) (hu : s.condition ≤ 8) :
    readSource (run probeInput s) = some s.source := by
  have hc := capacity_bounds s
  simp only [run, if_pos hr, readSource, outcome, Option.bind_some]
  unfold classify probeInput
  dsimp only
  have guard : true = true ∧ 3 ≤ s.condition ∧ s.condition ≤ 8 ∧ 2 ≤ capacity s :=
    ⟨rfl, hq, hu, hc.1⟩
  rw [if_pos guard]
  unfold returned emitted
  rw [if_pos hq]
  cases hsrc : s.source
  · simp only [↓reduceIte, Nat.add_zero]
    have hb : min 8 (s.condition-1) = s.condition-1 := by omega
    rw [hb]
    simp
  · have hd : ¬ min 8 (s.condition-1+capacity s) = s.condition-1 := by omega
    rw [if_neg hd]
    simp

theorem repair_accounting (s : State) (hr : RepairReady s) :
    (repaired s).condition + (repaired s).feed = s.condition+s.feed ∧
    (repaired s).funds+1=s.funds ∧ (repaired s).carrier=s.carrier := by
  unfold RepairReady at hr
  unfold repaired
  dsimp only
  omega

/-- Uniform sufficient support for probing either causal implementation, with
repair if needed and enough actual material for the next heterogeneous carrier. -/
def Prepared (s : State) : Prop :=
  3 ≤ s.condition ∧ s.condition ≤ 8 ∧ 2 ≤ s.parts ∧
  capacity s+4 ≤ s.feed ∧ 2 ≤ s.funds

theorem prepared_probe_ready (s : State) (hp : Prepared s) : Ready probeInput s := by
  unfold Prepared at hp
  unfold Ready probeInput charge emitted
  rw [if_pos hp.1]
  simp only [↓reduceIte]
  omega

theorem repair_keeps_receipt (s : State) : readSource (repair s) = readSource s := by
  unfold repair
  split <;> rfl

theorem repair_keeps_carrier (s : State) : (repair s).carrier = s.carrier := by
  unfold repair
  split <;> rfl

theorem repair_recovers (s : State) (hq : 2 ≤ s.condition) (hu : s.condition ≤ 8)
    (hp : 0 < s.parts) (hf : 4 ≤ s.feed) (hb : 0 < s.funds) : Stable (repair s) := by
  by_cases hl : s.condition < 3
  · have hr : RepairReady s := ⟨hl, by omega, hb⟩
    simp only [repair, if_pos hr, Stable, repaired]
    omega
  · have hr : ¬ RepairReady s := by intro h; exact hl h.1
    simp only [repair, if_neg hr, Stable]
    omega

theorem diagnosis_preserves_continuation (s : State) (hp : Prepared s) :
    Stable (diagnose s) ∧ readSource (diagnose s) = some s.source ∧
    (diagnose s).carrier = s.carrier+1 := by
  have hr := prepared_probe_ready s hp
  have hq := hp.1
  have hu := hp.2.1
  have hc := capacity_bounds s
  have ident := probe_classifies_actual_source s hr hq hu
  have hp' : 0 < (run probeInput s).parts := by
    rw [performed _ _ hr]
    change 0 < s.parts-1+0
    unfold Prepared at hp
    omega
  have hf' : 4 ≤ (run probeInput s).feed := by
    rw [performed _ _ hr]
    change 4 ≤ s.feed-emitted s+0
    rw [show emitted s = capacity s by simp [emitted, hq]]
    unfold Prepared at hp
    omega
  have hb' : 0 < (run probeInput s).funds := by
    rw [performed _ _ hr]
    change 0 < s.funds-1
    unfold Prepared at hp
    omega
  have hid : (run probeInput s).carrier = s.carrier+1 := by
    rw [performed _ _ hr]
    rfl
  unfold diagnose
  dsimp only
  rw [ident]
  cases hsrc : s.source
  · change Stable (repair (run probeInput s)) ∧
      readSource (repair (run probeInput s)) = some .activity ∧
      (repair (run probeInput s)).carrier = s.carrier+1
    have bounds : 2 ≤ (run probeInput s).condition ∧ (run probeInput s).condition ≤ 8 := by
      rw [performed _ _ hr]
      change 2 ≤ min 8 (s.condition-1+returned true s) ∧ min 8 (s.condition-1+returned true s) ≤ 8
      rw [show returned true s = 0 by simp [returned, hsrc]]
      omega
    refine ⟨repair_recovers _ bounds.1 bounds.2 hp' hf' hb', ?_, ?_⟩
    · rw [repair_keeps_receipt, ident, hsrc]
    · rw [repair_keeps_carrier, hid]
  · change Stable (run probeInput s) ∧ readSource (run probeInput s) = some .substitute ∧
      (run probeInput s).carrier = s.carrier+1
    have bounds : 3 ≤ (run probeInput s).condition ∧ (run probeInput s).condition ≤ 8 := by
      rw [performed _ _ hr]
      change 3 ≤ min 8 (s.condition-1+returned true s) ∧ min 8 (s.condition-1+returned true s) ≤ 8
      rw [show returned true s = capacity s by simp [returned, hsrc, emitted, hq]]
      omega
    refine ⟨⟨bounds.1, bounds.2, hp', by omega⟩, ?_, hid⟩
    rw [ident, hsrc]

theorem diagnosis_then_recurrence (s : State) (hp : Prepared s) (t : Nat) :
    Stable (recurring (diagnose s) t) ∧
    (recurring (diagnose s) t).carrier = s.carrier+1+t := by
  have hd := diagnosis_preserves_continuation s hp
  have hr := recurrence_with_variant_carriers (diagnose s) hd.1 t
  exact ⟨hr.1, by rw [hr.2.1, hd.2.2]⟩

theorem successful_diagnosis_result (s : State) (hp : Prepared s) :
    diagnosisResult s = some (s.source, diagnose s) := by
  have hr := prepared_probe_ready s hp
  have hd := (diagnosis_preserves_continuation s hp).2.1
  simp only [diagnosisResult, if_pos hr, hd, Option.map_some]

theorem no_diagnosis_without_execution (s : State) (hr : ¬ Ready probeInput s) :
    diagnosisResult s = none := by simp [diagnosisResult, hr]

theorem actual_diagnosis_trace (s : State) (hr : Ready probeInput s) :
    ∃ events, Generative.Trace process s events (diagnose s) ∧
      (events = [.cycle probeInput] ∨ events = [.cycle probeInput,.repair]) := by
  let t := run probeInput s
  have first : process.step s (.cycle probeInput) t :=
    ⟨hr, performed _ _ hr⟩
  by_cases hc : readSource t = some .activity
  · have hd : diagnose s = repair t := by
      change (if readSource t = some .activity then repair t else t) = repair t
      rw [if_pos hc]
    by_cases hx : RepairReady t
    · refine ⟨[.cycle probeInput,.repair], ?_, Or.inr rfl⟩
      rw [hd, repair, if_pos hx]
      exact .cons first (.cons ⟨hx,rfl⟩ (.nil _))
    · refine ⟨[.cycle probeInput], ?_, Or.inl rfl⟩
      rw [hd, repair, if_neg hx]
      exact .cons first (.nil _)
  · have hd : diagnose s = t := by
      change (if readSource t = some .activity then repair t else t) = t
      rw [if_neg hc]
    refine ⟨[.cycle probeInput], ?_, Or.inl rfl⟩
    rw [hd]
    exact .cons first (.nil _)

def seed (source : Source) : State := ⟨3, 0, false, 2, 6, 2, source, none⟩

theorem no_full_passive_classifier :
    ¬ ∃ label : (Nat → Nat × Nat × Bool × Nat × Nat × Nat × Option Receipt) → Source,
      ∀ s, label (fun t => visible (recurring s t)) = s.source := by
  rintro ⟨label, correct⟩
  have same : (fun t => visible (recurring (seed .activity) t)) =
      (fun t => visible (recurring (seed .substitute) t)) := by
    funext t
    exact full_passive_record_equal (seed .activity) t
  have left := correct (seed .activity)
  have right := correct (seed .substitute)
  rw [same] at left
  rw [left] at right
  contradiction

theorem actual_diagnosis_and_recurrence (s : State) (hp : Prepared s) (t : Nat) :
    ∃ events, Generative.Trace process s
      (events ++ List.replicate t (.cycle ordinary)) (recurring (diagnose s) t) ∧
      (events = [.cycle probeInput] ∨ events = [.cycle probeInput,.repair]) := by
  obtain ⟨events, initial, shape⟩ := actual_diagnosis_trace s (prepared_probe_ready s hp)
  have subsequent := actual_recurring_trace (diagnose s)
    (diagnosis_preserves_continuation s hp).1 t
  exact ⟨events, Generative.trace_append_iff.mpr ⟨diagnose s, initial, subsequent⟩, shape⟩

theorem example_prepared (source : Source) : Prepared (seed source) := by simp [Prepared, seed, capacity]

theorem paid_probe_repair_seed :
    (diagnose (seed .activity)).condition = 3 ∧
    (diagnose (seed .activity)).feed = 3 ∧
    (diagnose (seed .activity)).funds = 0 ∧
    (diagnose (seed .activity)).carrier = 1 ∧
    (diagnose (seed .activity)).rich = true := by decide

theorem heterogeneous_successors_seed :
    (recurring (diagnose (seed .activity)) 1).condition = 5 ∧
    (recurring (diagnose (seed .activity)) 2).condition = 6 ∧
    (recurring (diagnose (seed .activity)) 3).condition = 8 := by decide

theorem identification_without_repair_fails :
    readSource (diagnose { seed .activity with funds := 1 }) = some .activity ∧
    (diagnose { seed .activity with funds := 1 }).condition = 2 := by decide

theorem funding_without_material_fails :
    readSource (diagnose { seed .activity with feed := 2 }) = some .activity ∧
    (diagnose { seed .activity with feed := 2 }).condition = 2 ∧
    (diagnose { seed .activity with feed := 2 }).funds = 1 := by decide

theorem change_probe_changes_target :
    (run probeInput (seed .activity)).condition = 2 ∧
    (run ordinary (seed .activity)).condition = 4 := by decide

theorem waiting_can_avoid_repair :
    readSource (diagnose (run ordinary {seed .activity with funds := 1})) = some .activity ∧
    Stable (diagnose (run ordinary {seed .activity with funds := 1})) ∧
    (diagnose (run ordinary {seed .activity with funds := 1})).funds=0 := by decide

end CarrierDiagnosis
