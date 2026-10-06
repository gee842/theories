import AcquiredEvaluation

namespace EvaluationWitness
open AcquiredEvaluation
open RecipientCorrection (packedAct)

set_option maxRecDepth 32768
set_option maxHeartbeats 8000000

/- Exact accepted pre-import endpoint; added parts and stocks were partitioned
at EvaluationPreparation, not created by this state expression. The existing
conditional formal history and the stochastic mixture retain distinct scope. -/
def entry (routing : Routing) : State :=
  {parent:=RevisionWitness.consumed,n:=0,count:=0,mode:=.ready,bit:=false, cells:=6,adapter:=true,routing:=routing,updates:=true,suppressed:=false, training:=12,source0:=2,source1:=2,source2:=2,later:=11,laterSource:=10, port:=true,portMode:=.idle,opportunity:=.firstDue,retired:=0,freeA:=1,freeH:=1}

def lesson (returns : Bool) (channel : Channel) : List Event :=
  [.pay,.returnNative returns,.readNative channel,.writeNative]
def train := lesson false .faithful++lesson false .faithful++lesson false .faithful

def trained (r : Routing) := run RevisionWitness.changed (entry r) train

def choose : List Event := [.read,.assess]
def chosen (r : Routing) := run RevisionWitness.changed (trained r) choose

def selectedTrial : List Event := [.attempt]++
  (RecipientIdentification.trial .recipient true true).map Event.trial++[.close]
def first := run RevisionWitness.changed (chosen .shared) selectedTrial
def second := advance RevisionWitness.changed first .replace
def final := run RevisionWitness.changed second (choose++selectedTrial)
def whole := train++choose++selectedTrial++[.replace]++choose++selectedTrial

theorem inherited_actual_entry : (entry .shared).parent=RevisionWitness.consumed ∧
    (core (entry .shared)).hardware.fuel=10 ∧ (core (entry .shared)).patient=40 ∧
    (core (entry .shared)).packets=1 ∧ energy (entry .shared)=99 ∧ material (entry .shared)=60 := by
  constructor
  · rfl
  · decide

theorem paid_native_runnable : Runnable RevisionWitness.changed (entry .shared) train := by decide
theorem paid_native_trace : Generative.Trace (process RevisionWitness.changed) (entry .shared) train (trained .shared) :=
  runnable_trace paid_native_runnable

theorem acquired_coefficient : (trained .shared).n=7 ∧ (trained .shared).count=3 ∧
    (trained .shared).mode=.closed ∧ fuel (trained .shared)=10 ∧
    (trained .shared).source0=2 ∧ (trained .shared).source1=2 ∧ (trained .shared).source2=2 ∧
    (core (trained .shared)).patient=40 ∧ energy (trained .shared)=87 ∧
    spent RevisionWitness.changed (entry .shared) train=12 := by decide

theorem matched_postperception_training :
    (trained .shared).parent=(trained .filtered).parent ∧
    (trained .shared).n=(trained .filtered).n ∧
    energy (trained .shared)=energy (trained .filtered) ∧
    Known (trained .shared) ∧ Known (trained .filtered) := by
  refine ⟨rfl,rfl,rfl,by decide,by decide⟩

theorem different_paid_decisions :
    Runnable RevisionWitness.changed (trained .shared) choose ∧
    Runnable RevisionWitness.changed (trained .filtered) choose ∧
    (chosen .shared).portMode=.help ∧ (chosen .filtered).portMode=.abstain ∧
    fuel (chosen .shared)=8 ∧ fuel (chosen .filtered)=8 ∧
    (chosen .shared).parent=(chosen .filtered).parent := by
  refine ⟨by decide,by decide,by decide,by decide,by decide,by decide,rfl⟩

theorem first_actual_action : Runnable RevisionWitness.changed (chosen .shared) selectedTrial ∧
    (core first).patient=50 ∧ fuel first=0 ∧ (core first).packets=0 ∧
    first.portMode=.consumed ∧ first.opportunity=.firstClosed ∧ energy first=77 := by decide

theorem paid_carrier_replacement : Enabled first .replace ∧
    second.n=7 ∧ second.count=3 ∧ second.portMode=.idle ∧
    second.opportunity=.secondDue ∧ second.retired=1 ∧ second.freeA=0 ∧ second.freeH=0 ∧
    fuel second=10 ∧ (core second).packets=1 ∧ (core second).patient=50 ∧
    energy second=76 ∧ material second=60 := by decide

