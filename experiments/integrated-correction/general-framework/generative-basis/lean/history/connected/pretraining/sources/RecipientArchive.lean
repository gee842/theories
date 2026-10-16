import EmissionArchive
import RecipientIdentification

namespace RecipientArchive

open RecipientCorrection (Target Laws lookup packedAct receiptOf)

structure Frame where
  context : Bool
  action : Bool
  present : Bool
  receipt : Bool
  deriving DecidableEq, Repr

def encode (r : Frame) : List Bool := [r.context,r.action,r.present,r.receipt]

theorem encode_injective {r x : Frame} (h : encode r = encode x) : r = x := by
  cases r; cases x
  simp only [encode,List.cons.injEq] at h
  rcases h with ⟨rfl,rfl,rfl,rfl,_⟩
  rfl

structure Header where
  address : Nat
  context : Bool
  action : Bool
  deriving DecidableEq, Repr

/- next/current are the declared bounded query workspace, not archive indices
computed from the number of completed records. A context change quarantines it. -/
structure World where
  core : RecipientIdentification.State
  context : Bool
  next : Nat
  current : Option Nat
  live : Bool
  deriving DecidableEq, Repr

inductive Event where
  | core (event : RecipientIdentification.Event)
  | contextChange (context : Bool)
  deriving DecidableEq, Repr

def advance (laws : Laws) (s : World) : Event → World
  | .core e => { s with
      core := RecipientIdentification.advance laws s.core e,
      next := if e = .sense .recipient then s.next+1 else s.next,
      current := if e = .sense .recipient then some s.next else s.current }
  | .contextChange c => { s with context := c, current := none, live := false }

def Step (laws : Laws) (s : World) (e : Event) (t : World) : Prop :=
  (match e with
   | .core e => RecipientIdentification.Step laws s.core e t.core ∧
       (e = .sense .recipient → s.next < 3)
   | .contextChange _ => True) ∧ t = advance laws s e

def binding (s : World) (i : Nat) (h : Header) : Prop :=
  s.live = true ∧ s.core.phase = .sensed .recipient ∧ s.current = some i ∧
  h.address = i ∧ h.context = s.context ∧ h.action = packedAct s.core.hardware.q .recipient

/- Acquisition is the only emission. The guard checks the prebound query id,
context and command against the continuing physical query. None is recorded. -/
def emission (h : Header) (s : World) (e : Event) (_t : World) : Option Frame :=
  if s.live && (h.context == s.context) && (s.current == some h.address) &&
      (h.action == packedAct s.core.hardware.q .recipient) then
    match e, s.core.phase with
    | .core (.acquire channel), .worked .recipient r =>
        some ⟨h.context,h.action,channel,channel && r⟩
    | _, _ => none
  else none

def charge (laws : Laws) (s : World) : Event → Nat
  | .core e => RecipientIdentification.spending e + RecipientIdentification.waste laws s.core e
  | .contextChange _ => 0

theorem step_energy {laws : Laws} {s t : World} {e : Event} (h : Step laws s e t) :
    RecipientIdentification.energy t.core + charge laws s e = RecipientIdentification.energy s.core := by
  rcases h with ⟨hs,rfl⟩
  cases e with
  | core e => simpa [charge,Nat.add_assoc] using RecipientIdentification.step_energy hs.1
  | contextChange c => simp [advance,charge]

def producer (laws : Laws) (backing : Nat → Bool) : EmissionArchive.Producer World Event Header Frame where
  step := Step laws
  bind := fun s i h => binding s i h ∧ i < 3 ∧ backing i = true
  writable := fun s => s.live = true
  emission := emission
  encode := encode
  fourBits := by intro r; rfl
  encoding_injective := encode_injective
  energy := fun s => RecipientIdentification.energy s.core
  charge := fun s e _ => charge laws s e
  ledger := step_energy

theorem pointer_advances_without_archive (laws : Laws) (s : World) :
    (advance laws s (.core (.sense .recipient))).next = s.next+1 ∧
    (advance laws s (.core (.sense .recipient))).current = some s.next := by
  simp [advance]

theorem step_pointer_bounded {laws : Laws} {s t : World} {e : Event}
    (hs : s.next ≤ 3) (he : Step laws s e t) : t.next ≤ 3 := by
  rcases he with ⟨he,rfl⟩
  cases e with
  | contextChange c => exact hs
  | core e =>
      by_cases hr : e = .sense .recipient
      · have hn := he.2 hr; simp [advance,hr]; omega
      · simpa [advance,hr] using hs

theorem context_change_quarantines (laws : Laws) (s : World) (c : Bool) (h : Header)
    (e : Event) (t : World) :
    emission h (advance laws s (.contextChange c)) e t = none := by
  simp [emission,advance]

theorem quarantined_writer_blocked (laws : Laws) (backing : Nat → Bool) (n : Nat)
    (a : EmissionArchive.State World Header Frame) (h : a.world.live=false) :
    ¬ EmissionArchive.Enabled (producer laws backing) n a .write := by
  simp [EmissionArchive.Enabled,producer,h]

