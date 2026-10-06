import EvaluativeSuccession

namespace SuccessionWitness
open EvaluativeSuccession
open RecipientCorrection (Laws packedAct)
set_option maxRecDepth 32768
set_option maxHeartbeats 8000000

/-- This is the actual exhausted accepted donor, with only prospectively
isolated successor reserves added by the preparation projection. -/
def entry := enter EvaluationWitness.final .shared
def changed : Laws := (false,true)
def assemblyWord : List Event := List.replicate 8 .assemble
def assembled := run changed entry assemblyWord
def copyWord : List Event := [.copyRead,.copyWrite false true true true]
def copied := run changed assembled copyWord
def releaseWord : List Event := [.bindAccess true,.release]
def released := run changed copied releaseWord
def firstStart := advance changed released .probeStart

inductive Command where
  | core (event : RecipientIdentification.Event)
  | bind | write

def toOld (laws : Laws) (s : State) : Command → PublicationBridge.ArchiveEvent
  | .core e => .core (.core e) (RecipientArchive.advance laws (archive s).world (.core e))
  | .bind => .bind 1 ⟨1,true,packedAct s.core.hardware.q .recipient⟩
  | .write => .write

def runBank (laws : Laws) (s : State) : List Command → State
  | []=>s
  | e::es=>runBank laws (advance laws s (.bank (toOld laws s e))) es

def bankWord (laws : Laws) (s : State) : List Command → List PublicationBridge.ArchiveEvent
  | []=>[]
  | e::es=>toOld laws s e::bankWord laws (advance laws s (.bank (toOld laws s e))) es

def BankRunnable (laws : Laws) (s : State) : List Command → Prop
  | []=>True
  | e::es=>Enabled laws s (.bank (toOld laws s e)) ∧
      BankRunnable laws (advance laws s (.bank (toOld laws s e))) es

instance bankRunnableDecidable (laws : Laws) (s : State) (es : List Command) : Decidable (BankRunnable laws s es) :=
  match es with
  | []=>isTrue trivial
  | e::es=>
    let _:=bankRunnableDecidable laws (advance laws s (.bank (toOld laws s e))) es
    inferInstanceAs (Decidable (Enabled laws s (.bank (toOld laws s e)) ∧ _))

theorem runnable_bank_trace {laws : Laws} {s : State} {es : List Command}
    (h : BankRunnable laws s es) : Generative.Trace (process laws) s
      ((bankWord laws s es).map Event.bank) (runBank laws s es) := by
  induction es generalizing s with
  | nil=>exact .nil _
  | cons e es ih=>exact .cons ⟨h.1,rfl⟩ (ih h.2)

def firstWord := (RecipientIdentification.trial .recipient true true).map Command.core
def firstEnd := runBank changed firstStart firstWord
def betweenWord : List Event := [.probeEnd,.probeStart]
def secondStart := run changed firstEnd betweenWord
def secondWord : List Command := [.core .rent,.core (.sense .recipient),.bind,
  .core .reserve,.core (.work true),.core (.acquire true),.core .write,
  .write,.write,.write,.write]
def bankEnd := runBank changed secondStart secondWord
def prepareWord : List Event := [.probeEnd,.prepare]
def reading := run changed bankEnd prepareWord
def consumerWord := PaidRecipientReasons.cycle.map Event.reason
def consumed := run changed reading consumerWord
def choiceWord : List Event := [.read,.assess]
def chosen := run changed consumed choiceWord
def acting := advance changed chosen .attempt
def selectedWord := (RecipientIdentification.trial .recipient true true).map Event.trial
def final := run changed acting selectedWord

theorem actual_donor_admissible : Admissible EvaluationWitness.final := by decide

theorem actual_entry : entry=enter EvaluationWitness.final .shared ∧ energy entry=162 ∧
    material entry=78 ∧ entry.core.hardware.q=0 ∧ entry.core.hardware.fuel=0 ∧
    entry.core.patient=60 ∧ entry.native.n=7 ∧ entry.native.energy=6 := by
  exact ⟨rfl,by decide,by decide,by decide,by decide,by decide,by decide,by decide⟩

theorem eight_assemblies : Runnable changed entry assemblyWord ∧
    assembled.installed=8 ∧ assembled.held=1 ∧ assembled.cursor=8 ∧
    energy assembled=154 ∧ assembled.window=true := by decide

