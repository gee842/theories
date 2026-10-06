import PretrainingEvidence

namespace PretrainingEvidence.Enumeration
open PairedPlasticity
set_option maxRecDepth 32768
set_option maxHeartbeats 4000000

def word (own recipient : Nat) : List Event :=
  (List.range 4).flatMap (fun i => PlasticityWitness.pair (own.testBit i) (recipient.testBit i))

/-- Observe the actual admitted prefix, stopping before the first rejected event.
    In particular an inadmissible four-pair word is not run to a fictitious end. -/
def walk (s : State) : List Event → Nat × Bool × State
  | [] => (0,true,s)
  | e::es =>
    if Enabled s e then
      let (k,done,t) := walk (advance PlasticityWitness.laws s e) es
      (k+1,done,t)
    else (0,false,s)

def signCode : Option Sign → Int
  | none => 0
  | some .negative => -1
  | some .inert => 2
  | some .positive => 1

def phaseCode : Phase → Nat
  | .ready => 0
  | .ownPaid => 1
  | .ownReturned => 2
  | .recipientPaid => 3
  | .recipientReturned => 4
  | .ownKnown => 5
  | .bothKnown => 6
  | .missing => 7
  | .settled => 8
  | .closed => 9

def row (own recipient : Nat) : List Int :=
  let (steps,done,s) := walk (PlasticityWitness.entry .active true) (word own recipient)
  [own,recipient,(if done then 1 else 0),steps,s.count,s.n,patient s,fuel s,
    sockets s,s.retired,s.blanks,signCode s.link0,signCode s.link1,
    (if s.ownBit then 1 else 0),(if s.recipientBit then 1 else 0),phaseCode s.phase,
    s.training,s.revision,s.ownSource.total,s.recipientSource.total,energy s,
    (if Enabled s .ownPay then 1 else 0)]

def emit : IO Unit := do
  for own in List.range 16 do
    for recipient in List.range 16 do
      IO.println s!"PRETRAINING {repr (row own recipient)}"

#eval emit
end PretrainingEvidence.Enumeration
