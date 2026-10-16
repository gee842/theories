import RecordedEvidence

/-!
A finite three-node contextual reason interface. Query positions are bound to
edge/context pairs before outcomes. Recorded truth and reason relevance remain
separate calibrated-assay and semantic premises. The reader is a paid finite
circuit, made from a spare A/H pair. Its declared capacity/wiring is not derived
from counting parts. Three audits in one witness reuse that physical circuit.
-/
namespace ReasonReplay

set_option maxHeartbeats 2000000
set_option maxRecDepth 8192

inductive Node where
  | root | p | q
deriving DecidableEq, Repr

structure Graph where
  e0 : Node × Node
  e1 : Node × Node
  e2 : Node × Node
deriving DecidableEq, Repr

structure Mask where
  p : Bool
  q : Bool
deriving DecidableEq, Repr

def emptyMask : Mask := ⟨false,false⟩
def Mask.has (m : Mask) : Node → Prop
  | .root => True
  | .p => m.p = true
  | .q => m.q = true

inductive Path where
  | directP | directQ | viaP | viaQ
deriving DecidableEq, Repr

def paths : List Path := [.directP,.directQ,.viaP,.viaQ]
def pathIndex : Path → Nat | .directP => 0 | .directQ => 1 | .viaP => 2 | .viaQ => 3
def pathCost : Path → Nat | .directP | .directQ => 1 | .viaP | .viaQ => 2
def endpoint : Path → Node | .directP | .viaQ => .p | .directQ | .viaP => .q

def positive (x : Option Bool) : Bool := x == some true

def edge (g : Graph) (certs : List (Option Bool)) (u v : Node) : Bool :=
  ((g.e0 == (u,v)) && positive (certs.getD 0 none)) ||
  ((g.e1 == (u,v)) && positive (certs.getD 1 none)) ||
  ((g.e2 == (u,v)) && positive (certs.getD 2 none))

def pathValid (g : Graph) (certs : List (Option Bool)) : Path → Bool
  | .directP => edge g certs .root .p
  | .directQ => edge g certs .root .q
  | .viaP => edge g certs .root .p && edge g certs .p .q
  | .viaQ => edge g certs .root .q && edge g certs .q .p

def applyPath (g : Graph) (certs : List (Option Bool)) (m : Mask) (path : Path) : Mask :=
  match endpoint path with
  | .p => {m with p := m.p || pathValid g certs path}
  | .q => {m with q := m.q || pathValid g certs path}
  | .root => m

def closureMask (g : Graph) (certs : List (Option Bool)) : Mask :=
  paths.foldl (applyPath g certs) emptyMask

inductive Rooted (E : Node → Node → Prop) : Node → Prop where
  | root : Rooted E .root
  | next {u v : Node} : Rooted E u → E u v → Rooted E v

def supported (E : Node → Node → Prop) : Node → Prop
  | .root => True
  | .p => E .root .p ∨ (E .root .q ∧ E .q .p)
  | .q => E .root .q ∨ (E .root .p ∧ E .p .q)

theorem supported_closed {E : Node → Node → Prop} {u v : Node}
    (hu : supported E u) (he : E u v) : supported E v := by
  cases u <;> cases v
  · trivial
  · exact Or.inl he
  · exact Or.inl he
  · trivial
  · exact hu
  · exact hu.elim (fun h => Or.inr ⟨h,he⟩) (fun h => Or.inl h.1)
  · trivial
  · exact hu.elim (fun h => Or.inr ⟨h,he⟩) (fun h => Or.inl h.1)
  · exact hu

/-- All root-reachable nodes in this three-node domain have one of four paths. -/
theorem rooted_iff_supported (E : Node → Node → Prop) (v : Node) :
    Rooted E v ↔ supported E v := by
  constructor
  · intro h
    induction h with
    | root => trivial
    | next _ he ih => exact supported_closed ih he
  · intro h
    cases v with
    | root => exact .root
    | p =>
      exact h.elim (fun he => Rooted.next Rooted.root he)
        (fun he => Rooted.next (Rooted.next Rooted.root he.1) he.2)
    | q =>
      exact h.elim (fun he => Rooted.next Rooted.root he)
        (fun he => Rooted.next (Rooted.next Rooted.root he.1) he.2)

theorem closure_exact (g : Graph) (certs : List (Option Bool)) (v : Node) :
    (closureMask g certs).has v ↔ Rooted (fun u v => edge g certs u v = true) v := by
  rw [rooted_iff_supported]
  cases v <;>
    cases h0 : edge g certs .root .p <;>
    cases h1 : edge g certs .root .q <;>
    cases h2 : edge g certs .p .q <;>
    cases h3 : edge g certs .q .p <;>
    simp [closureMask, paths, emptyMask, applyPath, endpoint, pathValid, Mask.has,
      supported, h0,h1,h2,h3]

theorem rooted_semantic_sound {E : Node → Node → Prop} {Reason : Node → Prop}
    (anchor : Reason .root) (relevant : ∀ u v, E u v → Reason u → Reason v)
    {v : Node} (h : Rooted E v) : Reason v := by
  induction h with
  | root => exact anchor
  | next _ he ih => exact relevant _ _ he ih

/-- Decoder bytes have no implicit ethical meaning. This implication is supplied. -/
theorem closure_semantic_sound (g : Graph) (certs : List (Option Bool))
    (Reason : Node → Prop) (anchor : Reason .root)
    (relevant : ∀ u v, edge g certs u v = true → Reason u → Reason v)
    {v : Node} (h : (closureMask g certs).has v) : Reason v :=
  rooted_semantic_sound anchor relevant ((closure_exact g certs v).mp h)