theorem paid_actual_copy : Runnable changed assembled copyWord ∧
    copied.life=.committed ∧ copied.core.hardware.q=0 ∧ copied.core.hardware.last=false ∧
    copied.core.patient=60 ∧ copied.core.hardware.fuel=0 ∧ copied.copyFund=0 ∧
    energy copied=152 ∧ copied.history=entry.history ∧ copied.native=entry.native := by
  refine ⟨by decide,by decide,by decide,by decide,by decide,by decide,by decide,by decide,rfl,rfl⟩

theorem paid_binding_release : Runnable changed copied releaseWord ∧
    released.life=.child ∧ released.installed=9 ∧ released.held=0 ∧
    released.core.hardware.fuel=26 ∧ released.core.packets=3 ∧ released.core.patient=60 ∧
    released.bank.budget=5 ∧ released.readerFund=24 ∧ energy released=151 ∧
    released.reader.current=false ∧ released.reader.published=none := by decide

theorem first_probe_runnable : Enabled changed released .probeStart ∧
    BankRunnable changed firstStart firstWord := by decide

theorem first_probe_actual : firstEnd.core.hardware.q=2 ∧ firstEnd.core.hardware.last=false ∧
    firstEnd.core.hardware.fuel=18 ∧ firstEnd.core.packets=2 ∧ firstEnd.core.patient=60 ∧
    firstEnd.bank.next=1 ∧ firstEnd.bank.records 1=none ∧ firstEnd.probeRunning=false ∧
    energy firstEnd=133 := by decide

theorem second_probe_runnable : Runnable changed firstEnd betweenWord ∧
    BankRunnable changed secondStart secondWord := by decide

theorem fresh_acquisition : bankEnd.bank.records 0=none ∧
    bankEnd.bank.records 1=some ⟨true,true,true,true⟩ ∧ bankEnd.bank.records 2=none ∧
    bankEnd.bank.next=2 ∧ bankEnd.bank.blanks=0 ∧ bankEnd.bank.budget=0 ∧ bankEnd.bank.escrow=0 ∧
    bankEnd.core.hardware.q=2 ∧ bankEnd.core.hardware.last=true ∧
    bankEnd.core.hardware.fuel=10 ∧ bankEnd.core.packets=1 ∧ bankEnd.core.patient=70 ∧
    bankEnd.history.hardware.q=0 ∧ energy bankEnd=120 := by decide

theorem actual_consumer_runnable : Runnable changed bankEnd prepareWord ∧
    Runnable changed reading consumerWord := by decide

theorem actual_new_publication : consumed.core.hardware.q=2 ∧ consumed.core.hardware.fuel=10 ∧
    consumed.core.patient=70 ∧ consumed.reader.reader.fuel=0 ∧ consumed.reader.reserve=0 ∧
    Current consumed ∧ command consumed=some true ∧ Known consumed ∧ energy consumed=96 := by decide

theorem acquired_assessment : Runnable changed consumed choiceWord ∧
    chosen.port=.help ∧ chosen.core.hardware.fuel=8 ∧ chosen.core.patient=70 ∧
    chosen.native.n=7 ∧ Known chosen ∧ energy chosen=94 := by decide

theorem actual_selected_action : Enabled changed chosen .attempt ∧ Runnable changed acting selectedWord ∧
    final.core.hardware.q=2 ∧ final.core.hardware.last=true ∧ final.core.hardware.fuel=0 ∧
    final.core.packets=0 ∧ final.core.patient=80 ∧ final.native.n=7 ∧ final.native.energy=6 ∧
    final.port=.consumed ∧ final.closed=true ∧ energy final=86 ∧ material final=78 := by decide


theorem first_probe_trace : Generative.Trace (process changed) firstStart
    ((bankWord changed firstStart firstWord).map Event.bank) firstEnd :=
  runnable_bank_trace first_probe_runnable.2

theorem second_probe_trace : Generative.Trace (process changed) secondStart
    ((bankWord changed secondStart secondWord).map Event.bank) bankEnd :=
  runnable_bank_trace second_probe_runnable.2

theorem actual_consumer_trace : Generative.Trace (process changed) reading consumerWord consumed :=
  runnable_trace actual_consumer_runnable.2

theorem actual_new_facts : PaidArchiveReader.Facts true
    (PaidArchiveReader.initial () bankEnd.bank.records true 24) := by
  apply fresh_bank_facts (s:=secondStart) (laws:=changed)
    (w:=(archive secondStart).world) (budget:=5) (cells:=4)
  · rfl
  · decide
  · exact second_probe_trace

