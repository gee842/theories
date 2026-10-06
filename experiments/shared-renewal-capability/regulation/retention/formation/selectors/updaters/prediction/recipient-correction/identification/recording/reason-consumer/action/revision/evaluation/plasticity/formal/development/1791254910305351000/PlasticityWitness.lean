import PairedPlasticity

namespace PlasticityWitness
open PairedPlasticity
set_option maxRecDepth 32768
set_option maxHeartbeats 8000000

def source : Sources := ⟨2,2,2,2,2,2⟩
def entry (v : Variant) (continuation : Bool := false) : State :=
  { parent:=RevisionWitness.consumed,n:=0,count:=0,phase:=.ready, ownBit:=false,recipientBit:=false,cells:=8,adapter:=true,port:=true,portMode:=.idle, readCommand:=none,continuation:=continuation,variant:=v,updates:=true, link0:=none,link1:=none,blanks:=2,replacement:=1,retired:=0,idleParts:=0, training:=22,revision:=12,idleFuel:=0,ownSource:=source,recipientSource:=source,idleSource:=0 }
def laws : RecipientCorrection.Laws := RevisionWitness.changed

def pair (y x : Bool) (replace : Bool := false) : List Event :=
  [.ownPay,.ownReturn (!y),.recipientPay,.recipientReturn (!x),.ownRead .faithful,.recipientRead .faithful] ++
  [if x then (if replace then .replace else .bind) else .skip,.nativeWrite]
def aligned := pair true true++pair false false++pair false false++pair true true
def opposed := pair true false++pair false true++pair false true++pair true false
def mixed := pair true true++pair false true++pair false false++pair true false
def continued := aligned++pair false true true++pair true false

def trained (v : Variant) (word : List Event := aligned) := run laws (entry v) word
def closed (v : Variant) (word : List Event := aligned) := run laws (entry v) (word++[.close])
def chosen (v : Variant) (word : List Event := aligned) := run laws (entry v) (word++[.close,.read,.assess])
def actionWord : List Event := [.attempt]++(RecipientIdentification.trial .recipient true true).map Event.trial
def final := run laws (chosen .active) actionWord

theorem actual_inherited_entry : (entry .active).parent=RevisionWitness.consumed ∧
    fuel (entry .active)=10 ∧ patient (entry .active)=40 ∧ (core (entry .active)).packets=1 ∧
    energy (entry .active)=118 ∧ material (entry .active)=68 ∧
    505=351+36+energy (entry .active) := by decide

theorem empty_conductance : (entry .active).link0=none ∧ (entry .active).link1=none ∧
    rawTransmission (entry .active)=0 ∧ (entry .active).n=0 := by decide

theorem aligned_paid : Runnable laws (entry .active) aligned := by decide
theorem aligned_trace : Generative.Trace (process laws) (entry .active) aligned (trained .active) := runnable_trace aligned_paid

theorem primary_counts_and_links : (trained .active).n=4 ∧ (trained .active).count=4 ∧
    (trained .active).link0=some .positive ∧ (trained .active).link1=some .positive ∧
    (trained .active).blanks=0 ∧ (trained .active).replacement=1 ∧
    fuel (trained .active)=14 ∧ patient (trained .active)=36 ∧
    spent laws (entry .active) aligned=30 ∧ energy (trained .active)=88 := by decide

theorem matched_other_pairings : Runnable laws (entry .active) opposed ∧ Runnable laws (entry .active) mixed ∧
    (trained .active opposed).n=4 ∧ (trained .active mixed).n=4 ∧
    rawTransmission (trained .active opposed)= -8 ∧ rawTransmission (trained .active mixed)=0 ∧
    fuel (trained .active opposed)=14 ∧ fuel (trained .active mixed)=14 ∧
    patient (trained .active opposed)=36 ∧ patient (trained .active mixed)=36 ∧
    energy (trained .active opposed)=88 ∧ energy (trained .active mixed)=88 := by decide

