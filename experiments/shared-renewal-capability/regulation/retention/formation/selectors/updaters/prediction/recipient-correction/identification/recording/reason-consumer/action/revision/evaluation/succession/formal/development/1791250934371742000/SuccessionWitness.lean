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

end SuccessionWitness