theorem reading_reader_exact : reading.reader=
    PaidRecipientReasons.initial (PaidArchiveReader.initial () bankEnd.bank.records true 24) 0 := by rfl

theorem actual_fresh_reasons {G : Prop} (root : G) :
    PublicationBridge.Assured true G consumed.reader := by
  have hc:Generative.Trace (PaidRecipientReasons.process Unit) reading.reader
      PaidRecipientReasons.cycle consumed.reader:=reader_trace_projects actual_consumer_trace
  rw [reading_reader_exact] at hc
  exact PublicationBridge.initialized_trace_assured root
    (PaidArchiveReader.initial_cache_agrees _ _ _ _) actual_new_facts hc

theorem acting_reader_exact : acting.reader=consumed.reader :=
  (attempt_reader changed chosen).trans (choice_reader changed consumed)

theorem selected_current_reason {G : Prop} (root : G) :
    G ∧ RecipientReasons.Meaning G true (RecipientAction.commandNode true) := by
  have h:PublicationBridge.Assured true G acting.reader:=
    (congrArg (PublicationBridge.Assured true G) acting_reader_exact).mpr (actual_fresh_reasons root)
  have hk:Known acting:=by decide
  have hm:=warranted_instrumental_meaning (s:=acting) h hk
  have ha:packedAct acting.core.hardware.q .recipient=true:=by decide
  rw [ha] at hm
  exact hm

theorem actual_effect_from_fresh_evidence : final.core.patient=acting.core.patient+10 ∧
    packedAct final.core.hardware.q .actor=packedAct acting.core.hardware.q .actor := by
  have h:PublicationBridge.Assured true True acting.reader:=
    (congrArg (PublicationBridge.Assured true True) acting_reader_exact).mpr (actual_fresh_reasons trivial)
  exact selected_physical_effect (observed:=changed) (used:=changed) (s:=acting) (t:=final)
    h (by decide) rfl (runnable_trace actual_selected_action.2.1)

def setupWord := assemblyWord++copyWord++releaseWord++[.probeStart]
def firstSegment := (bankWord changed firstStart firstWord).map Event.bank++betweenWord
def secondSegment := (bankWord changed secondStart secondWord).map Event.bank++prepareWord
def prefixWord := setupWord++firstSegment++secondSegment++consumerWord
def suffix := choiceWord++[.attempt]++selectedWord
def whole := prefixWord++suffix

theorem setup_trace : Generative.Trace (process changed) entry setupWord firstStart := by
  have h1:=Generative.trace_append_iff.mpr
    ⟨assembled,runnable_trace eight_assemblies.1,runnable_trace paid_actual_copy.1⟩
  have h2:=Generative.trace_append_iff.mpr ⟨copied,h1,runnable_trace paid_binding_release.1⟩
  exact Generative.trace_append_iff.mpr ⟨released,h2,
    .cons ⟨first_probe_runnable.1,rfl⟩ (.nil _)⟩

theorem prefix_trace : Generative.Trace (process changed) entry prefixWord consumed := by
  have h1:Generative.Trace (process changed) firstStart firstSegment secondStart:=
    Generative.trace_append_iff.mpr ⟨firstEnd,first_probe_trace,runnable_trace second_probe_runnable.1⟩
  have h2:Generative.Trace (process changed) secondStart secondSegment reading:=
    Generative.trace_append_iff.mpr ⟨bankEnd,second_probe_trace,runnable_trace actual_consumer_runnable.1⟩
  have h3:=Generative.trace_append_iff.mpr ⟨firstStart,setup_trace,h1⟩
  have h4:=Generative.trace_append_iff.mpr ⟨secondStart,h3,h2⟩
  exact Generative.trace_append_iff.mpr ⟨reading,h4,actual_consumer_trace⟩

theorem suffix_trace : Generative.Trace (process changed) consumed suffix final := by
  have h1:Generative.Trace (process changed) consumed (choiceWord++[.attempt]) acting:=
    Generative.trace_append_iff.mpr ⟨chosen,runnable_trace acquired_assessment.1,
      .cons ⟨actual_selected_action.1,rfl⟩ (.nil _)⟩
  exact Generative.trace_append_iff.mpr ⟨acting,h1,runnable_trace actual_selected_action.2.1⟩

theorem whole_actual_trace : Generative.Trace (process changed) entry whole final :=
  Generative.trace_append_iff.mpr ⟨consumed,prefix_trace,suffix_trace⟩