theorem matched_controls_paid : Runnable laws (entry .inert) aligned ∧
    Runnable laws (entry .gated) aligned ∧ Runnable laws (entry .conventional) aligned ∧
    (trained .inert).n=4 ∧ (trained .gated).n=4 ∧ (trained .conventional).n=4 ∧
    energy (trained .inert)=88 ∧ energy (trained .gated)=88 ∧ energy (trained .conventional)=88 ∧
    material (trained .inert)=68 ∧ material (trained .gated)=68 ∧ material (trained .conventional)=68 := by decide

theorem assessment_contrast : Runnable laws (entry .active) (aligned++[.close,.read,.assess]) ∧
    (chosen .active).portMode=.help ∧ (chosen .inert).portMode=.abstain ∧
    (chosen .gated).portMode=.abstain ∧ (chosen .conventional).portMode=.help ∧
    (chosen .active opposed).portMode=.abstain ∧ (chosen .active mixed).portMode=.abstain ∧
    fuel (chosen .active)=12 ∧ fuel (chosen .inert)=12 ∧ fuel (chosen .gated)=12 := by decide

theorem selected_use_paid : Runnable laws (chosen .active) actionWord := by decide
theorem selected_use_trace : Generative.Trace (process laws) (chosen .active) actionWord final := runnable_trace selected_use_paid

theorem selected_same_recipient : fuel final=4 ∧ patient final=46 ∧
    (core final).packets=0 ∧ (core final).hardware.q=(core (entry .active)).hardware.q ∧
    spent laws (chosen .active) actionWord=8 ∧ energy final=78 ∧ material final=68 ∧
    final.portMode=.consumed ∧ ¬Enabled final .attempt ∧ ¬Enabled final (.trial .rent) ∧
    505=351+36+30+10+energy final := by decide

def repaired (v : Variant) := run laws (entry v true) continued
def revisionChosen (v : Variant) := run laws (entry v true) (continued++[.close,.read,.assess])
def revisionFinal := advance laws (revisionChosen .active) .abstain
def frozenFinal := run laws (revisionChosen .frozen) actionWord

theorem actual_replacement_histories : Runnable laws (entry .active true) continued ∧
    Runnable laws (entry .frozen true) continued ∧
    (repaired .active).n=5 ∧ (repaired .frozen).n=5 ∧
    (repaired .active).count=6 ∧ (repaired .frozen).count=6 ∧
    (repaired .active).link0=some .negative ∧ (repaired .frozen).link0=some .positive ∧
    (repaired .active).link1=some .positive ∧ (repaired .frozen).link1=some .positive ∧
    (repaired .active).retired=1 ∧ (repaired .frozen).retired=1 ∧
    (repaired .active).replacement=0 ∧ (repaired .frozen).replacement=0 := by decide

theorem matched_revision_accounts : fuel (repaired .active)=16 ∧ fuel (repaired .frozen)=16 ∧
    patient (repaired .active)=34 ∧ patient (repaired .frozen)=34 ∧
    energy (repaired .active)=72 ∧ energy (repaired .frozen)=72 ∧
    material (repaired .active)=68 ∧ material (repaired .frozen)=68 ∧
    spent laws (entry .active true) continued=46 ∧ spent laws (entry .frozen true) continued=46 := by decide

theorem revision_changes_assessment_not_native_data :
    Runnable laws (entry .active true) (continued++[.close,.read,.assess,.abstain]) ∧
    Runnable laws (entry .frozen true) (continued++[.close,.read,.assess]++actionWord) ∧
    (revisionChosen .active).portMode=.abstain ∧ (revisionChosen .frozen).portMode=.help ∧
    8≤fuel (revisionChosen .active) ∧ 8≤fuel (revisionChosen .frozen) ∧
    energy revisionFinal=70 ∧ energy frozenFinal=62 ∧
    505=351+36+30+16+2+energy revisionFinal ∧
    505=351+36+30+16+10+energy frozenFinal := by decide

def missingWord := [.ownPay,.ownReturn false,.recipientPay,.recipientReturn false,.ownRead .faithful,.recipientRead .missing]
def missingEnd := run laws (entry .active) missingWord