/-- Fixed positions 0..2 concern context false; 3..5 concern context true. -/
def queryContext (index : Nat) : Bool := decide (3 ≤ index)
def queryEdge (index : Nat) : Nat := index % 3

def decodeAt (context : Bool) (records : List Bool) (index : Nat) : Option Bool :=
  if index < 3 then records[(if context then 3 else 0) + index]? else none

def decodedAt (context : Bool) (records : List Bool) : List (Option Bool) :=
  [decodeAt context records 0, decodeAt context records 1, decodeAt context records 2]

def Assayed (truth : Bool → Nat → Bool) (records : List Bool) : Prop :=
  ∀ index bit, records[index]? = some bit → index < 6 ∧
    bit = truth (queryContext index) (queryEdge index)

theorem current_decode_sound {truth : Bool → Nat → Bool} {records : List Bool}
    (ha : Assayed truth records) (context : Bool) (index : Nat) (hi : index < 3)
    (bit : Bool) (h : decodeAt context records index = some bit) : bit = truth context index := by
  simp only [decodeAt, if_pos hi] at h
  have hh := (ha _ _ h).2
  cases context <;> simp only [Bool.false_eq_true, if_false, if_true, Nat.zero_add] at hh
  · have hq : queryContext index = false := by simp [queryContext]; omega
    have he : queryEdge index = index := Nat.mod_eq_of_lt hi
    simpa [hq,he] using hh
  · have hq : queryContext (3+index) = true := by simp [queryContext]
    have he : queryEdge (3+index) = index := by unfold queryEdge; omega
    simpa [hq,he] using hh

theorem missing_is_not_negative (context : Bool) (index : Nat) :
    decodeAt context [] index ≠ some false ∧ decodeAt context [] index ≠ some true := by
  simp [decodeAt]

/-- Completeness of the actual retained word transports the explicit assay premise. -/
theorem recorded_word_supplies_assay {M : Nat} {s t : RecordedEvidence.State}
    {events : List RecordedEvidence.Event} {truth : Bool → Nat → Bool}
    (ht : Generative.Trace (RecordedEvidence.process M) s events t)
    (hs : s.pending = .idle) (he : t.pending = .idle)
    (ha : Assayed truth (s.records ++ RecordedEvidence.word events)) : Assayed truth t.records := by
  rw [RecordedEvidence.complete_record ht hs he]
  exact ha

structure State where
  record : RecordedEvidence.State
  reader : Bool
  context : Bool
  phase : Nat
  sensed : Option Bool
  decoded : List (Option Bool)
  working : Mask
  installed : Option (Bool × Mask)
  access : Bool
  delivery : Bool
deriving DecidableEq, Repr

def handoff (s : FormedSelection.State) : State :=
  ⟨RecordedEvidence.handoff s,false,false,0,none,[],emptyMask,none,true,true⟩

def material (s : State) : Nat := RecordedEvidence.materialUsed s.record + 2 * FormedSelection.bit s.reader
def energy (s : State) : Nat := RecordedEvidence.energy s.record

def Valid (M : Nat) (s : State) : Prop := RecordedEvidence.Valid M s.record ∧ material s ≤ M

def debit (s : State) (cost : Nat) : RecordedEvidence.State :=
  {s.record with plant := {s.record.plant with fuel := s.record.plant.fuel-cost}}

def sensedDecode (s : State) (index : Nat) : Option Bool :=
  s.sensed.bind (fun c => decodeAt c s.record.records index)

inductive Event where
  | record (event : RecordedEvidence.Event)
  | assembleReader | activate | sense
  | decode (index : Nat)
  | replay (path : Path)
  | publish
  | changeContext (context : Bool)
  | turnover
  | setAccess (available : Bool)
  | setDelivery (available : Bool)
deriving DecidableEq, Repr

def assayGuard (truth : Bool → Nat → Bool) (s : State) : RecordedEvidence.Event → Prop
  | .reserve => s.record.records.length < 6 ∧ queryContext s.record.records.length = s.context
  | .observe b => s.record.records.length < 6 ∧ queryContext s.record.records.length = s.context ∧
      b = truth s.context (queryEdge s.record.records.length)
  | _ => True

def Enabled (truth : Bool → Nat → Bool) (s : State) : Event → Prop
  | .record a => s.phase = 0 ∧ RecordedEvidence.Enabled s.record a ∧ assayGuard truth s a
  | .assembleReader => s.phase = 0 ∧ s.reader = false ∧ s.record.pending = .idle ∧
      1 ≤ s.record.plant.aFree ∧ 1 ≤ s.record.plant.hFree ∧ 1 ≤ s.record.plant.fuel
  | .activate => s.phase = 0 ∧ s.reader = true ∧ s.record.pending = .idle ∧ 1 ≤ s.record.plant.fuel
  | .sense => s.phase = 1 ∧ s.access = true ∧ 1 ≤ s.record.plant.fuel
  | .decode i => s.phase = 2+i ∧ i < 3 ∧ s.access = true ∧ 1 ≤ s.record.plant.fuel
  | .replay path => s.phase = 5+pathIndex path ∧ pathCost path ≤ s.record.plant.fuel
  | .publish => s.phase = 9 ∧ s.sensed.isSome = true
  | .changeContext _ | .turnover => s.record.pending = .idle
  | .setAccess _ | .setDelivery _ => True

