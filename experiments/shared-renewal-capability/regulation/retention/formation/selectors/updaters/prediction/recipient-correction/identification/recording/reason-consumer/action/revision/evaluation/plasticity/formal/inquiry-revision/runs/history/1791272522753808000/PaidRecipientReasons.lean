import RecipientReasons

namespace PaidRecipientReasons

set_option maxRecDepth 8192
set_option maxHeartbeats 2000000

open RecipientReasons (Triple normalize derived star)

structure State (W : Type) where
  reader : PaidArchiveReader.State W
  reserve : Nat
  workspace : Bool
  phase : Nat
  normalized : Triple
  conflict : Bool
  working : ReasonReplay.Mask
  published : Option (Bool × ReasonReplay.Mask)
  current : Bool

def initial (reader : PaidArchiveReader.State W) (reserve : Nat) : State W :=
  ⟨reader,reserve,true,0,RecipientReasons.empty,false,ReasonReplay.emptyMask,none,false⟩

def put (t : Triple) (i : Nat) (x : Option Bool) : Triple :=
  if i=0 then {t with first:=x} else if i=1 then {t with second:=x} else {t with third:=x}

def inferred (s : State W) (i : Nat) (access : Bool) : Triple :=
  put s.normalized i (if access then normalize (RecipientArchive.designated i) (s.reader.cache i) else none)

def debit (s : State W) (cost : Nat) : PaidArchiveReader.State W :=
  {s.reader with fuel:=s.reader.fuel-cost}

inductive Event where
  | reader (event : PaidArchiveReader.Event)
  | fund
  | activate
  | infer (index : Nat) (access : Bool)
  | path (path : ReasonReplay.Path)
  | publish
  | cold
  deriving DecidableEq, Repr

def advance (s : State W) : Event → State W
  | .reader e => {s with
      reader:=PaidArchiveReader.advance s.reader e, phase:=0,current:=false}
  | .fund => {s with reader:={s.reader with fuel:=s.reader.fuel+s.reserve}, reserve:=0}
  | .activate => {s with
      reader:=debit s 1,phase:=1,normalized:=RecipientReasons.empty,
      conflict:=false,working:=ReasonReplay.emptyMask,current:=false}
  | .infer i access => {s with
      reader:=debit s 1,phase:=s.phase+1,normalized:=inferred s i access,
      conflict:=RecipientReasons.conflict (inferred s i access)}
  | .path p => {s with
      reader:=debit s (ReasonReplay.pathCost p),phase:=s.phase+1,
      working:=ReasonReplay.applyPath star (derived s.normalized) s.working p}
  | .publish => {s with
      phase:=9,published:=some (s.reader.currentContext,s.working),current:=true}
  | .cold => {s with
      reader:={s.reader with active:=false,token:=none,next:=0,cache:=fun _=>none},
      phase:=0,normalized:=RecipientReasons.empty,conflict:=false,
      working:=ReasonReplay.emptyMask,published:=none,current:=false}

def Enabled (s : State W) : Event → Prop
  | .reader e => PaidArchiveReader.Enabled s.reader e
  | .fund => s.phase=0 ∧ PaidArchiveReader.Complete s.reader
  | .activate => s.workspace=true ∧ s.phase=0 ∧ PaidArchiveReader.Complete s.reader ∧ 1≤s.reader.fuel
  | .infer i _ => s.phase=1+i ∧ i<3 ∧ PaidArchiveReader.Complete s.reader ∧ 1≤s.reader.fuel
  | .path p => s.phase=4+ReasonReplay.pathIndex p ∧ PaidArchiveReader.Complete s.reader ∧
      ReasonReplay.pathCost p≤s.reader.fuel
  | .publish => s.phase=8 ∧ PaidArchiveReader.Complete s.reader
  | .cold => True

def Step (s : State W) (e : Event) (t : State W) : Prop := Enabled s e ∧ t=advance s e

def process (W : Type) : Generative.Process (State W) Event := ⟨Step⟩