theorem missing_acquisition_blocks_without_zero_write : Runnable laws (entry .active) missingWord ∧
    missingEnd.phase=.missing ∧ missingEnd.n=0 ∧ missingEnd.count=0 ∧
    missingEnd.link0=none ∧ ¬Enabled missingEnd .nativeWrite ∧ ¬Enabled missingEnd .bind ∧
    ¬Enabled missingEnd .ownPay := by decide

def noPacket := {entry .active with recipientSource:={source with a:=0},idleSource:=2}
theorem source_guard_keeps_full_account : energy noPacket=energy (entry .active) ∧
    ¬Enabled noPacket .ownPay := by decide

def oneBlank := {entry .active with blanks:=1,idleParts:=1}
def throughSecondAcquisition := pair true true++pair false false++pair false false++
  [.ownPay,.ownReturn false,.recipientPay,.recipientReturn false,.ownRead .faithful,.recipientRead .faithful]
def oneBlankEnd := run laws oneBlank throughSecondAcquisition

theorem missing_blank_preserves_pending_pair : Runnable laws oneBlank throughSecondAcquisition ∧
    oneBlankEnd.phase=.bothKnown ∧ oneBlankEnd.ownBit=true ∧ oneBlankEnd.recipientBit=true ∧
    oneBlankEnd.n=1 ∧ oneBlankEnd.count=3 ∧ oneBlankEnd.replacement=1 ∧
    ¬Enabled oneBlankEnd .bind ∧ ¬Enabled oneBlankEnd .replace ∧ ¬Enabled oneBlankEnd .nativeWrite ∧
    material oneBlankEnd=68 := by decide

def shortEntry := {entry .active with training:=17,idleFuel:=5}
def shortChosen := run laws shortEntry (aligned++[.close,.read,.assess])
def shortMiss := run laws shortChosen [.attempt,.trial .miss]
theorem funding_shortage_is_real_packet_loss :
    Runnable laws shortEntry (aligned++[.close,.read,.assess,.attempt,.trial .miss]) ∧
    shortChosen.portMode=.help ∧ fuel shortChosen=7 ∧ patient shortChosen=36 ∧
    fuel shortMiss=7 ∧ patient shortMiss=36 ∧ (core shortMiss).packets=0 ∧
    (core shortMiss).active=false ∧ spent laws shortChosen [.attempt,.trial .miss]=10 := by decide

def scoped := advance laws (closed .active) (.scope false)
def denied := advance laws scoped .read
theorem scope_loss_pays_read_but_not_assessment : Enabled scoped .read ∧ fuel scoped=14 ∧
    fuel denied=13 ∧ denied.portMode=.consumed ∧ ¬Enabled denied .assess ∧
    current denied ∧ denied.n=4 ∧ denied.link0=some .positive ∧ denied.link1=some .positive := by decide

def fullWord := aligned++[.close,.read,.assess]++actionWord
theorem whole_suffix_paid : Runnable laws (entry .active) fullWord := by decide
theorem whole_suffix_trace : Generative.Trace (process laws) (entry .active) fullWord final :=
  runnable_trace whole_suffix_paid

/- Actual returned stages, including the complete connected new suffix. -/
theorem staged_actual_connection :
    FormedSelection.Trace 68 PlasticityPreparation.start PlasticityPreparation.word PlasticityPreparation.formed ∧
    ArchivePreparation.AssemblyRunnable ⟨PlasticityPreparation.formed,0,0⟩ PlasticityPreparation.assemblyWord ∧
    PlasticityPreparation.parentProjection PlasticityPreparation.prepared=RevisionPreparation.prepared 227 184 ∧
    Generative.Trace (FreshRevision.bankProcess RevisionWitness.changed) RevisionWitness.start
      (RevisionWitness.word RevisionWitness.changed RevisionWitness.start RevisionWitness.queryWord) RevisionWitness.bankEnd ∧
    Generative.Trace (FreshRevision.actionProcess RevisionWitness.changed) RevisionWitness.reading
      RevisionWitness.consumerWord (entry .active).parent ∧
    Generative.Trace (process laws) (entry .active) fullWord final :=
  ⟨PlasticityPreparation.formation_trace,PlasticityPreparation.assembly_feasible,
    PlasticityPreparation.exact_parent_preparation,RevisionWitness.actual_queries_trace,
    RevisionWitness.actual_consumer_trace,whole_suffix_trace⟩