theorem later_query_cannot_fill (h : Header) (s : World) (e : Event) (t : World)
    (different : s.current ≠ some h.address) : emission h s e t = none := by
  simp [emission,different]

theorem missing_channel_is_explicit (h : Header) (s t : World) (r : Bool)
    (hl : s.live = true) (hc : h.context = s.context)
    (hi : s.current = some h.address)
    (ha : h.action = packedAct s.core.hardware.q .recipient)
    (hp : s.core.phase = .worked .recipient r) :
    emission h s (.core (.acquire false)) t = some ⟨h.context,h.action,false,false⟩ := by
  simp [emission,hl,hc,hi,ha,hp]

def PhysicalSound (laws : Laws) (s : World) : Prop :=
  ∀ r, s.core.phase = .worked .recipient r → r = true →
    packedAct s.core.hardware.q .recipient = lookup laws .recipient

theorem ready_sound (laws : Laws) (s : World) (h : s.core.phase = .ready) : PhysicalSound laws s := by
  simp [PhysicalSound,h]

theorem physical_step_sound {laws : Laws} {s t : World} {e : Event}
    (hs : PhysicalSound laws s) (he : Step laws s e t) : PhysicalSound laws t := by
  rcases he with ⟨he,rfl⟩
  cases e with
  | contextChange c => exact hs
  | core e =>
      rcases he.1 with ⟨_,hen,_⟩
      cases e with
      | work av =>
          rcases hen with ⟨⟨target,hp⟩,_,_⟩
          cases target with
          | actor => simp [PhysicalSound,advance,RecipientIdentification.advance,hp,RecipientIdentification.targetOf]
          | recipient =>
              intro r hr ht
              simp [advance,RecipientIdentification.advance,hp,RecipientIdentification.targetOf] at hr
              have hh : RecipientIdentification.returned laws s.core av = true := hr ▸ ht
              exact RecipientIdentification.positive_receipt_identifies _ _ av (by
                simpa [RecipientIdentification.returned,RecipientIdentification.issued,hp,RecipientIdentification.targetOf] using hh)
      | acquire channel =>
          rcases hen with ⟨⟨target,r,hp⟩,_⟩
          simp [PhysicalSound,advance,RecipientIdentification.advance,hp]
      | miss =>
          simp [PhysicalSound,advance,RecipientIdentification.advance,hen.1]
      | rent => simp [PhysicalSound,advance,RecipientIdentification.advance]
      | sense target => simp [PhysicalSound,advance,RecipientIdentification.advance]
      | reserve => simp [PhysicalSound,advance,RecipientIdentification.advance]
      | write => simp [PhysicalSound,advance,RecipientIdentification.advance]

theorem emission_sound {laws : Laws} {s t : World} {h : Header} {e : Event} {r : Frame}
    (hs : PhysicalSound laws s) (hem : emission h s e t = some r)
    (positive : r.present = true ∧ r.receipt = true) :
    r.action = lookup laws .recipient ∧ r.context = s.context := by
  unfold emission at hem
  split at hem
  next hg =>
    simp only [Bool.and_eq_true,beq_iff_eq] at hg
    rcases hg with ⟨⟨⟨_,hc⟩,hi⟩,ha⟩
    cases e with
    | contextChange c => contradiction
    | core e =>
      cases e <;> try contradiction
      next channel =>
        cases hp : s.core.phase <;> simp [hp] at hem
        next target receipt =>
          cases target <;> simp at hem
          subst r
          have both : channel = true ∧ receipt = true := by simpa using positive.2
          have hr : receipt = true := both.2
          exact ⟨ha.trans (hs receipt hp hr),hc⟩
  next => contradiction

def ArchiveSound (laws : Laws) (s : EmissionArchive.State World Header Frame) : Prop :=
  PhysicalSound laws s.world ∧ ∀ i r, EmissionArchive.held s i r →
    r.present=true → r.receipt=true → r.action=lookup laws .recipient

theorem origin_sound {laws : Laws} {backing : Nat → Bool}
    {s : EmissionArchive.State World Header Frame} {e : EmissionArchive.Event World Event Header}
    {i : Nat} {r : Frame} (hs : PhysicalSound laws s.world)
    (ho : (i,r) ∈ EmissionArchive.origin (producer laws backing) s e)
    (hp : r.present=true) (hr : r.receipt=true) : r.action=lookup laws .recipient := by
  cases e with
  | bind j h => simp [EmissionArchive.origin] at ho
  | write => simp [EmissionArchive.origin] at ho
  | core event w =>
      cases ph : s.phase with
      | idle => simp [EmissionArchive.origin,ph] at ho
      | latched j x bits => simp [EmissionArchive.origin,ph] at ho
      | bound j h =>
          cases hem : emission h s.world event w with
          | none => simp [EmissionArchive.origin,producer,ph,hem] at ho
          | some x =>
              simp [EmissionArchive.origin,producer,ph,hem] at ho
              rcases ho with ⟨rfl,rfl⟩
              exact (emission_sound hs hem ⟨hp,hr⟩).1