def energy (s : State W) : Nat := s.reader.fuel+s.reserve

def charge : Event → Nat
  | .reader e => PaidArchiveReader.charge e
  | .activate | .infer _ _ => 1
  | .path p => ReasonReplay.pathCost p
  | _ => 0

def spent : List Event → Nat | []=>0 | e::es=>charge e+spent es

def run (s : State W) : List Event → State W
  | []=>s
  | e::es=>run (advance s e) es

def reasonWord : List Event :=
  [.activate,.infer 0 true,.infer 1 true,.infer 2 true,
   .path .directP,.path .directQ,.path .viaP,.path .viaQ,.publish]

def factualWord : List Event := PaidArchiveReader.word.map Event.reader

def cycle : List Event := factualWord++reasonWord

def CurrentPublication (s : State W) : Prop :=
  s.current=true ∧ s.phase=9 ∧ PaidArchiveReader.Complete s.reader ∧
  s.published=some (s.reader.currentContext,s.working)

theorem step_ledger {s t : State W} {e : Event} (h : Step s e t) :
    energy t+charge e=energy s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | reader e =>
      have hh := PaidArchiveReader.step_ledger (show PaidArchiveReader.Step _ e _ from ⟨he,rfl⟩)
      simp [energy,advance,charge]; omega
  | fund => simp [energy,advance,charge]
  | activate => simp [energy,advance,charge,debit]; have hf:=he.2.2.2; omega
  | infer i a => simp [energy,advance,charge,debit]; have hf:=he.2.2.2; omega
  | path p => simp [energy,advance,charge,debit]; have hf:=he.2.2; omega
  | publish => simp [energy,advance,charge]
  | cold => simp [energy,advance,charge]

theorem trace_ledger {s t : State W} {es : List Event}
    (h : Generative.Trace (process W) s es t) : energy t+spent es=energy s := by
  induction h with
  | nil => simp [spent]
  | cons hs _ ih => have hh:=step_ledger hs; simp only [spent]; omega

theorem step_preserves_world {s t : State W} {e : Event} (h : Step s e t) :
    t.reader.world=s.reader.world := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | reader e => exact PaidArchiveReader.step_preserves_world ⟨he,rfl⟩
  | fund | activate | infer i a | path p | publish | cold => rfl

theorem step_preserves_archive {s t : State W} {e : Event} (h : Step s e t) :
    t.reader.archive=s.reader.archive := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | reader e => exact PaidArchiveReader.step_preserves_archive ⟨he,rfl⟩
  | fund | activate | infer i a | path p | publish | cold => rfl

theorem reopen_invalidates (s : State W) (e : PaidArchiveReader.Event) :
    ¬ CurrentPublication (advance s (.reader e)) := by simp [CurrentPublication,advance]

theorem same_context_reopen_invalidates (s : State W) :
    ¬ CurrentPublication (advance s (.reader (.contextChange s.reader.currentContext))) :=
  reopen_invalidates s _

theorem cold_retains_resources_and_hardware (s : State W) :
    energy (advance s .cold)=energy s ∧ (advance s .cold).reader.world=s.reader.world ∧
    (advance s .cold).reader.archive=s.reader.archive ∧ (advance s .cold).workspace=s.workspace ∧
    (advance s .cold).reader.cache=(fun _=>none) ∧ (advance s .cold).published=none := by
  exact ⟨rfl,rfl,rfl,rfl,rfl,rfl⟩

theorem no_workspace_no_activation (s : State W) (h : s.workspace=false) : ¬ Enabled s .activate := by
  simp [Enabled,h]

theorem run_append (s : State W) (xs ys : List Event) : run s (xs++ys)=run (run s xs) ys := by
  induction xs generalizing s with
  | nil => rfl
  | cons e xs ih => exact ih _