theorem complete_accounts : spent changed entry whole=76 ∧
    energy entry=76+energy final ∧ 590=410+18+66+10+86 ∧
    material final=material entry := by
  have h:=trace_energy whole_actual_trace
  have hi:energy entry=162:=actual_entry.2.1
  have hf:energy final=86:=by decide
  exact ⟨by omega,by omega,by decide,trace_material whole_actual_trace⟩

/-- Staged isolation joins the actual preparation and accepted donor history.
It is not an erasure theorem for a stochastic M78 machine. -/
theorem actual_staged_composition :
    FormedSelection.Trace 78 (SuccessionPreparation.start 360 230) SuccessionPreparation.word
      (SuccessionPreparation.formed 360 230) ∧
    ArchivePreparation.AssemblyRunnable ⟨SuccessionPreparation.formed 360 230,0,0⟩ SuccessionPreparation.assemblyWord ∧
    SuccessionPreparation.parentProjection (SuccessionPreparation.prepared 360 230)=EvaluationPreparation.prepared 276 200 ∧
    FreshRevision.OpenStep RevisionWitness.entry RevisionWitness.start ∧
    Generative.Trace (FreshRevision.bankProcess RevisionWitness.changed) RevisionWitness.start
      (RevisionWitness.word RevisionWitness.changed RevisionWitness.start RevisionWitness.queryWord) RevisionWitness.bankEnd ∧
    FreshRevision.PrepareStep RevisionWitness.bankEnd RevisionWitness.reading ∧
    Generative.Trace (FreshRevision.actionProcess RevisionWitness.changed) RevisionWitness.reading
      RevisionWitness.consumerWord RevisionWitness.consumed ∧
    (EvaluationWitness.entry .shared).parent=RevisionWitness.consumed ∧
    Generative.Trace (AcquiredEvaluation.process RevisionWitness.changed)
      (EvaluationWitness.entry .shared) EvaluationWitness.whole EvaluationWitness.final ∧
    entry=enter EvaluationWitness.final .shared ∧
    energy entry=AcquiredEvaluation.energy EvaluationWitness.final+96 ∧
    material entry=AcquiredEvaluation.material EvaluationWitness.final+18 ∧
    Generative.Trace (process changed) entry whole final := by
  exact ⟨SuccessionPreparation.prospective_formation_trace,
    SuccessionPreparation.assemblies_feasible,SuccessionPreparation.exact_parent_prepared_projection,
    RevisionWitness.actual_composed_history.1,RevisionWitness.actual_queries_trace,
    RevisionWitness.actual_composed_history.2.2.1,RevisionWitness.actual_consumer_trace,
    EvaluationWitness.retained_exact,EvaluationWitness.whole_actual_trace,rfl,
    (entry_accounts _ _).1,by decide,whole_actual_trace⟩

/-- Equal factual/physical prefixWord; the different routing recipe is explicit. -/
def filteredEntry := enter EvaluationWitness.final .filtered
def filteredConsumed := routed consumed .filtered
def filteredChosen := run changed filteredConsumed choiceWord
def filteredFinal := advance changed filteredChosen .abstain

local instance (e : Event) : Decidable (e=.assess) := by
  cases e <;> first | exact isTrue rfl | exact isFalse (fun h=>Event.noConfusion h)

theorem prefix_without_assessment : ∀ e∈prefixWord,e≠.assess := by decide

theorem filtered_consumed_exact : run changed filteredEntry prefixWord=filteredConsumed := by
  have hr:=run_route changed entry .filtered prefixWord prefix_without_assessment
  have he:routed entry .filtered=filteredEntry:=enter_route _ _ _
  exact (congrArg (fun x=>run changed x prefixWord) he).symm.trans
    (hr.trans (congrArg (fun x=>routed x .filtered) (trace_run prefix_trace).symm))

theorem filtered_actual_prefix : Generative.Trace (process changed) filteredEntry prefixWord filteredConsumed := by
  have ht:=trace_route prefix_trace .filtered prefix_without_assessment
  have he:routed entry .filtered=filteredEntry:=enter_route _ _ _
  exact (congrArg (fun x=>Generative.Trace (process changed) x prefixWord filteredConsumed) he).mp ht