theorem archive_step_sound {laws : Laws} {backing : Nat → Bool} {n : Nat}
    {s t : EmissionArchive.State World Header Frame} {e : EmissionArchive.Event World Event Header}
    (hs : ArchiveSound laws s) (he : EmissionArchive.Step (producer laws backing) n s e t) :
    ArchiveSound laws t := by
  constructor
  · rcases he with ⟨_,hen,rfl⟩
    cases e with
    | bind i h => exact hs.1
    | core event w => exact physical_step_sound hs.1 hen
    | write => simpa only [EmissionArchive.write_preserves_world] using hs.1
  · intro i r held present receipt
    rcases EmissionArchive.step_held_origin he held with before | now
    · exact hs.2 i r before present receipt
    · exact origin_sound hs.1 now present receipt

theorem archive_trace_sound {laws : Laws} {backing : Nat → Bool} {n : Nat}
    {s t : EmissionArchive.State World Header Frame} {es : List (EmissionArchive.Event World Event Header)}
    (hs : ArchiveSound laws s)
    (h : Generative.Trace (EmissionArchive.process (producer laws backing) n) s es t) :
    ArchiveSound laws t := by
  induction h with
  | nil => exact hs
  | cons he _ ih => exact ih (archive_step_sound hs he)

theorem empty_archive_sound (laws : Laws) (w : World) (b c : Nat)
    (hw : PhysicalSound laws w) : ArchiveSound laws (EmissionArchive.empty w b c) := by
  constructor
  · exact hw
  · intro i r bad
    exact False.elim (EmissionArchive.empty_holds_nothing w b c i r bad)

theorem completed_record_sound {laws : Laws} {s : EmissionArchive.State World Header Frame}
    (hs : ArchiveSound laws s) {i : Nat} {r : Frame} (hr : s.records i=some r)
    (present : r.present=true) (receipt : r.receipt=true) : r.action=lookup laws .recipient :=
  hs.2 i r (Or.inl hr) present receipt

/- The concrete physical backing is indexed before trials. Pooled generic
capacity never licenses taking another address's four cells. -/
def Backed (cells : Nat → Bool) (i : Nat) : Prop := i < 3 ∧ cells i = true

def PrimaryBacking : Nat → Bool := fun i => i < 3

theorem three_frames_backed : ∀ i, i < 3 → Backed PrimaryBacking i := by
  intro i hi; exact ⟨hi,by simp [PrimaryBacking,hi]⟩

def decode (current desired : Bool) : Option Frame → Option Bool
  | none => none
  | some r => if r.context == current && r.present && r.receipt then some (r.action == desired) else none

theorem decode_sound {r : Frame} {current desired z b : Bool}
    (hr : r.present = true → r.receipt = true → r.action = z)
    (hd : decode current desired (some r) = some b) : b = (z == desired) := by
  simp only [decode] at hd
  split at hd
  next hg =>
    simp only [Bool.and_eq_true,beq_iff_eq] at hg
    have ha := hr hg.1.2 hg.2
    simpa [ha] using hd.symm
  next => contradiction

theorem zero_is_unknown (r : Frame) (c d : Bool) (h : r.receipt = false) :
    decode c d (some r) = none := by simp [decode,h]

theorem missing_is_unknown (r : Frame) (c d : Bool) (h : r.present = false) :
    decode c d (some r) = none := by simp [decode,h]

theorem stale_is_unknown (r : Frame) (c d : Bool) (h : r.context ≠ c) :
    decode c d (some r) = none := by simp [decode,h]

def designated : Nat → Bool := fun i => i = 1

theorem complete_truth_vectors (z : Bool) :
    [(z == designated 0),(z == designated 1),(z == designated 2)] =
      if z then [false,true,false] else [true,false,true] := by cases z <;> decide

end RecipientArchive

#print axioms RecipientArchive.encode_injective
#print axioms RecipientArchive.step_energy
#print axioms RecipientArchive.pointer_advances_without_archive
#print axioms RecipientArchive.step_pointer_bounded
#print axioms RecipientArchive.context_change_quarantines
#print axioms RecipientArchive.quarantined_writer_blocked
#print axioms RecipientArchive.later_query_cannot_fill
#print axioms RecipientArchive.missing_channel_is_explicit
#print axioms RecipientArchive.ready_sound
#print axioms RecipientArchive.physical_step_sound
#print axioms RecipientArchive.emission_sound
#print axioms RecipientArchive.origin_sound
#print axioms RecipientArchive.archive_step_sound
#print axioms RecipientArchive.archive_trace_sound
#print axioms RecipientArchive.empty_archive_sound
#print axioms RecipientArchive.completed_record_sound
#print axioms RecipientArchive.three_frames_backed
#print axioms RecipientArchive.decode_sound
#print axioms RecipientArchive.zero_is_unknown
#print axioms RecipientArchive.missing_is_unknown
#print axioms RecipientArchive.stale_is_unknown
#print axioms RecipientArchive.complete_truth_vectors