def advance (g : Graph) (s : State) : Event → State
  | .record a => {s with record := RecordedEvidence.advance s.record a}
  | .assembleReader => {s with reader := true, record := {s.record with plant := {s.record.plant with aFree := s.record.plant.aFree-1, hFree := s.record.plant.hFree-1, fuel := s.record.plant.fuel-1}}}
  | .activate => {s with record := debit s 1, phase := 1, sensed := none, decoded := [], working := emptyMask}
  | .sense => {s with record := debit s 1, phase := 2, sensed := some s.context}
  | .decode i => {s with record := debit s 1, phase := s.phase+1, decoded := s.decoded ++ [sensedDecode s i]}
  | .replay path => {s with record := debit s (pathCost path), phase := s.phase+1, working := applyPath g s.decoded s.working path}
  | .publish => {s with phase := 10, installed := s.sensed.map (fun c => (c,s.working))}
  | .changeContext c => {s with context := c, phase := 0, sensed := none}
  | .turnover => {s with phase := 0, sensed := none, decoded := [], working := emptyMask, installed := none}
  | .setAccess b => {s with access := b}
  | .setDelivery b => {s with delivery := b}

def spending : Event → Nat
  | .record a => RecordedEvidence.spending a
  | .assembleReader | .activate | .sense | .decode _ => 1
  | .replay path => pathCost path
  | _ => 0

def tally : List Event → Nat
  | [] => 0
  | a :: as => spending a + tally as

def Step (M : Nat) (g : Graph) (truth : Bool → Nat → Bool) (s : State) (a : Event) (t : State) : Prop :=
  Valid M s ∧ Enabled truth s a ∧ t = advance g s a

instance (M : Nat) (s : State) : Decidable (Valid M s) := by unfold Valid; infer_instance
instance (truth : Bool → Nat → Bool) (s : State) (a : RecordedEvidence.Event) : Decidable (assayGuard truth s a) := by
  cases a <;> unfold assayGuard <;> infer_instance
instance (truth : Bool → Nat → Bool) (s : State) (a : Event) : Decidable (Enabled truth s a) := by
  cases a <;> unfold Enabled <;> infer_instance
instance (M : Nat) (g : Graph) (truth : Bool → Nat → Bool) (s t : State) (a : Event) : Decidable (Step M g truth s a t) := by
  unfold Step; infer_instance

def process (M : Nat) (g : Graph) (truth : Bool → Nat → Bool) : Generative.Process State Event := ⟨Step M g truth⟩
def Trace (M : Nat) (g : Graph) (truth : Bool → Nat → Bool) := Generative.Trace (process M g truth)

def auditEvents : List Event :=
  [.activate,.sense,.decode 0,.decode 1,.decode 2,
   .replay .directP,.replay .directQ,.replay .viaP,.replay .viaQ,.publish]

def run (g : Graph) : State → List Event → State
  | s, [] => s
  | s, a :: as => run g (advance g s a) as

def Runnable (M : Nat) (g : Graph) (truth : Bool → Nat → Bool) : State → List Event → Prop
  | _, [] => True
  | s, a :: as => Valid M s ∧ Enabled truth s a ∧ Runnable M g truth (advance g s a) as

def runnableDecidable (M : Nat) (g : Graph) (truth : Bool → Nat → Bool) :
    (s : State) → (as : List Event) → Decidable (Runnable M g truth s as)
  | _, [] => isTrue trivial
  | s, a :: as => by
    haveI : Decidable (Runnable M g truth (advance g s a) as) := runnableDecidable M g truth (advance g s a) as
    unfold Runnable; infer_instance
instance (M : Nat) (g : Graph) (truth : Bool → Nat → Bool) (s : State) (as : List Event) :
    Decidable (Runnable M g truth s as) := runnableDecidable M g truth s as

theorem runnable_trace {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s : State} {as : List Event} (h : Runnable M g truth s as) : Trace M g truth s as (run g s as) := by
  induction as generalizing s with
  | nil => exact .nil _
  | cons a as ih => exact .cons ⟨h.1,h.2.1,rfl⟩ (ih h.2.2)