theorem retained_data_not_new_learner :
    second.parent.bank=first.parent.bank ∧
    second.parent.parent.reasons.reader.archive=first.parent.parent.reasons.reader.archive ∧
    second.parent.parent.reasons.reader.world.records=first.parent.parent.reasons.reader.world.records ∧
    (core second).hardware.q=(core first).hardware.q ∧
    second.cells=first.cells ∧ second.adapter=first.adapter := ⟨rfl,rfl,rfl,rfl,rfl,rfl⟩

theorem second_actual_action : Runnable RevisionWitness.changed second (choose++selectedTrial) ∧
    fuel final=0 ∧ (core final).patient=60 ∧ (core final).packets=0 ∧
    final.source0+final.source1+final.source2=6 ∧ final.later=0 ∧ final.laterSource=0 ∧
    final.opportunity=.finished ∧ final.portMode=.consumed ∧
    energy final=66 ∧ material final=60 := by decide

theorem whole_actual_trace : Generative.Trace (process RevisionWitness.changed)
    (entry .shared) whole final := by
  exact runnable_trace (by decide)

theorem complete_accounts : spent RevisionWitness.changed (entry .shared) whole=33 ∧
    476=351+26+12+10+11+66 ∧ energy (entry .shared)=33+energy final := by decide

def filteredFirst := run RevisionWitness.changed (chosen .filtered) [.abstain,.close]
def filteredSecond := advance RevisionWitness.changed filteredFirst .replace
def filteredFinal := run RevisionWitness.changed filteredSecond (choose++[.abstain,.close])

theorem exclusion_with_equal_facts : Runnable RevisionWitness.changed (chosen .filtered) [.abstain,.close] ∧
    Enabled filteredFirst .replace ∧
    Runnable RevisionWitness.changed filteredSecond (choose++[.abstain,.close]) ∧
    (core filteredFinal).patient=40 ∧ fuel filteredFinal=16 ∧
    (core filteredFinal).packets=2 ∧ filteredFinal.n=7 ∧ Known filteredFinal ∧
    energy filteredFinal=82 := by decide

def cut := advance RevisionWitness.changed (chosen .shared) (.permission false)
def blocked := advance RevisionWitness.changed cut .attempt

theorem authority_is_not_valuation : cut.portMode=.help ∧ Known cut ∧ cut.n=7 ∧
    Enabled cut .attempt ∧ blocked.portMode=.consumed ∧
    (core blocked).patient=40 ∧ fuel blocked=8 ∧
    ¬Enabled blocked (.trial .rent) := by decide

def stale := advance RevisionWitness.changed (advance RevisionWitness.changed (trained .shared) .read) (.reason .cold)
theorem stale_read_has_no_assessment : stale.portMode=.consumed ∧ ¬Enabled stale .assess ∧
    stale.n=7 ∧ fuel stale=9 := by decide

theorem completed_capacity_is_finite : ¬Enabled final .replace ∧ ¬Enabled final .pay ∧
    ¬Enabled final .read ∧ ¬Enabled final (.trial .rent) := by decide

end EvaluationWitness

#print axioms EvaluationWitness.inherited_actual_entry
#print axioms EvaluationWitness.paid_native_runnable
#print axioms EvaluationWitness.paid_native_trace
#print axioms EvaluationWitness.acquired_coefficient
#print axioms EvaluationWitness.matched_postperception_training
#print axioms EvaluationWitness.different_paid_decisions
#print axioms EvaluationWitness.first_actual_action
#print axioms EvaluationWitness.paid_carrier_replacement
#print axioms EvaluationWitness.retained_data_not_new_learner
#print axioms EvaluationWitness.second_actual_action
#print axioms EvaluationWitness.whole_actual_trace
#print axioms EvaluationWitness.complete_accounts
#print axioms EvaluationWitness.exclusion_with_equal_facts
#print axioms EvaluationWitness.authority_is_not_valuation
#print axioms EvaluationWitness.stale_read_has_no_assessment
#print axioms EvaluationWitness.completed_capacity_is_finite