theorem equal_information_filter : filteredConsumed.reader=consumed.reader ∧
    filteredConsumed.core=consumed.core ∧ filteredConsumed.native=consumed.native ∧
    Runnable changed filteredConsumed choiceWord ∧ filteredChosen.port=.abstain ∧
    Enabled changed filteredChosen .abstain ∧ filteredFinal.core.patient=70 ∧
    filteredFinal.core.hardware.fuel=8 ∧ filteredFinal.core.packets=1 ∧ energy filteredFinal=94 := by
  refine ⟨?_,?_,?_,by decide,by decide,by decide,by decide,by decide,by decide,by decide⟩
  · exact (routed_data consumed .filtered).1
  · exact (routed_data consumed .filtered).2.1
  · exact (routed_data consumed .filtered).2.2

def permissionCut := advance changed chosen (.permission false)
def blocked := advance changed permissionCut .attempt

theorem permission_does_not_remove_reason : Known permissionCut ∧ permissionCut.port=.help ∧
    permissionCut.reader=chosen.reader ∧ permissionCut.native=chosen.native ∧
    Enabled changed permissionCut .attempt ∧ blocked.port=.consumed ∧
    blocked.core.patient=70 ∧ blocked.core.hardware.fuel=8 ∧ ¬Enabled changed blocked (.trial .rent) := by
  refine ⟨by decide,by decide,(permission_data changed chosen false).1,
    (permission_data changed chosen false).2,by decide,by decide,by decide,by decide,by decide⟩

def inaccessible := advance changed consumed (.access false)
def unknown := advance changed inaccessible .read

theorem unavailable_influence_attempt_is_paid : Enabled changed inaccessible .read ∧
    unknown.port=.consumed ∧ unknown.closed=true ∧ unknown.core.hardware.fuel=9 ∧
    unknown.native.n=7 ∧ Current unknown ∧ ¬Enabled changed unknown .assess := by decide

def retiredRead := advance changed consumed .read
def lostAfterRead := advance changed retiredRead (.access false)
theorem access_cut_invalidates_pending_read : lostAfterRead.port=.consumed ∧
    lostAfterRead.core.hardware.fuel=9 ∧ lostAfterRead.native.n=7 ∧
    ¬Enabled changed lostAfterRead .assess := by decide

theorem finite_successor_capacity : ¬Enabled changed final .copyRead ∧
    ¬Enabled changed final .probeStart ∧ ¬Enabled changed final .read ∧
    ¬Enabled changed final (.trial .rent) ∧ final.history.hardware.q=0 ∧
    final.core.hardware.q=2 := by decide

end SuccessionWitness

#print axioms SuccessionWitness.runnable_bank_trace
#print axioms SuccessionWitness.actual_donor_admissible
#print axioms SuccessionWitness.actual_entry
#print axioms SuccessionWitness.eight_assemblies
#print axioms SuccessionWitness.paid_actual_copy
#print axioms SuccessionWitness.paid_binding_release
#print axioms SuccessionWitness.first_probe_runnable
#print axioms SuccessionWitness.first_probe_actual
#print axioms SuccessionWitness.second_probe_runnable
#print axioms SuccessionWitness.fresh_acquisition
#print axioms SuccessionWitness.actual_consumer_runnable
#print axioms SuccessionWitness.actual_new_publication
#print axioms SuccessionWitness.acquired_assessment
#print axioms SuccessionWitness.actual_selected_action
#print axioms SuccessionWitness.first_probe_trace
#print axioms SuccessionWitness.second_probe_trace
#print axioms SuccessionWitness.actual_consumer_trace
#print axioms SuccessionWitness.actual_new_facts
#print axioms SuccessionWitness.reading_reader_exact
#print axioms SuccessionWitness.actual_fresh_reasons
#print axioms SuccessionWitness.acting_reader_exact
#print axioms SuccessionWitness.selected_current_reason
#print axioms SuccessionWitness.actual_effect_from_fresh_evidence
#print axioms SuccessionWitness.setup_trace
#print axioms SuccessionWitness.prefix_trace
#print axioms SuccessionWitness.suffix_trace
#print axioms SuccessionWitness.whole_actual_trace
#print axioms SuccessionWitness.complete_accounts
#print axioms SuccessionWitness.actual_staged_composition
#print axioms SuccessionWitness.prefix_without_assessment
#print axioms SuccessionWitness.filtered_consumed_exact
#print axioms SuccessionWitness.filtered_actual_prefix
#print axioms SuccessionWitness.equal_information_filter
#print axioms SuccessionWitness.permission_does_not_remove_reason
#print axioms SuccessionWitness.unavailable_influence_attempt_is_paid
#print axioms SuccessionWitness.access_cut_invalidates_pending_read
#print axioms SuccessionWitness.finite_successor_capacity