theorem reason_run_normalized (s : State W) :
    (run s reasonWord).normalized=RecipientReasons.cacheTriple s.reader ∧
    (run s reasonWord).working=ReasonReplay.closureMask star (derived (RecipientReasons.cacheTriple s.reader)) ∧
    (run s reasonWord).reader.fuel=s.reader.fuel-10 ∧
    (run s reasonWord).reserve=s.reserve := by
  simp [run,reasonWord,advance,debit,inferred,put,RecipientReasons.cacheTriple,
    RecipientArchive.designated,ReasonReplay.closureMask,ReasonReplay.paths,
    ReasonReplay.pathCost,Nat.sub_sub]

theorem reason_word_cost : spent reasonWord=10 := by decide

theorem factual_word_cost : spent factualWord=14 := by decide

theorem cycle_cost : spent cycle=24 := by decide

theorem insufficient_ten_blocks_word {s t : State W}
    (h : energy s<10) : ¬ Generative.Trace (process W) s reasonWord t := by
  intro ht
  have hh:=trace_ledger ht
  rw [reason_word_cost] at hh
  omega

theorem funded_reason_trace (s : State W) (hw : s.workspace=true) (hp : s.phase=0)
    (hc : PaidArchiveReader.Complete s.reader) (hf : 10≤s.reader.fuel) :
    Generative.Trace (process W) s reasonWord (run s reasonWord) := by
  apply Generative.Trace.cons (show Step _ (.activate) _ from ⟨by
    simp_all [Enabled,PaidArchiveReader.Complete]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.infer 0 true) _ from ⟨by
    simp_all [Enabled,advance,debit,PaidArchiveReader.Complete]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.infer 1 true) _ from ⟨by
    simp_all [Enabled,advance,debit,PaidArchiveReader.Complete]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.infer 2 true) _ from ⟨by
    simp_all [Enabled,advance,debit,PaidArchiveReader.Complete]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.path .directP) _ from ⟨by
    simp_all [Enabled,advance,debit,PaidArchiveReader.Complete,ReasonReplay.pathIndex,ReasonReplay.pathCost]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.path .directQ) _ from ⟨by
    simp_all [Enabled,advance,debit,PaidArchiveReader.Complete,ReasonReplay.pathIndex,ReasonReplay.pathCost]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.path .viaP) _ from ⟨by
    simp_all [Enabled,advance,debit,PaidArchiveReader.Complete,ReasonReplay.pathIndex,ReasonReplay.pathCost]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.path .viaQ) _ from ⟨by
    simp_all [Enabled,advance,debit,PaidArchiveReader.Complete,ReasonReplay.pathIndex,ReasonReplay.pathCost]; omega,rfl⟩)
  apply Generative.Trace.cons (show Step _ (.publish) _ from ⟨by
    simp_all [Enabled,advance,debit,PaidArchiveReader.Complete,ReasonReplay.pathCost],rfl⟩)
  exact .nil _

theorem reason_run_complete (s : State W) (hc : PaidArchiveReader.Complete s.reader) :
    CurrentPublication (run s reasonWord) := by
  simpa [CurrentPublication,run,reasonWord,advance,debit] using hc

theorem actual_cache_reason_sound {s : State W} {G : Prop} {z : Bool}
    (root : G) (hc : PaidArchiveReader.Complete s.reader)
    (ha : PaidArchiveReader.CacheAgrees s.reader) (hf : PaidArchiveReader.Facts z s.reader)
    {v : ReasonReplay.Node} (hm : (run s reasonWord).working.has v) : RecipientReasons.Meaning G z v := by
  rw [(reason_run_normalized s).2.1] at hm
  exact RecipientReasons.closure_instrumental_sound root
    (RecipientReasons.current_cache_normalizes_sound hc ha hf) hm

theorem step_cache_agrees {s t : State W} {e : Event}
    (hs : PaidArchiveReader.CacheAgrees s.reader) (h : Step s e t) :
    PaidArchiveReader.CacheAgrees t.reader := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | reader e => exact PaidArchiveReader.step_cache_agrees hs ⟨he,rfl⟩
  | cold => simp [advance,PaidArchiveReader.CacheAgrees]
  | fund | activate | infer i a | path p | publish => exact hs

