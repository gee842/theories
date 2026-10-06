import RecipientArchive

namespace PaidArchiveReader

open RecipientArchive (Frame decode designated)

/- The archive/world are retained, never projected to the old fuel-return
recorder. This finite cache/pointer/interlock is supplied reader hardware. -/
structure State (World : Type) where
  world : World
  archive : Nat → Option Frame
  currentContext : Bool
  fuel : Nat
  active : Bool
  token : Option Bool
  next : Nat
  cache : Nat → Option Bool

def initial (w : W) (archive : Nat → Option Frame) (c : Bool) (fuel : Nat) : State W :=
  ⟨w,archive,c,fuel,false,none,0,fun _ => none⟩

inductive Event where
  | activate | sense | read | contextChange (context : Bool)
  deriving DecidableEq, Repr

def advance (s : State W) : Event → State W
  | .activate => { s with fuel := s.fuel-1, active := true, token := none, next := 0, cache := fun _ => none }
  | .sense => { s with fuel := s.fuel-1, token := some s.currentContext }
  | .read => { s with
      fuel := s.fuel-4, next := s.next+1,
      cache := fun i => if i=s.next then decode s.currentContext (designated i) (s.archive i) else s.cache i }
  | .contextChange c => { s with
      currentContext := c, active := false, token := none }

def Enabled (s : State W) : Event → Prop
  | .activate => 1 ≤ s.fuel
  | .sense => s.active = true ∧ s.token = none ∧ s.next = 0 ∧ 1 ≤ s.fuel
  | .read => s.active = true ∧ s.token = some s.currentContext ∧ s.next < 3 ∧ 4 ≤ s.fuel
  | .contextChange _ => True

def Step (s : State W) (e : Event) (t : State W) : Prop := Enabled s e ∧ t=advance s e

def process (W : Type) : Generative.Process (State W) Event := ⟨Step⟩

def charge : Event → Nat | .activate | .sense => 1 | .read => 4 | .contextChange _ => 0

def spent : List Event → Nat | [] => 0 | e::es => charge e+spent es

def Complete (s : State W) : Prop := s.active=true ∧ s.token=some s.currentContext ∧ s.next=3

def CacheAgrees (s : State W) : Prop := s.active=true → s.token=some s.currentContext →
  ∀ i, i < s.next → s.cache i = decode s.currentContext (designated i) (s.archive i)

def Facts (z : Bool) (s : State W) : Prop :=
  ∀ i r, s.archive i=some r → r.present=true → r.receipt=true → r.action=z

theorem step_preserves_world {s t : State W} {e : Event} (h : Step s e t) : t.world=s.world := by
  rcases h with ⟨_,rfl⟩; cases e <;> rfl

theorem step_preserves_archive {s t : State W} {e : Event} (h : Step s e t) : t.archive=s.archive := by
  rcases h with ⟨_,rfl⟩; cases e <;> rfl

theorem step_ledger {s t : State W} {e : Event} (h : Step s e t) : t.fuel+charge e=s.fuel := by
  rcases h with ⟨he,rfl⟩
  cases e <;> simp [advance,charge] <;> simp only [Enabled] at he <;> omega

theorem trace_ledger {s t : State W} {es : List Event}
    (h : Generative.Trace (process W) s es t) : t.fuel+spent es=s.fuel := by
  induction h with
  | nil => simp [spent]
  | cons hs _ ih => have hh := step_ledger hs; simp only [spent]; omega

theorem initial_cache_agrees (w : W) (archive : Nat → Option Frame) (c : Bool) (f : Nat) :
    CacheAgrees (initial w archive c f) := by simp [CacheAgrees,initial]

theorem step_cache_agrees {s t : State W} {e : Event}
    (hs : CacheAgrees s) (he : Step s e t) : CacheAgrees t := by
  rcases he with ⟨he,rfl⟩
  cases e with
  | activate => simp [CacheAgrees,advance]
  | contextChange c => simp [CacheAgrees,advance]
  | sense =>
      intro _ _ i hi
      simp only [advance] at hi
      have hz : s.next=0 := he.2.2.1
      omega
  | read =>
      intro _ _ i hi
      simp only [advance] at hi ⊢
      by_cases hn : i=s.next
      · simp [hn]
      · have hlt : i<s.next := by omega
        simpa [hn] using hs he.1 he.2.1 i hlt

theorem trace_cache_agrees {s t : State W} {es : List Event}
    (hs : CacheAgrees s) (h : Generative.Trace (process W) s es t) : CacheAgrees t := by
  induction h with
  | nil => exact hs
  | cons he _ ih => exact ih (step_cache_agrees hs he)

theorem completed_paid_cache_sound {s : State W} {z : Bool}
    (hc : Complete s) (hs : CacheAgrees s) (hf : Facts z s)
    {i : Nat} (hi : i<3) {b : Bool} (hb : s.cache i=some b) : b=(z==designated i) := by
  have hd := hs hc.1 hc.2.1 i (by rw [hc.2.2]; exact hi)
  rw [hd] at hb
  cases hr : s.archive i with
  | none => simp [hr,decode] at hb
  | some r =>
      rw [hr] at hb
      exact RecipientArchive.decode_sound (hf i r hr) hb