theorem trace_run {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (h : Trace M g truth s as t) : t = run g s as := by
  induction h with
  | nil => rfl
  | cons hs _ ih => rcases hs with ⟨_,_,rfl⟩; exact ih

theorem record_step_projects {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {a : RecordedEvidence.Event} (h : Step M g truth s (.record a) t) :
    RecordedEvidence.Step M s.record a t.record := by
  rcases h with ⟨hv,he,rfl⟩
  exact ⟨hv.1,he.2.1,rfl⟩

theorem step_material {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {a : Event} (h : Step M g truth s a t) : material t = material s := by
  cases a with
  | record a =>
    have hm := RecordedEvidence.step_material (record_step_projects h)
    rcases h with ⟨_,_,rfl⟩
    simpa [material,advance] using congrArg (fun n => n+2*FormedSelection.bit s.reader) hm
  | assembleReader =>
    rcases h with ⟨_,he,rfl⟩
    simp only [Enabled] at he
    simp only [material,advance,RecordedEvidence.materialUsed,FormedSelection.population,he.2.1,FormedSelection.bit]
    omega
  | activate | sense | decode i | replay path | publish | changeContext c | turnover | setAccess b | setDelivery b =>
    rcases h with ⟨_,_,rfl⟩; rfl

theorem step_energy {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {a : Event} (h : Step M g truth s a t) : energy t + spending a = energy s := by
  cases a with
  | record a => exact RecordedEvidence.step_energy (record_step_projects h)
  | assembleReader =>
    rcases h with ⟨_,he,rfl⟩
    have hf := he.2.2.2.2.2
    simp only [energy,advance,RecordedEvidence.energy,FormedSelection.energy,spending]
    omega
  | activate =>
    rcases h with ⟨_,he,rfl⟩
    have hf := he.2.2.2
    simp only [energy,advance,debit,RecordedEvidence.energy,FormedSelection.energy,spending]
    omega
  | sense =>
    rcases h with ⟨_,he,rfl⟩
    have hf := he.2.2
    simp only [energy,advance,debit,RecordedEvidence.energy,FormedSelection.energy,spending]
    omega
  | decode i =>
    rcases h with ⟨_,he,rfl⟩
    have hf := he.2.2.2
    simp only [energy,advance,debit,RecordedEvidence.energy,FormedSelection.energy,spending]
    omega
  | replay path =>
    rcases h with ⟨_,he,rfl⟩
    have hf := he.2
    simp only [energy,advance,debit,RecordedEvidence.energy,FormedSelection.energy,spending]
    omega
  | publish | changeContext c | turnover | setAccess b | setDelivery b =>
    rcases h with ⟨_,_,rfl⟩; rfl

theorem step_valid {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {a : Event} (h : Step M g truth s a t) : Valid M t := by
  have hm := step_material h
  have hv := h.1
  constructor
  · cases a with
    | record a => exact RecordedEvidence.step_valid (record_step_projects h)
    | assembleReader =>
      rcases h with ⟨hv,he,rfl⟩
      rcases hv.1 with ⟨hs,hesc,hmat⟩
      have ha := he.2.2.2.1
      have hh := he.2.2.2.2.1
      simp only [advance,RecordedEvidence.Valid,RecordedEvidence.materialUsed,FormedSelection.population]
      exact ⟨hs,hesc,by simp only [RecordedEvidence.materialUsed,FormedSelection.population] at hmat; omega⟩
    | activate | sense | decode i | replay path | publish | changeContext c | turnover | setAccess b | setDelivery b =>
      rcases h with ⟨hv,_,rfl⟩; exact hv.1
  · rw [hm]; exact hv.2

theorem trace_energy {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (h : Trace M g truth s as t) : energy t + tally as = energy s := by
  induction h with
  | nil => simp [tally]
  | cons hs _ ih => have he := step_energy hs; simp only [tally]; omega

theorem trace_material {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (h : Trace M g truth s as t) : material t = material s := by
  induction h with
  | nil => rfl
  | cons hs _ ih => exact ih.trans (step_material hs)

theorem trace_valid {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (hv : Valid M s) (h : Trace M g truth s as t) : Valid M t := by
  induction h with
  | nil => exact hv
  | cons hs _ ih => exact ih (step_valid hs)

theorem assayed_append {truth : Bool → Nat → Bool} {records : List Bool} {bit : Bool}
    (ha : Assayed truth records)
    (hb : records.length < 6 ∧ bit = truth (queryContext records.length) (queryEdge records.length)) :
    Assayed truth (records ++ [bit]) := by
  intro index value hv
  by_cases hi : index < records.length
  · rw [List.getElem?_append_left hi] at hv
    exact ha index value hv
  · have hp := (List.getElem?_eq_some_iff.mp hv).1
    have he : index = records.length := by simp only [List.length_append,List.length_cons,List.length_nil] at hp; omega
    subst index
    simp only [List.getElem?_append_right (Nat.le_refl _),Nat.sub_self,List.getElem?_cons_zero,Option.some.injEq] at hv
    subst value
    exact hb

def Authentic (truth : Bool → Nat → Bool) (s : State) : Prop :=
  Assayed truth s.record.records ∧
  ∀ bit, s.record.pending = .latched bit → s.record.records.length < 6 ∧
    bit = truth (queryContext s.record.records.length) (queryEdge s.record.records.length)

theorem handoff_authentic (truth : Bool → Nat → Bool) (s : FormedSelection.State) :
    Authentic truth (handoff s) := by
  constructor
  · intro index bit h; simp [handoff,RecordedEvidence.handoff] at h
  · intro bit h; cases h

theorem step_authentic {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {a : Event} (hi : Authentic truth s) (h : Step M g truth s a t) : Authentic truth t := by
  rcases h with ⟨_,he,rfl⟩
  cases a with
  | record a =>
    rcases hi with ⟨ha,hp⟩
    cases a with
    | assemble => exact ⟨ha,hp⟩
    | reserve => exact ⟨ha,fun _ h => by cases h⟩
    | observe b =>
      refine ⟨ha,?_⟩
      intro bit hb
      have hbe : b = bit := by injection hb
      subst bit
      have hg := he.2.2
      exact ⟨hg.1, by change b = truth (queryContext s.record.records.length) (queryEdge s.record.records.length); rw [hg.2.1]; exact hg.2.2⟩
    | commit b =>
      have hb := hp b he.2.1
      exact ⟨assayed_append ha hb,fun _ h => by cases h⟩
  | assembleReader | activate | sense | decode i | replay path | publish | changeContext c | turnover | setAccess b | setDelivery b => exact hi

theorem trace_authentic {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (hi : Authentic truth s) (h : Trace M g truth s as t) : Authentic truth t := by
  induction h with
  | nil => exact hi
  | cons hs _ ih => exact ih (step_authentic hi hs)

set_option maxRecDepth 4096 in
theorem audit_run_accounts (g : Graph) (s : State) :
    (run g s auditEvents).record.records = s.record.records ∧
    (run g s auditEvents).record.plant.fuel + 11 = s.record.plant.fuel + (11-s.record.plant.fuel) ∧
    (run g s auditEvents).record.plant.source = s.record.plant.source ∧
    (run g s auditEvents).context = s.context ∧
    (run g s auditEvents).installed = some (s.context,closureMask g (decodedAt s.context s.record.records)) := by
  simp [run,auditEvents,advance,debit,sensedDecode,decodedAt,closureMask,paths,emptyMask,pathCost,Nat.sub_sub]
  omega

theorem audit_run_energy (g : Graph) (s : State) :
    energy (run g s auditEvents) + 11 = energy s + (11-s.record.plant.fuel) := by
  simp [energy,RecordedEvidence.energy,FormedSelection.energy,run,auditEvents,advance,debit,pathCost,Nat.sub_sub]
  omega

theorem paid_audit_installs_exact_closure {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} (h : Trace M g truth s auditEvents t) :
    t.installed = some (s.context,closureMask g (decodedAt s.context s.record.records)) ∧
    t.record.records = s.record.records ∧ t.record.plant.fuel + 11 = s.record.plant.fuel := by
  have hr := trace_run h
  have hac := audit_run_accounts g s
  have hen := trace_energy h
  have hea := audit_run_energy g s
  have hc : tally auditEvents = 11 := by decide
  rw [hc,hr] at hen
  have hz : 11-s.record.plant.fuel = 0 := by omega
  rw [hr]
  exact ⟨hac.2.2.2.2,hac.1,by have hf := hac.2.1; omega⟩

/-- A completed contextual audit is sound only under the independent anchor and
relevance implications for its actual current decoded observations. -/
theorem paid_audit_rooted_sound {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} (h : Trace M g truth s auditEvents t)
    (Reason : Node → Prop) (anchor : Reason .root)
    (relevant : ∀ u v, edge g (decodedAt s.context s.record.records) u v = true → Reason u → Reason v)
    {mask : Mask} (hi : t.installed = some (s.context,mask)) {v : Node} (ha : mask.has v) : Reason v := by
  have hm := (paid_audit_installs_exact_closure h).1
  rw [hi] at hm
  have he : mask = closureMask g (decodedAt s.context s.record.records) := by injection hm with hm; exact (Prod.mk.inj hm).2
  rw [he] at ha
  exact closure_semantic_sound _ _ Reason anchor relevant ha

/-- A current negative applies to the edge-specific fact, not to the destination reason. -/
theorem negative_decode_identifies_false_assay {truth : Bool → Nat → Bool} {records : List Bool}
    (ha : Assayed truth records) (context : Bool) (index : Nat) (hi : index < 3)
    (h : decodeAt context records index = some false) : truth context index = false :=
  (current_decode_sound ha context index hi false h).symm

theorem access_cut_retains_records_and_published_reason (g : Graph) (s : State) :
    (advance g s (.setAccess false)).record = s.record ∧
    (advance g s (.setAccess false)).installed = s.installed ∧
    (advance g s (.setAccess false)).decoded = s.decoded := ⟨rfl,rfl,rfl⟩

theorem delivery_cut_is_not_refutation (g : Graph) (s : State) :
    (advance g s (.setDelivery false)).record = s.record ∧
    (advance g s (.setDelivery false)).installed = s.installed ∧
    (advance g s (.setDelivery false)).working = s.working := ⟨rfl,rfl,rfl⟩

theorem context_change_preserves_history_not_current_audit (g : Graph) (s : State) (c : Bool) :
    (advance g s (.changeContext c)).record = s.record ∧
    (advance g s (.changeContext c)).installed = s.installed ∧
    (advance g s (.changeContext c)).phase = 0 ∧
    (advance g s (.changeContext c)).sensed = none := ⟨rfl,rfl,rfl,rfl⟩

theorem successor_turnover_preserves_physical_grounds (g : Graph) (s : State) :
    (advance g s .turnover).record = s.record ∧
    (advance g s .turnover).reader = s.reader ∧
    (advance g s .turnover).installed = none ∧
    (advance g s .turnover).phase = 0 := ⟨rfl,rfl,rfl,rfl⟩

/-- The edge identities remain distinct even when endpoints coincide. -/
def endpoints (g : Graph) (i : Nat) : Node × Node :=
  if i = 0 then g.e0 else if i = 1 then g.e1 else g.e2

theorem calibrated_edges_preserve_reasons {truth : Bool → Nat → Bool} {records : List Bool}
    (ha : Assayed truth records) (g : Graph) (context : Bool)
    (Fact : Nat → Prop) (Reason : Node → Prop)
    (calibrated : ∀ i, i < 3 → truth context i = true → Fact i)
    (relevant : ∀ i, i < 3 → Fact i → Reason (endpoints g i).1 → Reason (endpoints g i).2)
    {u v : Node} (he : edge g (decodedAt context records) u v = true) (hu : Reason u) : Reason v := by
  simp only [edge,Bool.or_eq_true,Bool.and_eq_true,beq_iff_eq] at he
  rcases he with (⟨he,hp⟩ | ⟨he,hp⟩) | ⟨he,hp⟩
  · have hd : decodeAt context records 0 = some true := by simpa [positive,decodedAt] using hp
    have ht := (current_decode_sound ha context 0 (by decide) true hd).symm
    have hr := relevant 0 (by decide) (calibrated 0 (by decide) ht)
    simp [endpoints,he] at hr
    exact hr hu
  · have hd : decodeAt context records 1 = some true := by simpa [positive,decodedAt] using hp
    have ht := (current_decode_sound ha context 1 (by decide) true hd).symm
    have hr := relevant 1 (by decide) (calibrated 1 (by decide) ht)
    simp [endpoints,he] at hr
    exact hr hu
  · have hd : decodeAt context records 2 = some true := by simpa [positive,decodedAt] using hp
    have ht := (current_decode_sound ha context 2 (by decide) true hd).symm
    have hr := relevant 2 (by decide) (calibrated 2 (by decide) ht)
    simp [endpoints,he] at hr
    exact hr hu

/-- Recorded observations reach a reason conclusion through explicit factual
calibration, relevance and anchor premises, with every replay stage paid. -/
theorem paid_recorded_reason_sound {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {start s t : State} {history : List Event}
    (ha : Authentic truth start) (hh : Trace M g truth start history s)
    (audit : Trace M g truth s auditEvents t)
    (Fact : Nat → Prop) (Reason : Node → Prop) (anchor : Reason .root)
    (calibrated : ∀ i, i < 3 → truth s.context i = true → Fact i)
    (relevant : ∀ i, i < 3 → Fact i → Reason (endpoints g i).1 → Reason (endpoints g i).2)
    {mask : Mask} (hi : t.installed = some (s.context,mask)) {v : Node} (hv : mask.has v) : Reason v := by
  have hs := (trace_authentic ha hh).1
  exact paid_audit_rooted_sound audit Reason anchor
    (fun _ _ he hu => calibrated_edges_preserve_reasons hs g s.context Fact Reason calibrated relevant he hu) hi hv

/-- A matching historical tag alone is insufficient: publication status also
requires the completed phase, which excludes subsequent record appends. -/
def CurrentPublication (s : State) (mask : Mask) : Prop :=
  s.phase = 10 ∧ s.installed = some (s.context,mask)

theorem current_publication_blocks_recording {truth : Bool → Nat → Bool}
    {s : State} {mask : Mask} (h : CurrentPublication s mask) (a : RecordedEvidence.Event) :
    ¬ Enabled truth s (.record a) := by
  intro he
  have hp := he.1
  have hc := h.1
  omega

theorem reset_withdraws_current_publication (g : Graph) (s : State) (c : Bool) (m : Mask) :
    ¬ CurrentPublication (advance g s (.changeContext c)) m := by
  intro h
  have hp := h.1
  simp [advance] at hp

theorem audit_is_funded_iff {M : Nat} {g : Graph} {truth : Bool → Nat → Bool} {s : State}
    (hv : Valid M s) (hp : s.phase = 0) (hr : s.reader = true)
    (hi : s.record.pending = .idle) (ha : s.access = true) :
    (∃ t, Trace M g truth s auditEvents t) ↔ 11 ≤ s.record.plant.fuel := by
  constructor
  · rintro ⟨t,ht⟩
    have he := (paid_audit_installs_exact_closure ht).2.2
    omega
  · intro hf
    refine ⟨run g s auditEvents,runnable_trace ?_⟩
    rcases hv with ⟨⟨hslots,hesc,hmaterial⟩,hm⟩
    simp [Runnable,auditEvents,Enabled,advance,Valid,RecordedEvidence.Valid,
      material,RecordedEvidence.materialUsed,FormedSelection.population,
      FormedSelection.bit,debit,pathIndex,pathCost,hp,hr,hi,ha,
      hslots,hesc,Nat.sub_sub] at *
    omega

inductive Stage where | formation (s : FormedSelection.State) | reason (s : State)
deriving DecidableEq, Repr
inductive StageEvent where | formation (a : FormedSelection.Event) | handoff | reason (a : Event)
deriving DecidableEq, Repr

def StagedStep (M : Nat) (g : Graph) (truth : Bool → Nat → Bool) : Stage → StageEvent → Stage → Prop
  | .formation s,.formation a,.formation t => FormedSelection.Step M s a t
  | .formation s,.handoff,.reason t => FormedSelection.Valid M s ∧ t = handoff s
  | .reason s,.reason a,.reason t => Step M g truth s a t
  | _,_,_ => False

def stagedProcess (M : Nat) (g : Graph) (truth : Bool → Nat → Bool) : Generative.Process Stage StageEvent :=
  ⟨StagedStep M g truth⟩
def StagedTrace (M : Nat) (g : Graph) (truth : Bool → Nat → Bool) := Generative.Trace (stagedProcess M g truth)

theorem formation_trace_embeds {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : FormedSelection.State} {as : List FormedSelection.Event} (h : FormedSelection.Trace M s as t) :
    StagedTrace M g truth (.formation s) (as.map StageEvent.formation) (.formation t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih => exact Generative.Trace.cons (m := Stage.formation u) hs ih

theorem reason_trace_embeds {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} {as : List Event} (h : Trace M g truth s as t) :
    StagedTrace M g truth (.reason s) (as.map StageEvent.reason) (.reason t) := by
  induction h with
  | nil => exact .nil _
  | @cons s u t a as hs _ ih => exact Generative.Trace.cons (m := Stage.reason u) hs ih

theorem compose_actual_state {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s u : FormedSelection.State} {t : State} {as : List FormedSelection.Event} {bs : List Event}
    (hv : FormedSelection.Valid M s) (hp : FormedSelection.Trace M s as u)
    (hr : Trace M g truth (handoff u) bs t) :
    StagedTrace M g truth (.formation s)
      (as.map StageEvent.formation ++ .handoff :: bs.map StageEvent.reason) (.reason t) := by
  apply Generative.trace_append_iff.mpr
  refine ⟨.formation u,formation_trace_embeds hp,?_⟩
  apply Generative.Trace.cons (m := .reason (handoff u))
  · exact ⟨FormedSelection.trace_valid hv hp,rfl⟩
  · exact reason_trace_embeds hr

def primary : Graph := ⟨(.root,.p),(.p,.q),(.root,.q)⟩
def truth : Bool → Nat → Bool | false,_ => true | true,i => !(i==0)
def initial : FormedSelection.State := ⟨0,0,.empty,false,false,80,20⟩
def prepared : FormedSelection.State := ⟨7,7,.active,true,false,63,20⟩
def formationEvents : List FormedSelection.Event :=
  [.formH,.formH,.formH,.formH,.formH,.formH,.formH,
   .formA,.formA,.formA,.formA,.formA,.formA,.formA,.formA,.associateA,.repair]

theorem actual_part_preparation : FormedSelection.Trace 15 initial formationEvents prepared := by
  apply FormedSelection.Trace.cons (u := ⟨0,1,.empty,false,false,79,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,2,.empty,false,false,78,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,3,.empty,false,false,77,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,4,.empty,false,false,76,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,5,.empty,false,false,75,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,6,.empty,false,false,74,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0,7,.empty,false,false,73,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1,7,.empty,false,false,72,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨2,7,.empty,false,false,71,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨3,7,.empty,false,false,70,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨4,7,.empty,false,false,69,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨5,7,.empty,false,false,68,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨6,7,.empty,false,false,67,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨7,7,.empty,false,false,66,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨8,7,.empty,false,false,65,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨7,7,.active,false,false,64,20⟩) (by decide)
  apply FormedSelection.Trace.cons (u := prepared) (by decide)
  exact .nil _

def recordBit (b : Bool) : List Event := [.record .reserve,.record (.observe b),.record (.commit b)]
def apparatusEvents : List Event :=
  [.record .assemble,.record .assemble,.record .assemble,.record .assemble,.record .assemble,.record .assemble,.assembleReader]
def firstRecordEvents : List Event := recordBit true ++ recordBit true ++ recordBit true
def secondRecordEvents : List Event := recordBit false ++ recordBit true ++ recordBit true

def ready := run primary (handoff prepared) apparatusEvents
def firstRecorded := run primary ready firstRecordEvents
def firstPublished := run primary firstRecorded auditEvents
def changed := advance primary firstPublished (.changeContext true)
def secondRecorded := run primary changed secondRecordEvents
def secondPublished := run primary secondRecorded auditEvents
def successor := advance primary secondPublished .turnover
def final := run primary successor auditEvents

def fullEvents := apparatusEvents ++ firstRecordEvents ++ auditEvents ++
  [.changeContext true] ++ secondRecordEvents ++ auditEvents ++ [.turnover] ++ auditEvents

theorem actual_apparatus : Trace 15 primary truth (handoff prepared) apparatusEvents ready :=
  runnable_trace (by decide)
theorem actual_first_records : Trace 15 primary truth ready firstRecordEvents firstRecorded :=
  runnable_trace (by decide)
theorem actual_first_audit : Trace 15 primary truth firstRecorded auditEvents firstPublished :=
  runnable_trace (by decide)
theorem actual_second_records : Trace 15 primary truth changed secondRecordEvents secondRecorded :=
  runnable_trace (by decide)
theorem actual_revised_audit : Trace 15 primary truth secondRecorded auditEvents secondPublished :=
  runnable_trace (by decide)
theorem actual_successor_replay : Trace 15 primary truth successor auditEvents final :=
  runnable_trace (by decide)

theorem full_history : Trace 15 primary truth (handoff prepared) fullEvents final :=
  runnable_trace (by decide)

theorem actual_construction_record_revision_successor :
    StagedTrace 15 primary truth (.formation initial)
      (formationEvents.map StageEvent.formation ++ .handoff :: fullEvents.map StageEvent.reason) (.reason final) :=
  compose_actual_state (by decide) actual_part_preparation full_history

theorem whole_history_resource_account :
    FormedSelection.Absent initial ∧ FormedSelection.energy initial = 100 ∧
    FormedSelection.tally FormedSelection.expenditure formationEvents = 17 ∧
    tally apparatusEvents = 7 ∧ tally firstRecordEvents + tally secondRecordEvents = 12 ∧
    tally auditEvents = 11 ∧ final.record.plant.fuel = 13 ∧ final.record.plant.source = 18 ∧
    material final = 15 ∧ energy final = 31 ∧
    FormedSelection.energy initial = 17 + 6 + 1 + 12 + 3*11 + energy final := by unfold FormedSelection.Absent; decide

theorem rooted_revision_keeps_alternative_ground :
    firstPublished.installed = some (false,⟨true,true⟩) ∧
    secondPublished.installed = some (true,⟨false,true⟩) ∧
    final.installed = secondPublished.installed ∧
    final.record.records = [true,true,true,false,true,true] ∧
    successor.installed = none ∧ successor.reader = true ∧
    final.record.records = successor.record.records ∧
    final.record.plant.fuel + 11 = successor.record.plant.fuel := by decide

theorem actual_history_authentic : Authentic truth final :=
  trace_authentic (handoff_authentic truth prepared) full_history

theorem stale_and_missing_are_not_new_negative :
    changed.installed = some (false,⟨true,true⟩) ∧ changed.context = true ∧
    decodedAt changed.context changed.record.records = [none,none,none] ∧
    ¬ CurrentPublication changed ⟨true,true⟩ ∧
    decodedAt secondRecorded.context secondRecorded.record.records = [some false,some true,some true] := by unfold CurrentPublication; decide

theorem unsupported_cycle_does_not_self_anchor :
    closureMask ⟨(.root,.p),(.p,.q),(.q,.p)⟩ [some false,some true,some true] = emptyMask := by decide

/-- Existing M5 record machinery has no free pair for this additional circuit. -/
theorem old_full_recorder_cannot_supply_reader :
    ¬ Enabled truth {handoff RecordedEvidence.exhausted.plant with record := RecordedEvidence.exhausted} .assembleReader := by decide

/-- Shared physical grounds allow another paid replay, but not unlimited replays. -/
def extraSuccessor := advance primary final .turnover
def extraFinal := run primary extraSuccessor auditEvents

theorem one_more_replay_then_liquidity_failure :
    Trace 15 primary truth extraSuccessor auditEvents extraFinal ∧
    extraFinal.record.plant.fuel = 2 ∧ extraFinal.record.plant.source = 18 ∧
    ¬ ∃ t, Trace 15 primary truth (advance primary extraFinal .turnover) auditEvents t := by
  refine ⟨runnable_trace (by decide),by decide,by decide,?_⟩
  rintro ⟨t,h⟩
  have he := (paid_audit_installs_exact_closure h).2.2
  have hf : (advance primary extraFinal .turnover).record.plant.fuel = 2 := by decide
  rw [hf] at he
  omega

/-- Factual refutation additionally needs negative calibration; positive-only
calibration cannot establish it by contraposition. -/
theorem calibrated_negative_refutes_only_edge_fact {truth : Bool → Nat → Bool} {records : List Bool}
    (ha : Assayed truth records) (context : Bool) (i : Nat) (hi : i < 3)
    (Fact : Nat → Prop) (negativeCalibration : truth context i = false → ¬ Fact i)
    (h : decodeAt context records i = some false) : ¬ Fact i :=
  negativeCalibration (negative_decode_identifies_false_assay ha context i hi h)

/-- Exact available-evidence closure is an endpoint theorem for a completed
paid audit, not a claim inferred from an old matching publication tag. -/
theorem paid_audit_exact_available_reachability {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} (h : Trace M g truth s auditEvents t)
    {mask : Mask} (hi : t.installed = some (s.context,mask)) (v : Node) :
    mask.has v ↔ Rooted (fun u v => edge g (decodedAt s.context s.record.records) u v = true) v := by
  have hm := (paid_audit_installs_exact_closure h).1
  rw [hi] at hm
  have he : mask = closureMask g (decodedAt s.context s.record.records) := by
    injection hm with hm
    exact (Prod.mk.inj hm).2
  rw [he]
  exact closure_exact _ _ _

theorem completed_audit_has_current_status {M : Nat} {g : Graph} {truth : Bool → Nat → Bool}
    {s t : State} (h : Trace M g truth s auditEvents t) :
    CurrentPublication t (closureMask g (decodedAt s.context s.record.records)) := by
  have hr := trace_run h
  have hac := audit_run_accounts g s
  refine ⟨?_,?_⟩
  · rw [hr]
    simp [run,auditEvents,advance]
  · rw [hr,hac.2.2.2.1]
    exact hac.2.2.2.2

theorem access_cut_blocks_acquisition (g : Graph) (truth : Bool → Nat → Bool) (s : State) (i : Nat) :
    ¬ Enabled truth (advance g s (.setAccess false)) .sense ∧
    ¬ Enabled truth (advance g s (.setAccess false)) (.decode i) := by
  simp [Enabled,advance]

end ReasonReplay

#print axioms ReasonReplay.supported_closed
#print axioms ReasonReplay.rooted_iff_supported
#print axioms ReasonReplay.closure_exact
#print axioms ReasonReplay.rooted_semantic_sound
#print axioms ReasonReplay.closure_semantic_sound
#print axioms ReasonReplay.current_decode_sound
#print axioms ReasonReplay.missing_is_not_negative
#print axioms ReasonReplay.recorded_word_supplies_assay
#print axioms ReasonReplay.runnable_trace
#print axioms ReasonReplay.trace_run
#print axioms ReasonReplay.record_step_projects
#print axioms ReasonReplay.step_material
#print axioms ReasonReplay.step_energy
#print axioms ReasonReplay.step_valid
#print axioms ReasonReplay.trace_energy
#print axioms ReasonReplay.trace_material
#print axioms ReasonReplay.trace_valid
#print axioms ReasonReplay.assayed_append
#print axioms ReasonReplay.handoff_authentic
#print axioms ReasonReplay.step_authentic
#print axioms ReasonReplay.trace_authentic
#print axioms ReasonReplay.audit_run_accounts
#print axioms ReasonReplay.audit_run_energy
#print axioms ReasonReplay.paid_audit_installs_exact_closure
#print axioms ReasonReplay.paid_audit_rooted_sound
#print axioms ReasonReplay.negative_decode_identifies_false_assay
#print axioms ReasonReplay.access_cut_retains_records_and_published_reason
#print axioms ReasonReplay.delivery_cut_is_not_refutation
#print axioms ReasonReplay.context_change_preserves_history_not_current_audit
#print axioms ReasonReplay.successor_turnover_preserves_physical_grounds
#print axioms ReasonReplay.calibrated_edges_preserve_reasons
#print axioms ReasonReplay.paid_recorded_reason_sound
#print axioms ReasonReplay.current_publication_blocks_recording
#print axioms ReasonReplay.reset_withdraws_current_publication
#print axioms ReasonReplay.audit_is_funded_iff
#print axioms ReasonReplay.formation_trace_embeds
#print axioms ReasonReplay.reason_trace_embeds
#print axioms ReasonReplay.compose_actual_state
#print axioms ReasonReplay.actual_part_preparation
#print axioms ReasonReplay.actual_apparatus
#print axioms ReasonReplay.actual_first_records
#print axioms ReasonReplay.actual_first_audit
#print axioms ReasonReplay.actual_second_records
#print axioms ReasonReplay.actual_revised_audit
#print axioms ReasonReplay.actual_successor_replay
#print axioms ReasonReplay.full_history
#print axioms ReasonReplay.actual_construction_record_revision_successor
#print axioms ReasonReplay.whole_history_resource_account
#print axioms ReasonReplay.rooted_revision_keeps_alternative_ground
#print axioms ReasonReplay.actual_history_authentic
#print axioms ReasonReplay.stale_and_missing_are_not_new_negative
#print axioms ReasonReplay.unsupported_cycle_does_not_self_anchor
#print axioms ReasonReplay.old_full_recorder_cannot_supply_reader
#print axioms ReasonReplay.one_more_replay_then_liquidity_failure
#print axioms ReasonReplay.calibrated_negative_refutes_only_edge_fact
#print axioms ReasonReplay.paid_audit_exact_available_reachability
#print axioms ReasonReplay.completed_audit_has_current_status
#print axioms ReasonReplay.access_cut_blocks_acquisition
