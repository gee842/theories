import ReasonReplay

/-!
A finite actuator interface, with the unchanged recorded-reason state retained
as an actual component. The gate/workspace recipe, timely context sensing,
physical authority, action effects and ethical action premises are supplied.
Cash and utility are not identified with common fuel. External control events
are not a menu of free strategic actions.
-/
namespace ReasonProtection

set_option maxHeartbeats 2000000
set_option maxRecDepth 8192

abbrev Mask := ReasonReplay.Mask

def empty : Mask := ⟨false,false⟩
def full : Mask := ⟨true,true⟩
def card (m : Mask) : Nat := FormedSelection.bit m.p + FormedSelection.bit m.q

def Covers (outer inner : Mask) : Prop :=
  (inner.p = true → outer.p = true) ∧ (inner.q = true → outer.q = true)
instance (outer inner : Mask) : Decidable (Covers outer inner) := by unfold Covers; infer_instance

inductive Patient where | p | q
deriving DecidableEq, Repr

def member (m : Mask) : Patient → Bool | .p => m.p | .q => m.q
def insert (m : Mask) : Patient → Mask | .p => {m with p := true} | .q => {m with q := true}
def union (a b : Mask) : Mask := ⟨a.p || b.p,a.q || b.q⟩
def difference (a b : Mask) : Mask := ⟨a.p && !b.p,a.q && !b.q⟩

theorem covers_self (m : Mask) : Covers m m := ⟨id,id⟩
theorem covers_trans {a b c : Mask} (hab : Covers a b) (hbc : Covers b c) : Covers a c :=
  ⟨fun h => hab.1 (hbc.1 h),fun h => hab.2 (hbc.2 h)⟩

def patientNode : Patient → ReasonReplay.Node | .p => .p | .q => .q

structure State where
  core : ReasonReplay.State
  gate : Bool
  lease : Option (Bool × Mask)
  safe : Mask
  authority : Bool
  cuts : Mask
  episodeOpen : Bool
  forcedOpen : Bool
  harmP : Nat
  harmQ : Nat
deriving DecidableEq, Repr

def wrap (core : ReasonReplay.State) : State :=
  ⟨core,false,none,empty,true,empty,false,false,0,0⟩

def material (s : State) : Nat := ReasonReplay.material s.core + 2 * FormedSelection.bit s.gate
def energy (s : State) : Nat := ReasonReplay.energy s.core

def Valid (M : Nat) (s : State) : Prop := ReasonReplay.Valid M s.core ∧ material s ≤ M
instance (M : Nat) (s : State) : Decidable (Valid M s) := by unfold Valid; infer_instance

def debit (s : State) (cost : Nat) : ReasonReplay.State :=
  {s.core with record := ReasonReplay.debit s.core cost}

def required (s : State) (requested : Mask) : Mask :=
  if s.authority && s.core.delivery then difference requested s.cuts else empty

def preserveLease : ReasonReplay.Event → Bool
  | .setAccess _ | .setDelivery _ => true
  | _ => false

inductive Event where
  | core (a : ReasonReplay.Event)
  | assembleGate
  | beginEpisode
  | arm (requested : Mask)
  | safeguard (recipient : Patient)
  | release | releaseOpen | withdraw | refuse
  | privateWork
  | forceOpen
  | cut (targets : Mask)
  | setAuthority (available : Bool)
deriving DecidableEq, Repr

def Enabled (truth : Bool → Nat → Bool) (s : State) : Event → Prop
  | .core a => ReasonReplay.Enabled truth s.core a
  | .assembleGate => 1 ≤ s.core.record.plant.fuel ∧ s.gate = false ∧
      s.core.record.pending = .idle ∧ 1 ≤ s.core.record.plant.aFree ∧ 1 ≤ s.core.record.plant.hFree
  | .beginEpisode => s.episodeOpen = false ∧ s.core.record.pending = .idle
  | .arm G => 1 ≤ s.core.record.plant.fuel ∧ s.gate = true ∧ s.episodeOpen = true ∧
      s.forcedOpen = false ∧ s.lease = none ∧ s.authority = true ∧ s.core.delivery = true ∧ 0 < card G
  | .safeguard i => 1 ≤ s.core.record.plant.fuel ∧ s.gate = true ∧ s.episodeOpen = true ∧ member s.safe i = false
  | .release => 1 ≤ s.core.record.plant.fuel ∧ s.episodeOpen = true ∧
      match s.lease with
      | none => False
      | some (c,G) => c = s.core.context ∧ Covers s.safe (required s G)
  | .releaseOpen => 1 ≤ s.core.record.plant.fuel ∧ s.episodeOpen = true ∧ s.lease = none
  | .withdraw => s.episodeOpen = true ∧ s.forcedOpen = false
  | .refuse => s.episodeOpen = true
  | .privateWork => 1 ≤ s.core.record.plant.fuel ∧ s.episodeOpen = true ∧ s.core.record.pending = .idle
  | .forceOpen | .cut _ => s.episodeOpen = true
  | .setAuthority _ => True