theorem context_change_invalidates (s : State W) (c : Bool) :
    ¬ Complete (advance s (.contextChange c)) ∧
    (advance s (.contextChange c)).cache=s.cache ∧
    (advance s (.contextChange c)).token=none := by
  simp [Complete,advance]

def run (s : State W) : List Event → State W
  | [] => s
  | e::es => run (advance s e) es

def word : List Event := [.activate,.sense,.read,.read,.read]

theorem paid_reader_trace (w : W) (archive : Nat → Option Frame) (c : Bool) :
    Generative.Trace (process W) (initial w archive c 20) word
      (run (initial w archive c 20) word) := by
  apply Generative.Trace.cons (show Step _ .activate _ from ⟨by simp [Enabled,initial],rfl⟩)
  apply Generative.Trace.cons (show Step _ .sense _ from ⟨by simp [Enabled,initial,advance],rfl⟩)
  apply Generative.Trace.cons (show Step _ .read _ from ⟨by simp [Enabled,initial,advance],rfl⟩)
  apply Generative.Trace.cons (show Step _ .read _ from ⟨by simp [Enabled,initial,advance],rfl⟩)
  apply Generative.Trace.cons (show Step _ .read _ from ⟨by simp [Enabled,initial,advance],rfl⟩)
  exact .nil _

theorem paid_reader_complete (w : W) (archive : Nat → Option Frame) (c : Bool) :
    Complete (run (initial w archive c 20) word) ∧
    (run (initial w archive c 20) word).fuel=6 ∧ spent word=14 := by
  simp [Complete,run,initial,word,advance,spent,charge]

theorem trace_preserves_facts {s t : State W} {es : List Event} {z : Bool}
    (hf : Facts z s) (h : Generative.Trace (process W) s es t) : Facts z t := by
  induction h with
  | nil => exact hf
  | cons he _ ih =>
      apply ih
      intro i r hr
      rw [step_preserves_archive he] at hr
      exact hf i r hr

theorem actual_archive_paid_certificate {laws : RecipientCorrection.Laws}
    (a : EmissionArchive.State RecipientArchive.World RecipientArchive.Header Frame)
    (context : Bool) (ha : RecipientArchive.ArchiveSound laws a)
    {i : Nat} (hi : i<3) {b : Bool}
    (hb : (run (initial a a.records context 20) word).cache i=some b) :
    b=(RecipientCorrection.lookup laws .recipient == designated i) := by
  have ht := paid_reader_trace a a.records context
  apply completed_paid_cache_sound (paid_reader_complete a a.records context).1
      (trace_cache_agrees (initial_cache_agrees _ _ _ _) ht) _ hi hb
  apply trace_preserves_facts _ ht
  intro i r hr hp hrec
  exact RecipientArchive.completed_record_sound ha hr hp hrec

theorem reachable_archive_paid_certificate {laws : RecipientCorrection.Laws}
    {backing : Nat → Bool} {addresses budget cells : Nat}
    {w : RecipientArchive.World} {a : EmissionArchive.State RecipientArchive.World RecipientArchive.Header Frame}
    {events : List (EmissionArchive.Event RecipientArchive.World RecipientArchive.Event RecipientArchive.Header)}
    (ready : w.core.phase=.ready)
    (history : Generative.Trace (EmissionArchive.process (RecipientArchive.producer laws backing) addresses)
      (EmissionArchive.empty w budget cells) events a)
    (context : Bool) {i : Nat} (hi : i<3) {b : Bool}
    (hb : (run (initial a a.records context 20) word).cache i=some b) :
    b=(RecipientCorrection.lookup laws .recipient == designated i) := by
  apply actual_archive_paid_certificate a context _ hi hb
  exact RecipientArchive.archive_trace_sound
    (RecipientArchive.empty_archive_sound laws w budget cells
      (RecipientArchive.ready_sound laws w ready)) history

end PaidArchiveReader

#print axioms PaidArchiveReader.step_preserves_world
#print axioms PaidArchiveReader.step_preserves_archive
#print axioms PaidArchiveReader.step_ledger
#print axioms PaidArchiveReader.trace_ledger
#print axioms PaidArchiveReader.initial_cache_agrees
#print axioms PaidArchiveReader.step_cache_agrees
#print axioms PaidArchiveReader.trace_cache_agrees
#print axioms PaidArchiveReader.completed_paid_cache_sound
#print axioms PaidArchiveReader.context_change_invalidates
#print axioms PaidArchiveReader.paid_reader_trace
#print axioms PaidArchiveReader.paid_reader_complete
#print axioms PaidArchiveReader.trace_preserves_facts
#print axioms PaidArchiveReader.actual_archive_paid_certificate
#print axioms PaidArchiveReader.reachable_archive_paid_certificate