theorem trace_cache_agrees {s t : State W} {es : List Event}
    (hs : PaidArchiveReader.CacheAgrees s.reader)
    (h : Generative.Trace (process W) s es t) : PaidArchiveReader.CacheAgrees t.reader := by
  induction h with
  | nil => exact hs
  | cons he _ ih => exact ih (step_cache_agrees hs he)

theorem trace_preserves_facts {s t : State W} {es : List Event} {z : Bool}
    (hf : PaidArchiveReader.Facts z s.reader)
    (h : Generative.Trace (process W) s es t) : PaidArchiveReader.Facts z t.reader := by
  induction h with
  | nil => exact hf
  | cons he _ ih =>
      apply ih
      intro i r hr
      rw [step_preserves_archive he] at hr
      exact hf i r hr

theorem trace_run {s t : State W} {es : List Event}
    (h : Generative.Trace (process W) s es t) : t=run s es := by
  induction h with
  | nil => rfl
  | cons hs _ ih => rcases hs with ⟨_,rfl⟩; exact ih

theorem reason_run_conflict (s : State W) :
    (run s reasonWord).conflict=RecipientReasons.conflict (RecipientReasons.cacheTriple s.reader) := by
  simp [run,reasonWord,advance,debit,inferred,put,RecipientArchive.designated,RecipientReasons.cacheTriple]

theorem sound_cache_no_runtime_conflict {s : State W} {z : Bool}
    (hc : PaidArchiveReader.Complete s.reader) (ha : PaidArchiveReader.CacheAgrees s.reader)
    (hf : PaidArchiveReader.Facts z s.reader) : (run s reasonWord).conflict=false := by
  rw [reason_run_conflict]
  exact RecipientReasons.sound_no_conflict (RecipientReasons.current_cache_normalizes_sound hc ha hf)

theorem paid_cycle_count_necessary {s t : State W} {es : List Event} {F N : Nat}
    (hf : s.reader.fuel=20) (hr : s.reserve=F-94) (hF : 94≤F)
    (ht : Generative.Trace (process W) s es t) (charged : 24*N≤spent es) : 74+24*N≤F := by
  have hh:=trace_ledger ht
  simp only [energy,hf,hr] at hh
  omega

end PaidRecipientReasons

#print axioms PaidRecipientReasons.step_ledger
#print axioms PaidRecipientReasons.trace_ledger
#print axioms PaidRecipientReasons.step_preserves_world
#print axioms PaidRecipientReasons.step_preserves_archive
#print axioms PaidRecipientReasons.reopen_invalidates
#print axioms PaidRecipientReasons.same_context_reopen_invalidates
#print axioms PaidRecipientReasons.cold_retains_resources_and_hardware
#print axioms PaidRecipientReasons.no_workspace_no_activation
#print axioms PaidRecipientReasons.run_append
#print axioms PaidRecipientReasons.reason_run_normalized
#print axioms PaidRecipientReasons.reason_word_cost
#print axioms PaidRecipientReasons.factual_word_cost
#print axioms PaidRecipientReasons.cycle_cost
#print axioms PaidRecipientReasons.insufficient_ten_blocks_word
#print axioms PaidRecipientReasons.funded_reason_trace
#print axioms PaidRecipientReasons.reason_run_complete
#print axioms PaidRecipientReasons.actual_cache_reason_sound
#print axioms PaidRecipientReasons.step_cache_agrees
#print axioms PaidRecipientReasons.trace_cache_agrees
#print axioms PaidRecipientReasons.trace_preserves_facts
#print axioms PaidRecipientReasons.trace_run
#print axioms PaidRecipientReasons.reason_run_conflict
#print axioms PaidRecipientReasons.sound_cache_no_runtime_conflict
#print axioms PaidRecipientReasons.paid_cycle_count_necessary