def advance (g : ReasonReplay.Graph) (s : State) : Event → State
  | .core a => {s with core := ReasonReplay.advance g s.core a, lease := if preserveLease a then s.lease else none, safe := if preserveLease a then s.safe else empty}
  | .assembleGate => {s with gate := true, core := {s.core with record := {s.core.record with plant := {s.core.record.plant with aFree := s.core.record.plant.aFree-1, hFree := s.core.record.plant.hFree-1,fuel := s.core.record.plant.fuel-1}}}}
  | .beginEpisode => {s with episodeOpen := true, forcedOpen := false, cuts := empty, lease := none, safe := empty}
  | .arm G => {s with core := debit s 1, lease := some (s.core.context,G)}
  | .safeguard i => {s with core := debit s 1, safe := insert s.safe i}
  | .release | .releaseOpen => {s with core := debit s 1, episodeOpen := false, lease := none, safe := empty, harmP := s.harmP + FormedSelection.bit (!s.safe.p), harmQ := s.harmQ + FormedSelection.bit (!s.safe.q)}
  | .withdraw | .refuse => {s with episodeOpen := false, lease := none, safe := empty}
  | .privateWork => {s with core := debit s 1}
  | .forceOpen => {s with forcedOpen := true, lease := none}
  | .cut G => {s with cuts := union s.cuts G}
  | .setAuthority b => {s with authority := b}

def spending : Event → Nat
  | .core a => ReasonReplay.spending a
  | .assembleGate | .arm _ | .safeguard _ | .release | .releaseOpen | .privateWork => 1
  | _ => 0

def tally : List Event → Nat | [] => 0 | a::as => spending a + tally as

def Step (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool)
    (s : State) (a : Event) (t : State) : Prop := Valid M s ∧ Enabled truth s a ∧ t = advance g s a

def process (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) : Generative.Process State Event :=
  ⟨Step M g truth⟩
def Trace (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) := Generative.Trace (process M g truth)

instance (truth : Bool → Nat → Bool) (s : State) (a : Event) : Decidable (Enabled truth s a) := by
  cases s with
  | mk core gate lease safe authority cuts episodeOpen forcedOpen harmP harmQ =>
    cases lease with
    | none => cases a <;> unfold Enabled <;> infer_instance
    | some l =>
      rcases l with ⟨c,G⟩
      cases a <;> unfold Enabled <;> infer_instance

instance (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) (s t : State) (a : Event) :
    Decidable (Step M g truth s a t) := by unfold Step; infer_instance

def run (g : ReasonReplay.Graph) : State → List Event → State
  | s,[] => s
  | s,a::as => run g (advance g s a) as

def Runnable (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) : State → List Event → Prop
  | _,[] => True
  | s,a::as => Valid M s ∧ Enabled truth s a ∧ Runnable M g truth (advance g s a) as

def runnableDecidable (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) :
    (s : State) → (as : List Event) → Decidable (Runnable M g truth s as)
  | _,[] => isTrue trivial
  | s,a::as => by
    haveI : Decidable (Runnable M g truth (advance g s a) as) := runnableDecidable M g truth (advance g s a) as
    unfold Runnable; infer_instance
instance (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) (s : State) (as : List Event) :
    Decidable (Runnable M g truth s as) := runnableDecidable M g truth s as

theorem runnable_trace {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s : State} {as : List Event} (h : Runnable M g truth s as) : Trace M g truth s as (run g s as) := by
  induction as generalizing s with
  | nil => exact .nil _
  | cons a as ih => exact .cons ⟨h.1,h.2.1,rfl⟩ (ih h.2.2)

