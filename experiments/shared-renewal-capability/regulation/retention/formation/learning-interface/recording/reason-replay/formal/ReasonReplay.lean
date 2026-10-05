import RecordedEvidence

/-!
A finite three-node contextual reason interface. Query positions are bound to
edge/context pairs before outcomes. Recorded truth and reason relevance remain
separate calibrated-assay and semantic premises. The reader is a paid finite
circuit, made from a spare A/H pair. Its declared capacity/wiring is not derived
from counting parts. Three audits in one witness reuse that physical circuit.
-/
namespace ReasonReplay

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
    | p => exact h.elim (fun he => .next .root he)
        (fun he => .next (.next .root he.1) he.2)
    | q => exact h.elim (fun he => .next .root he)
        (fun he => .next (.next .root he.1) he.2)

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
  cases context <;> simp only [Bool.false_eq_true, if_false, Bool.true_eq_true, if_true, Nat.zero_add] at hh
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
  | .assembleReader => {s with reader := true, record :=
      {s.record with plant := {s.record.plant with aFree := s.record.plant.aFree-1,
        hFree := s.record.plant.hFree-1, fuel := s.record.plant.fuel-1}}}
  | .activate => {s with record := debit s 1, phase := 1, sensed := none, decoded := [], working := emptyMask}
  | .sense => {s with record := debit s 1, phase := 2, sensed := some s.context}
  | .decode i => {s with record := debit s 1, phase := s.phase+1, decoded := s.decoded ++ [sensedDecode s i]}
  | .replay path => {s with record := debit s (pathCost path), phase := s.phase+1,
      working := applyPath g s.decoded s.working path}
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

end ReasonReplay