/- Printed evaluator rows are diagnostics, not proof terms. -/
def corePhaseCode : RecipientIdentification.Phase → Nat
  | .ready => 0 | .rented => 1 | .sensed _ => 2 | .reserved _ => 3
  | .worked _ _ => 4 | .acquired _ _ => 5
def phaseCode : Phase → Nat
  | .ready => 0 | .ownPaid => 1 | .ownReturned => 2 | .recipientPaid => 3
  | .recipientReturned => 4 | .ownKnown => 5 | .bothKnown => 6
  | .missing => 7 | .settled => 8 | .closed => 9
def portCode : PortMode → Nat
  | .idle => 0 | .read => 1 | .help => 2 | .abstain => 3 | .executing => 4 | .consumed => 5
def vector (s : State) : List Int :=
  [s.n,s.count,fuel s,patient s,10*(core s).packets,s.ownSource.total,s.recipientSource.total,
   s.training,s.revision,s.idleFuel,s.idleSource,energy s,conductance s.link0,conductance s.link1,
   occupied s.link0,occupied s.link1,s.blanks,s.replacement,s.retired,s.idleParts,material s,
   if (core s).active then 1 else 0,corePhaseCode (core s).phase,phaseCode s.phase,portCode s.portMode]
def row (name : String) (s : State) : IO Unit :=
  IO.println ("MILESTONE "++name++" ["++String.intercalate "," ((vector s).map toString)++"]")

end PlasticityWitness

#print axioms PlasticityWitness.actual_inherited_entry
#print axioms PlasticityWitness.empty_conductance
#print axioms PlasticityWitness.aligned_paid
#print axioms PlasticityWitness.aligned_trace
#print axioms PlasticityWitness.primary_counts_and_links
#print axioms PlasticityWitness.matched_other_pairings
#print axioms PlasticityWitness.matched_controls_paid
#print axioms PlasticityWitness.assessment_contrast
#print axioms PlasticityWitness.selected_use_paid
#print axioms PlasticityWitness.selected_use_trace
#print axioms PlasticityWitness.selected_same_recipient
#print axioms PlasticityWitness.actual_replacement_histories
#print axioms PlasticityWitness.matched_revision_accounts
#print axioms PlasticityWitness.revision_changes_assessment_not_native_data
#print axioms PlasticityWitness.missing_acquisition_blocks_without_zero_write
#print axioms PlasticityWitness.source_guard_keeps_full_account
#print axioms PlasticityWitness.missing_blank_preserves_pending_pair
#print axioms PlasticityWitness.funding_shortage_is_real_packet_loss
#print axioms PlasticityWitness.scope_loss_pays_read_but_not_assessment
#print axioms PlasticityWitness.whole_suffix_paid
#print axioms PlasticityWitness.whole_suffix_trace
#print axioms PlasticityWitness.staged_actual_connection

open PlasticityWitness PairedPlasticity
#eval row "entry" (entry .active)
#eval row "aligned_trained" (trained .active)
#eval row "aligned_final" (final)
#eval row "inert_final" (advance laws (chosen .inert) .abstain)
#eval row "gated_final" (advance laws (chosen .gated) .abstain)
#eval row "opposed_final" (advance laws (chosen .active opposed) .abstain)
#eval row "mixed_final" (advance laws (chosen .active mixed) .abstain)
#eval row "revision_active_trained" (repaired .active)
#eval row "revision_frozen_trained" (repaired .frozen)
#eval row "revision_active_final" (revisionFinal)
#eval row "revision_frozen_final" (frozenFinal)
#eval row "short_miss" (shortMiss)
#eval row "no_packet" (noPacket)
#eval row "scope_denied" (denied)