theorem trace_run {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (h : Trace M g truth s as t) : t = run g s as := by
  induction h with
  | nil => rfl
  | cons hs _ ih => rcases hs with ⟨_,_,rfl⟩; exact ih

theorem core_step_projects {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {a : ReasonReplay.Event} (h : Step M g truth s (.core a) t) :
    ReasonReplay.Step M g truth s.core a t.core := by
  rcases h with ⟨hv,he,rfl⟩
  exact ⟨hv.1,he,rfl⟩

theorem step_material {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {a : Event} (h : Step M g truth s a t) : material t = material s := by
  cases a with
  | core a =>
    have hm := ReasonReplay.step_material (core_step_projects h)
    rcases h with ⟨_,_,rfl⟩
    exact congrArg (fun n => n+2*FormedSelection.bit s.gate) hm
  | assembleGate =>
    rcases h with ⟨_,he,rfl⟩
    simp only [Enabled] at he
    simp only [material,advance,ReasonReplay.material,RecordedEvidence.materialUsed,
      FormedSelection.population,he.2.1,FormedSelection.bit]
    omega
  | beginEpisode | arm G | safeguard i | release | releaseOpen | withdraw | refuse | privateWork | forceOpen | cut G | setAuthority b =>
    rcases h with ⟨_,_,rfl⟩; rfl

theorem step_energy {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {a : Event} (h : Step M g truth s a t) : energy t + spending a = energy s := by
  cases a with
  | core a => exact ReasonReplay.step_energy (core_step_projects h)
  | assembleGate | arm G | safeguard i | release | releaseOpen | privateWork =>
    rcases h with ⟨_,he,rfl⟩
    have hf := he.1
    simp only [energy,advance,debit,ReasonReplay.energy,ReasonReplay.debit,
      RecordedEvidence.energy,FormedSelection.energy,spending]
    omega
  | beginEpisode | withdraw | refuse | forceOpen | cut G | setAuthority b =>
    rcases h with ⟨_,_,rfl⟩; rfl

theorem step_valid {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {a : Event} (h : Step M g truth s a t) : Valid M t := by
  have hm := step_material h
  have hv := h.1
  constructor
  · cases a with
    | core a => exact ReasonReplay.step_valid (core_step_projects h)
    | assembleGate =>
      rcases h with ⟨hv,he,rfl⟩
      rcases hv.1 with ⟨⟨hs,hesc,hmat⟩,hreader⟩
      simp only [ReasonReplay.Valid,advance,RecordedEvidence.Valid,ReasonReplay.material,
        RecordedEvidence.materialUsed,FormedSelection.population]
      refine ⟨⟨hs,hesc,?_⟩,?_⟩
      · simp only [RecordedEvidence.materialUsed,FormedSelection.population] at hmat
        omega
      · simp only [ReasonReplay.material,RecordedEvidence.materialUsed,FormedSelection.population] at hreader
        omega
    | beginEpisode | arm G | safeguard i | release | releaseOpen | withdraw | refuse | privateWork | forceOpen | cut G | setAuthority b =>
      rcases h with ⟨hv,_,rfl⟩; exact hv.1
  · rw [hm]; exact hv.2

theorem trace_energy {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (h : Trace M g truth s as t) : energy t + tally as = energy s := by
  induction h with
  | nil => simp [tally]
  | cons hs _ ih => have he := step_energy hs; simp only [tally]; omega

theorem trace_material {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (h : Trace M g truth s as t) : material t = material s := by
  induction h with
  | nil => rfl
  | cons hs _ ih => exact ih.trans (step_material hs)

theorem trace_valid {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (hv : Valid M s) (h : Trace M g truth s as t) : Valid M t := by
  induction h with
  | nil => exact hv
  | cons hs _ ih => exact ih (step_valid hs)

theorem step_authentic {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {a : Event} (hi : ReasonReplay.Authentic truth s.core)
    (h : Step M g truth s a t) : ReasonReplay.Authentic truth t.core := by
  cases a with
  | core a => exact ReasonReplay.step_authentic hi (core_step_projects h)
  | assembleGate | beginEpisode | arm G | safeguard i | release | releaseOpen | withdraw | refuse | privateWork | forceOpen | cut G | setAuthority b =>
    rcases h with ⟨_,_,rfl⟩; exact hi

theorem trace_authentic {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (hi : ReasonReplay.Authentic truth s.core)
    (h : Trace M g truth s as t) : ReasonReplay.Authentic truth t.core := by
  induction h with
  | nil => exact hi
  | cons hs _ ih => exact ih (step_authentic hi hs)

theorem core_segment_projects {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List ReasonReplay.Event} (h : Trace M g truth s (as.map Event.core) t) :
    ReasonReplay.Trace M g truth s.core as t.core := by
  induction as generalizing s with
  | nil => cases h; exact .nil _
  | cons a as ih =>
    cases h with
    | cons hs ht => exact .cons (core_step_projects hs) (ih ht)

theorem core_trace_lifts {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {r t : ReasonReplay.State} {as : List ReasonReplay.Event}
    (h : ReasonReplay.Trace M g truth r as t) (s : State) (he : s.core = r) (hv : Valid M s) :
    Trace M g truth s (as.map Event.core) (run g s (as.map Event.core)) := by
  induction h generalizing s with
  | nil => exact .nil _
  | cons hs _ ih =>
    have hstep : Step M g truth s (.core _) (advance g s (.core _)) :=
      ⟨hv,he ▸ hs.2.1,rfl⟩
    exact .cons hstep (ih _ (by simpa [advance,he] using hs.2.2.symm) (step_valid hstep))

theorem run_core_clean (g : ReasonReplay.Graph) (s : State) (as : List ReasonReplay.Event)
    (hl : s.lease = none) (hs : s.safe = empty) :
    run g s (as.map Event.core) = {s with core := ReasonReplay.run g s.core as} := by
  induction as generalizing s with
  | nil => rfl
  | cons a as ih =>
    have hl' : (advance g s (.core a)).lease = none := by simp [advance,hl]
    have hs' : (advance g s (.core a)).safe = empty := by simp [advance,hs]
    rw [List.map_cons,run,ih _ hl' hs']
    cases a <;> simp [advance,preserveLease,ReasonReplay.run,hl,hs]

def safeguards (G : Mask) : List Event :=
  (if G.p then [.safeguard .p] else []) ++ (if G.q then [.safeguard .q] else [])

def actionWord (G : Mask) : List Event :=
  if G = empty then [.releaseOpen] else [.arm G] ++ safeguards G ++ [.release]

def actionCost (G : Mask) : Nat := if G = empty then 1 else 2+card G

/-- All funds, control and unused opportunity conditions are physical premises;
this predicate neither declares a reason nor selects a morally right action. -/
def Fresh (M : Nat) (s : State) : Prop :=
  Valid M s ∧ s.gate = true ∧ s.episodeOpen = true ∧ s.forcedOpen = false ∧
  s.lease = none ∧ s.safe = empty ∧ s.authority = true ∧ s.cuts = empty ∧ s.core.delivery = true

instance (M : Nat) (s : State) : Decidable (Fresh M s) := by unfold Fresh; infer_instance

theorem action_cost_exact (G : Mask) : tally (actionWord G) = actionCost G := by
  rcases G with ⟨p,q⟩; cases p <;> cases q <;> decide

theorem action_run_core (g : ReasonReplay.Graph) (s : State) (G : Mask) :
    (run g s (actionWord G)).core = debit s (actionCost G) := by
  rcases G with ⟨p,q⟩; cases p <;> cases q <;>
    simp [run,actionWord,actionCost,safeguards,empty,card,advance,debit,
      ReasonReplay.debit,FormedSelection.bit,Nat.sub_sub]

theorem action_run_harms (g : ReasonReplay.Graph) (s : State) (G : Mask) (hs : s.safe = empty) :
    (run g s (actionWord G)).harmP = s.harmP + FormedSelection.bit (!G.p) ∧
    (run g s (actionWord G)).harmQ = s.harmQ + FormedSelection.bit (!G.q) ∧
    (run g s (actionWord G)).lease = none ∧ (run g s (actionWord G)).episodeOpen = false := by
  rcases G with ⟨p,q⟩; cases p <;> cases q <;>
    simp [run,actionWord,safeguards,empty,advance,insert,hs]

theorem action_feasible_iff {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s : State} (hf : Fresh M s) (G : Mask) :
    (∃ t, Trace M g truth s (actionWord G) t) ↔ actionCost G ≤ s.core.record.plant.fuel := by
  constructor
  · rintro ⟨t,ht⟩
    have he := trace_energy ht
    rw [trace_run ht,action_cost_exact] at he
    simp only [energy,action_run_core,debit,ReasonReplay.debit,ReasonReplay.energy,
      RecordedEvidence.energy,FormedSelection.energy] at he
    omega
  · intro hfund
    refine ⟨run g s (actionWord G),runnable_trace ?_⟩
    rcases hf with ⟨⟨⟨⟨hslots,hesc,hrec⟩,hreader⟩,hmat⟩,hgate,hopen,hforce,hlease,hsafe,hauth,hcuts,hdel⟩
    rcases G with ⟨p,q⟩; cases p <;> cases q <;>
      simp [Runnable,actionWord,actionCost,safeguards,Enabled,advance,Valid,ReasonReplay.Valid,
        RecordedEvidence.Valid,material,ReasonReplay.material,RecordedEvidence.materialUsed,
        FormedSelection.population,FormedSelection.bit,debit,ReasonReplay.debit,empty,card,member,
        insert,required,difference,Covers,hgate,hopen,hforce,hlease,hsafe,hauth,hcuts,hdel,
        hslots,hesc,Nat.sub_sub] at * <;> omega

theorem protected_action_has_no_new_admitted_harm {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {G I : Mask} (hf : Fresh M s) (hcover : Covers G I)
    (h : Trace M g truth s (actionWord G) t) :
    (I.p = true → t.harmP = s.harmP) ∧ (I.q = true → t.harmQ = s.harmQ) := by
  have ha := action_run_harms g s G hf.2.2.2.2.2.1
  rw [←trace_run h] at ha
  constructor
  · intro hp
    have hg := hcover.1 hp
    simpa [hg,FormedSelection.bit] using ha.1
  · intro hq
    have hg := hcover.2 hq
    simpa [hg,FormedSelection.bit] using ha.2.1

/-- A cut disables control without erasing the reader's grounds or actual
safeguards. Its financial feasibility belongs to the external game. -/
theorem cut_does_not_refute_or_erase (g : ReasonReplay.Graph) (s : State) (G : Mask) :
    (advance g s (.cut G)).core = s.core ∧ (advance g s (.cut G)).safe = s.safe := ⟨rfl,rfl⟩

theorem force_does_not_erase_actual_safeguards (g : ReasonReplay.Graph) (s : State) :
    (advance g s .forceOpen).safe = s.safe ∧ (advance g s .forceOpen).core = s.core ∧
    (advance g s .forceOpen).lease = none := ⟨rfl,rfl,rfl⟩

theorem withdrawal_consumes_opportunity (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) (s : State) :
    ¬ Enabled truth (advance g s .withdraw) .releaseOpen ∧
    ¬ Enabled truth (advance g s .withdraw) .release := by
  simp [Enabled,advance]

theorem run_append (g : ReasonReplay.Graph) (s : State) (as bs : List Event) :
    run g s (as++bs) = run g (run g s as) bs := by
  induction as generalizing s with
  | nil => rfl
  | cons a as ih => exact ih _

def auditWord : List Event := ReasonReplay.auditEvents.map Event.core

theorem audit_tally : tally auditWord = 11 := by decide

theorem audit_core_projection (g : ReasonReplay.Graph) (s : State) :
    (run g s auditWord).core = ReasonReplay.run g s.core ReasonReplay.auditEvents := by
  simp only [auditWord,ReasonReplay.auditEvents,List.map_cons,List.map_nil,run,advance,ReasonReplay.run]

theorem audit_then_action_fuel (g : ReasonReplay.Graph) (s : State) (G : Mask) :
    (run g s (auditWord++actionWord G)).core.record.plant.fuel =
      s.core.record.plant.fuel - (11+actionCost G) := by
  rw [run_append]
  simp only [action_run_core,debit,ReasonReplay.debit,audit_core_projection]
  have h : (ReasonReplay.run g s.core ReasonReplay.auditEvents).record.plant.fuel = s.core.record.plant.fuel-11 := by
    simp [ReasonReplay.run,ReasonReplay.auditEvents,ReasonReplay.advance,ReasonReplay.debit,ReasonReplay.pathCost,Nat.sub_sub]
  rw [h,Nat.sub_sub]

theorem audit_then_action_energy (g : ReasonReplay.Graph) (s : State) (G : Mask) :
    energy (run g s (auditWord++actionWord G)) + (11+actionCost G) =
      energy s + ((11+actionCost G)-s.core.record.plant.fuel) := by
  rw [run_append]
  simp only [energy,action_run_core,debit,ReasonReplay.debit,audit_core_projection,
    ReasonReplay.energy,RecordedEvidence.energy,FormedSelection.energy]
  simp [ReasonReplay.run,ReasonReplay.auditEvents,ReasonReplay.advance,ReasonReplay.debit,
    ReasonReplay.pathCost,Nat.sub_sub]
  omega

theorem tally_append (as bs : List Event) : tally (as++bs) = tally as+tally bs := by
  induction as with
  | nil => simp [tally]
  | cons a as ih => simp only [List.cons_append,tally,ih]; omega

/-- Exact feasibility of the fixed paid audit followed by the actual full-mask
actuation word. Empty protection uses open release rather than a phantom arm. -/
theorem audit_and_action_feasible_iff {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s : State} (hf : Fresh M s) (hphase : s.core.phase = 0) (hr : s.core.reader = true)
    (hidle : s.core.record.pending = .idle) (haccess : s.core.access = true) (G : Mask) :
    (∃ t, Trace M g truth s (auditWord++actionWord G) t) ↔
      11+actionCost G ≤ s.core.record.plant.fuel := by
  constructor
  · rintro ⟨t,ht⟩
    have he := trace_energy ht
    rw [trace_run ht,tally_append,audit_tally,action_cost_exact] at he
    have hc := audit_then_action_energy g s G
    omega
  · intro hfund
    refine ⟨run g s (auditWord++actionWord G),runnable_trace ?_⟩
    rcases hf with ⟨⟨⟨⟨hslots,hesc,hrec⟩,hreader⟩,hmat⟩,hgate,hopen,hforce,hlease,hsafe,hauth,hcuts,hdel⟩
    rcases G with ⟨p,q⟩; cases p <;> cases q <;>
      simp [Runnable,auditWord,ReasonReplay.auditEvents,actionWord,actionCost,safeguards,
        Enabled,advance,preserveLease,Valid,ReasonReplay.Valid,RecordedEvidence.Valid,
        ReasonReplay.Enabled,ReasonReplay.advance,ReasonReplay.debit,ReasonReplay.pathIndex,ReasonReplay.pathCost,
        material,ReasonReplay.material,RecordedEvidence.materialUsed,FormedSelection.population,
        FormedSelection.bit,debit,empty,card,member,insert,required,difference,Covers,
        hgate,hopen,hforce,hlease,hsafe,hauth,hcuts,hdel,hphase,hr,hidle,haccess,
        hslots,hesc,Nat.sub_sub] at * <;> omega

/-- The semantic claim uses a real completed audit and authentic precursor,
not an arbitrary state carrying a convincing publication tag. Permission to
perform this action remains an independent premise and is retained explicitly. -/
theorem reached_reason_and_protection {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {r s t : State} {I G : Mask}
    (hauth : ReasonReplay.Authentic truth r.core)
    (haudit : Trace M g truth r auditWord s)
    (hpub : s.core.installed = some (r.core.context,I))
    (hf : Fresh M s) (hcover : Covers G I)
    (hact : Trace M g truth s (actionWord G) t)
    (Fact : Nat → Prop) (Reason : ReasonReplay.Node → Prop) (anchor : Reason .root)
    (calibrated : ∀ i, i < 3 → truth r.core.context i = true → Fact i)
    (relevant : ∀ i, i < 3 → Fact i → Reason (ReasonReplay.endpoints g i).1 → Reason (ReasonReplay.endpoints g i).2)
    (Permissible : Mask → Prop) (permission : Permissible G) :
    Permissible G ∧
    (I.p = true → Reason .p ∧ t.harmP = s.harmP) ∧
    (I.q = true → Reason .q ∧ t.harmQ = s.harmQ) := by
  have hreader := core_segment_projects haudit
  have hnoharm := protected_action_has_no_new_admitted_harm hf hcover hact
  refine ⟨permission,?_,?_⟩
  · intro hp
    refine ⟨?_,hnoharm.1 hp⟩
    exact ReasonReplay.paid_recorded_reason_sound hauth (Generative.Trace.nil _) hreader Fact Reason anchor calibrated relevant hpub hp
  · intro hq
    refine ⟨?_,hnoharm.2 hq⟩
    exact ReasonReplay.paid_recorded_reason_sound hauth (Generative.Trace.nil _) hreader Fact Reason anchor calibrated relevant hpub hq

inductive Stage where | formation (s : FormedSelection.State) | operation (s : State)
deriving DecidableEq, Repr
inductive StageEvent where | formation (a : FormedSelection.Event) | handoff | operation (a : Event)
deriving DecidableEq, Repr

def StagedStep (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) : Stage → StageEvent → Stage → Prop
  | .formation s,.formation a,.formation t => FormedSelection.Step M s a t
  | .formation s,.handoff,.operation t => FormedSelection.Valid M s ∧ t = wrap (ReasonReplay.handoff s)
  | .operation s,.operation a,.operation t => Step M g truth s a t
  | _,_,_ => False

def stagedProcess (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) : Generative.Process Stage StageEvent :=
  ⟨StagedStep M g truth⟩
def StagedTrace (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) := Generative.Trace (stagedProcess M g truth)

theorem formation_trace_embeds {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : FormedSelection.State} {as : List FormedSelection.Event} (h : FormedSelection.Trace M s as t) :
    StagedTrace M g truth (.formation s) (as.map StageEvent.formation) (.formation t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih => exact Generative.Trace.cons (m := Stage.formation u) hs ih

theorem operation_trace_embeds {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (h : Trace M g truth s as t) :
    StagedTrace M g truth (.operation s) (as.map StageEvent.operation) (.operation t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih => exact Generative.Trace.cons (m := Stage.operation u) hs ih

theorem compose_actual_state {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s u : FormedSelection.State} {t : State} {as : List FormedSelection.Event} {bs : List Event}
    (hv : FormedSelection.Valid M s) (hp : FormedSelection.Trace M s as u)
    (ho : Trace M g truth (wrap (ReasonReplay.handoff u)) bs t) :
    StagedTrace M g truth (.formation s)
      (as.map StageEvent.formation ++ .handoff :: bs.map StageEvent.operation) (.operation t) := by
  apply Generative.trace_append_iff.mpr
  refine ⟨.formation u,formation_trace_embeds hp,?_⟩
  apply Generative.Trace.cons (m := .operation (wrap (ReasonReplay.handoff u)))
  · exact ⟨FormedSelection.trace_valid hv hp,rfl⟩
  · exact operation_trace_embeds ho

def primary := ReasonReplay.primary
def truth := ReasonReplay.truth
def initial : FormedSelection.State := ⟨0,0,.empty,false,false,83,20⟩
def prepared : FormedSelection.State := ⟨8,8,.active,true,false,64,20⟩
def formationEvents : List FormedSelection.Event :=
  [.formH,.formH,.formH,.formH,.formH,.formH,.formH,.formH,
   .formA,.formA,.formA,.formA,.formA,.formA,.formA,.formA,.formA,.associateA,.repair]

theorem actual_part_preparation : FormedSelection.Trace 17 initial formationEvents prepared := by
  apply FormedSelection.Trace.cons (u := ⟨0,1,.empty,false,false,82,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,2,.empty,false,false,81,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,3,.empty,false,false,80,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,4,.empty,false,false,79,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,5,.empty,false,false,78,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,6,.empty,false,false,77,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,7,.empty,false,false,76,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,8,.empty,false,false,75,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1,8,.empty,false,false,74,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨2,8,.empty,false,false,73,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨3,8,.empty,false,false,72,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨4,8,.empty,false,false,71,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨5,8,.empty,false,false,70,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨6,8,.empty,false,false,69,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨7,8,.empty,false,false,68,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨8,8,.empty,false,false,67,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨9,8,.empty,false,false,66,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨8,8,.active,false,false,65,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := prepared) (by decide)
  exact .nil _

def apparatusEvents : List Event := ReasonReplay.apparatusEvents.map Event.core ++ [.assembleGate]
def ready := run primary (wrap (ReasonReplay.handoff prepared)) apparatusEvents
def firstBeforeAuditEvents : List Event := [.beginEpisode] ++ ReasonReplay.firstRecordEvents.map Event.core
def firstBeforeAudit := run primary ready firstBeforeAuditEvents
def firstPublished := run primary firstBeforeAudit auditWord
def firstFinal := run primary firstPublished (actionWord full)
def secondBeforeAuditEvents : List Event := [.beginEpisode,.core (.changeContext true)] ++ ReasonReplay.secondRecordEvents.map Event.core
def secondBeforeAudit := run primary firstFinal secondBeforeAuditEvents
def secondPublished := run primary secondBeforeAudit auditWord
def qOnly : Mask := ⟨false,true⟩
def secondFinal := run primary secondPublished (actionWord qOnly)
def thirdBeforeAuditEvents : List Event := [.beginEpisode,.core .turnover]
def thirdBeforeAudit := run primary secondFinal thirdBeforeAuditEvents
def thirdPublished := run primary thirdBeforeAudit auditWord
def final := run primary thirdPublished (actionWord qOnly)

def fullEvents := apparatusEvents ++ firstBeforeAuditEvents ++ auditWord ++ actionWord full ++
  secondBeforeAuditEvents ++ auditWord ++ actionWord qOnly ++ thirdBeforeAuditEvents ++ auditWord ++ actionWord qOnly

theorem actual_apparatus : Trace 17 primary truth (wrap (ReasonReplay.handoff prepared)) apparatusEvents ready :=
  runnable_trace (by decide)

theorem reader_projection_is_exact : ready.core = ReasonReplay.ready ∧ material ready = 17 ∧ ready.gate = true := by decide

theorem actual_first_audit : Trace 17 primary truth firstBeforeAudit auditWord firstPublished := runnable_trace (by decide)
theorem actual_first_action : Trace 17 primary truth firstPublished (actionWord full) firstFinal := runnable_trace (by decide)
theorem actual_revised_audit : Trace 17 primary truth secondBeforeAudit auditWord secondPublished := runnable_trace (by decide)
theorem actual_revised_action : Trace 17 primary truth secondPublished (actionWord qOnly) secondFinal := runnable_trace (by decide)
theorem actual_successor_audit : Trace 17 primary truth thirdBeforeAudit auditWord thirdPublished := runnable_trace (by decide)
theorem actual_successor_action : Trace 17 primary truth thirdPublished (actionWord qOnly) final := runnable_trace (by decide)

theorem full_history : Trace 17 primary truth (wrap (ReasonReplay.handoff prepared)) fullEvents final := runnable_trace (by decide)

theorem actual_construction_revision_and_protection :
    StagedTrace 17 primary truth (.formation initial)
      (formationEvents.map StageEvent.formation ++ .handoff :: fullEvents.map StageEvent.operation) (.operation final) :=
  compose_actual_state (by decide) actual_part_preparation full_history

theorem complete_material_energy_and_harm_account :
    FormedSelection.Absent initial ∧ FormedSelection.energy initial = 103 ∧
    FormedSelection.tally FormedSelection.expenditure formationEvents = 19 ∧
    tally apparatusEvents = 8 ∧ tally auditWord = 11 ∧
    actionCost full = 4 ∧ actionCost qOnly = 3 ∧
    final.core.record.plant.fuel = 3 ∧ final.core.record.plant.source = 18 ∧
    material final = 17 ∧ energy final = 21 ∧ final.harmP = 2 ∧ final.harmQ = 0 ∧
    final.core.record.records = [true,true,true,false,true,true] ∧
    FormedSelection.energy initial = 19+6+1+1+12+33+10+energy final := by
  unfold FormedSelection.Absent
  decide

theorem actual_retraction_keeps_harm_visible :
    firstPublished.core.installed = some (false,full) ∧
    secondPublished.core.installed = some (true,qOnly) ∧ thirdPublished.core.installed = some (true,qOnly) ∧
    firstFinal.harmP = 0 ∧ firstFinal.harmQ = 0 ∧
    secondFinal.harmP = 1 ∧ secondFinal.harmQ = 0 ∧
    final.harmP = 2 ∧ final.harmQ = 0 := by decide

theorem actual_archive_authentic : ReasonReplay.Authentic truth final.core :=
  trace_authentic (ReasonReplay.handoff_authentic truth prepared) full_history

def freshFinal : State := advance primary (advance primary final .beginEpisode) (.core (.changeContext true))

theorem original_hardware_has_no_actuator_pair :
    ¬ Enabled truth (wrap ReasonReplay.final) .assembleGate := by decide

theorem reasons_remain_when_next_audit_unfunded :
    freshFinal.core.installed = some (true,qOnly) ∧ freshFinal.core.record.plant.fuel = 3 ∧
    freshFinal.core.record.plant.source = 18 ∧ Fresh 17 freshFinal ∧
    freshFinal.core.phase = 0 ∧ freshFinal.core.reader = true ∧
    freshFinal.core.record.pending = .idle ∧ freshFinal.core.access = true ∧
    ¬ ∃ t, Trace 17 primary truth freshFinal auditWord t := by
  refine ⟨by decide,by decide,by decide,by decide,by decide,by decide,by decide,by decide,?_⟩
  rintro ⟨t,ht⟩
  have he := (ReasonReplay.paid_audit_installs_exact_closure (core_segment_projects ht)).2.2
  have hf : freshFinal.core.record.plant.fuel = 3 := by decide
  rw [hf] at he
  omega

/-- A delivery cut leaves the actual installed reasons and lease while allowing
an unprotected release through the disabled interlock. All harms remain recorded. -/
def armedBoth := advance primary firstPublished (.arm full)
def deliveryCut := advance primary armedBoth (.core (.setDelivery false))
def unsafeReleased := advance primary deliveryCut .release

theorem actual_delivery_cut_preserves_reasons_but_allows_harm :
    Step 17 primary truth firstPublished (.arm full) armedBoth ∧
    Step 17 primary truth armedBoth (.core (.setDelivery false)) deliveryCut ∧
    Step 17 primary truth deliveryCut .release unsafeReleased ∧
    deliveryCut.core.installed = firstPublished.core.installed ∧
    unsafeReleased.harmP = 1 ∧ unsafeReleased.harmQ = 1 := by decide

def resetAfterArm := advance primary armedBoth (.core (.changeContext false))
theorem same_context_reset_cancels_lease_keeps_bill :
    resetAfterArm.lease = none ∧ resetAfterArm.core.record.plant.fuel + 1 = firstPublished.core.record.plant.fuel ∧
    resetAfterArm.core.installed = firstPublished.core.installed ∧
    ¬ Enabled truth resetAfterArm .release := by decide

theorem unaudited_voluntary_protection_is_possible :
    ∃ t, Trace 17 primary truth (advance primary ready .beginEpisode) (actionWord full) t :=
  ⟨_,runnable_trace (by decide)⟩

theorem no_gate_still_allows_open_production :
    Enabled truth (advance primary (wrap ReasonReplay.ready) .beginEpisode) .releaseOpen ∧
    ¬ Enabled truth (advance primary (wrap ReasonReplay.ready) .beginEpisode) (.arm full) := by decide

/-- The prescribed armed-word mask in this threshold is computed from the actual currently available
retained evidence. Its factual and normative adequacy remain separate. -/
theorem audit_full_protection_feasible_iff {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s : State} (hf : Fresh M s) (hphase : s.core.phase = 0) (hr : s.core.reader = true)
    (hidle : s.core.record.pending = .idle) (haccess : s.core.access = true) :
    let I := ReasonReplay.closureMask g (ReasonReplay.decodedAt s.core.context s.core.record.records)
    (∃ t, Trace M g truth s (auditWord++actionWord I) t) ↔
      11+actionCost I ≤ s.core.record.plant.fuel :=
  audit_and_action_feasible_iff hf hphase hr hidle haccess _

theorem actual_final_reopen_preserves_ground_and_is_enabled :
    Step 17 primary truth final .beginEpisode (advance primary final .beginEpisode) ∧
    Step 17 primary truth (advance primary final .beginEpisode) (.core (.changeContext true)) freshFinal ∧
    freshFinal.core.record = final.core.record ∧ freshFinal.core.installed = final.core.installed := by decide

/-- Intact enforcement rules out harmful releases for every leased recipient,
even when the operator chooses a different feasible safeguard sequence. -/
theorem enforced_release_protects_requested {M : Nat} {g : ReasonReplay.Graph} {truth : Bool → Nat → Bool}
    {s t : State} {c : Bool} {G : Mask}
    (h : Step M g truth s .release t) (hl : s.lease = some (c,G))
    (ha : s.authority = true) (hd : s.core.delivery = true) (hc : s.cuts = empty) :
    (G.p = true → t.harmP = s.harmP) ∧ (G.q = true → t.harmQ = s.harmQ) := by
  rcases h with ⟨_,he,rfl⟩
  simp only [Enabled,hl] at he
  have hcover : Covers s.safe G := by
    simpa [required,ha,hd,hc,difference,empty] using he.2.2.2
  constructor
  · intro hp
    have hs := hcover.1 hp
    simp [advance,hs,FormedSelection.bit]
  · intro hq
    have hs := hcover.2 hq
    simp [advance,hs,FormedSelection.bit]

theorem release_consumes_its_opportunity (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) (s : State) :
    ¬ Enabled truth (advance g s .release) .release ∧
    ¬ Enabled truth (advance g s .release) .releaseOpen ∧
    (advance g s .release).lease = none := by
  simp [Enabled,advance]

/-- Review boundary: fourteen is the price of audit plus the prescribed armed
q word, not the least fuel for every way to protect q. Four real private-work
steps put an actual continuing predecessor exactly at the separating budget. -/
def voluntaryPreparation : List Event := [.privateWork,.privateWork,.privateWork,.privateWork]
def voluntaryStart := run primary thirdBeforeAudit voluntaryPreparation

def voluntaryPrefix := apparatusEvents ++ firstBeforeAuditEvents ++ auditWord ++ actionWord full ++
  secondBeforeAuditEvents ++ auditWord ++ actionWord qOnly ++ thirdBeforeAuditEvents ++ voluntaryPreparation

def voluntaryWord : List Event := auditWord ++ [.safeguard .q,.releaseOpen]
def voluntaryFinal := run primary voluntaryStart voluntaryWord

theorem actual_predecessor_for_voluntary_boundary :
    Trace 17 primary truth (wrap (ReasonReplay.handoff prepared)) voluntaryPrefix voluntaryStart :=
  runnable_trace (by decide)

theorem voluntary_protection_is_strictly_cheaper_than_armed_word :
    Trace 17 primary truth voluntaryStart voluntaryWord voluntaryFinal ∧
    voluntaryStart.core.record.plant.fuel = 13 ∧ Fresh 17 voluntaryStart ∧
    voluntaryFinal.core.record.plant.fuel = 0 ∧ voluntaryFinal.core.record.plant.source = 18 ∧
    voluntaryFinal.harmP = 2 ∧ voluntaryFinal.harmQ = 0 ∧ material voluntaryFinal = 17 ∧
    energy voluntaryFinal + 13 = energy voluntaryStart ∧
    FormedSelection.energy initial = 19+8+12+33+7+4+2+energy voluntaryFinal ∧
    ¬ ∃ t, Trace 17 primary truth voluntaryStart (auditWord++actionWord qOnly) t := by
  refine ⟨runnable_trace (by decide),by decide,by decide,by decide,by decide,
    by decide,by decide,by decide,by decide,by decide,?_⟩
  intro h
  have hf := (audit_and_action_feasible_iff (M := 17) (g := primary) (truth := truth)
    (s := voluntaryStart) (by decide) (by decide) (by decide) (by decide) (by decide) qOnly).mp h
  have hstart : voluntaryStart.core.record.plant.fuel = 13 := by decide
  have hcost : actionCost qOnly = 3 := by decide
  rw [hstart,hcost] at hf
  omega

end ReasonProtection

#print axioms ReasonProtection.covers_self
#print axioms ReasonProtection.covers_trans
#print axioms ReasonProtection.runnable_trace
#print axioms ReasonProtection.trace_run
#print axioms ReasonProtection.core_step_projects
#print axioms ReasonProtection.step_material
#print axioms ReasonProtection.step_energy
#print axioms ReasonProtection.step_valid
#print axioms ReasonProtection.trace_energy
#print axioms ReasonProtection.trace_material
#print axioms ReasonProtection.trace_valid
#print axioms ReasonProtection.step_authentic
#print axioms ReasonProtection.trace_authentic
#print axioms ReasonProtection.core_segment_projects
#print axioms ReasonProtection.core_trace_lifts
#print axioms ReasonProtection.run_core_clean
#print axioms ReasonProtection.action_cost_exact
#print axioms ReasonProtection.action_run_core
#print axioms ReasonProtection.action_run_harms
#print axioms ReasonProtection.action_feasible_iff
#print axioms ReasonProtection.protected_action_has_no_new_admitted_harm
#print axioms ReasonProtection.cut_does_not_refute_or_erase
#print axioms ReasonProtection.force_does_not_erase_actual_safeguards
#print axioms ReasonProtection.withdrawal_consumes_opportunity
#print axioms ReasonProtection.run_append
#print axioms ReasonProtection.audit_tally
#print axioms ReasonProtection.audit_core_projection
#print axioms ReasonProtection.audit_then_action_fuel
#print axioms ReasonProtection.audit_then_action_energy
#print axioms ReasonProtection.tally_append
#print axioms ReasonProtection.audit_and_action_feasible_iff
#print axioms ReasonProtection.reached_reason_and_protection
#print axioms ReasonProtection.formation_trace_embeds
#print axioms ReasonProtection.operation_trace_embeds
#print axioms ReasonProtection.compose_actual_state
#print axioms ReasonProtection.actual_part_preparation
#print axioms ReasonProtection.actual_apparatus
#print axioms ReasonProtection.reader_projection_is_exact
#print axioms ReasonProtection.actual_first_audit
#print axioms ReasonProtection.actual_first_action
#print axioms ReasonProtection.actual_revised_audit
#print axioms ReasonProtection.actual_revised_action
#print axioms ReasonProtection.actual_successor_audit
#print axioms ReasonProtection.actual_successor_action
#print axioms ReasonProtection.full_history
#print axioms ReasonProtection.actual_construction_revision_and_protection
#print axioms ReasonProtection.complete_material_energy_and_harm_account
#print axioms ReasonProtection.actual_retraction_keeps_harm_visible
#print axioms ReasonProtection.actual_archive_authentic
#print axioms ReasonProtection.original_hardware_has_no_actuator_pair
#print axioms ReasonProtection.reasons_remain_when_next_audit_unfunded
#print axioms ReasonProtection.actual_delivery_cut_preserves_reasons_but_allows_harm
#print axioms ReasonProtection.same_context_reset_cancels_lease_keeps_bill
#print axioms ReasonProtection.unaudited_voluntary_protection_is_possible
#print axioms ReasonProtection.no_gate_still_allows_open_production
#print axioms ReasonProtection.audit_full_protection_feasible_iff
#print axioms ReasonProtection.actual_final_reopen_preserves_ground_and_is_enabled
#print axioms ReasonProtection.enforced_release_protects_requested
#print axioms ReasonProtection.release_consumes_its_opportunity
#print axioms ReasonProtection.actual_predecessor_for_voluntary_boundary
#print axioms ReasonProtection.voluntary_protection_is_strictly_cheaper_than_armed_word
